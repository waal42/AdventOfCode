from time import time
start = time()

day10input = ('165,1,255,31,87,52,24,113,0,91,148,254,158,2,73,153', 256)
day10testinput = ('3,4,1,5', 5)
trailing = [17, 31, 73, 47, 23]


def to_ascii_with_trailing(string):
    output = list()
    for code in string.encode('ascii'):
        output.append(code)
    output += trailing
    return output


def knot_hash(data):
    cycles = [int(x) for x in data[0].split(',')]
    size = data[1]
    position = 0
    skip = 0
    knot = [x for x in range(size)]
    for cycle in cycles:
        if cycle != 1:
            if cycle + position > size:
                length = cycle
                tied = knot[position:cycle+position]
                # print(tied)
                length -= len(tied)
                tied += knot[0:length]
                tied.reverse()
            else:
                tied = knot[position:cycle+position][::-1]
            # print(tied)
            for i in range(cycle):
                knot[(position + i) % size] = tied[i]
        position = (position + cycle + skip) % size
        skip += 1
        # print(knot, position, skip)
    print(knot[0]*knot[1])


def count_dense_hash(data):
    cycles = to_ascii_with_trailing(data[0])
    size = data[1]
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
    print(str_dense_hash)


knot_hash(day10input)
count_dense_hash(day10input)

runtime = time() - start
print('finished in ' + str(runtime) + ' seconds')
