from time import time

start = time()
day14testinput = 'stpzcrnm'
trailing = [17, 31, 73, 47, 23]


def to_ascii_with_trailing(string):
    output = list()
    for code in string.encode('ascii'):
        output.append(code)
    output += trailing
    return output


def count_dense_hash(data):
    cycles = to_ascii_with_trailing(data)
    size = 256
    position = 0
    skip = 0
    sparse_hash = [x for x in range(size)]
    for i in range(64):
        for cycle in cycles:
            if cycle != 1:
                if cycle + position > size:
                    length = cycle
                    tied = sparse_hash[position:cycle + position]
                    # print(tied)
                    length -= len(tied)
                    tied += sparse_hash[0:length]
                    tied.reverse()
                else:
                    tied = sparse_hash[position:cycle + position][::-1]
                # print(tied)
                for j in range(cycle):
                    sparse_hash[(position + j) % size] = tied[j]
            position = (position + cycle + skip) % size
            skip += 1
    dense_hash = list()
    position = 0
    for k in range(16):
        sub_sparse_hash = sparse_hash[k*16:k*16 + 16]
        sub_dense_hash = 0
        for number in sub_sparse_hash:
            sub_dense_hash ^= number
        hex_sub_dense_hash = hex(sub_dense_hash)[2:]\
            if len(hex(sub_dense_hash)[2:]) == 2\
            else '0' + hex(sub_dense_hash)[2:]
        dense_hash.append(hex_sub_dense_hash)
    str_dense_hash = ''.join(dense_hash)
    return str_dense_hash

def hextobin(hexval):
    '''
    Takes a string representation of hex data with
    arbitrary length and converts to string representation
    of binary.  Includes padding 0s
    '''
    thelen = len(hexval)*4
    binval = bin(int(hexval, 16))[2:]
    while ((len(binval)) < thelen):
        binval = '0' + binval
    return binval


def solution():
    ones = 0
    for i in range(128):
        to_hash = day14testinput + '-' + str(i)
        hex_hash = count_dense_hash(to_hash)
        bin_hash = hextobin(hex_hash)
        for char in bin_hash:
            if char == '1':
                ones += 1
    print(ones)


def depth_first_search(grid, row, col):
    len_rows = len(grid)
    len_cols = len(grid[0])
    if row < 0 or col < 0 or row >= len_rows or col >= len_cols or grid[row][col] == '0':
        return
    grid[row][col] = '0'
    depth_first_search(grid, row - 1, col)
    depth_first_search(grid, row + 1, col)
    depth_first_search(grid, row, col - 1)
    depth_first_search(grid, row, col + 1)


def solution_two():
    grid = list()
    islands = 0
    for i in range(128):
        to_hash = day14testinput + '-' + str(i)
        hex_hash = count_dense_hash(to_hash)
        grid.append([i for i in hextobin(hex_hash)])
    len_rows = len(grid)
    len_cols = len(grid[0])
    for row in range(len_rows):
        for col in range(len_cols):
            if grid[row][col] == '1':
                islands += 1
                depth_first_search(grid, row, col)
    print(islands)


solution_two()

print('finished in ' + str(time() - start) + ' seconds')