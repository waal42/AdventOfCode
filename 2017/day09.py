from time import time
start = time()

with open('day09input.txt', 'r') as file_input:
    fin = file_input.read()


def remove_garbage(strin):
    stream_list = list()
    len_strin = len(strin)
    garbage = False
    ignore_next = False
    for i in range(len_strin):
        if ignore_next:
            ignore_next = False
        elif strin[i] == '!':
            ignore_next = True
        elif strin[i] == '<' and not ignore_next:
            garbage = True
        elif strin[i] == '>' and not ignore_next:
            garbage = False
        elif not garbage and not ignore_next:
            stream_list.append(strin[i])
    stream = ''.join(stream_list)
    return stream


def count_garbage(strin):
    len_strin = len(strin)
    garbage = False
    ignore_next = False
    count = 0
    for i in range(len_strin):
        if ignore_next:
            ignore_next = False
        elif strin[i] == '!':
            ignore_next = True
        elif strin[i] == '<' and not ignore_next and not garbage:
            garbage = True
        elif strin[i] == '>' and not ignore_next:
            garbage = False
        elif garbage:
            count += 1
    return count


def count_score(groups):
    count = 0
    level = 0
    score = 0
    for char in groups:
        if char == '{':
            level += 1
            count += 1
        if char == '}':
            score += level
            level -= 1
    return score


print(count_score(remove_garbage(fin)))
print(count_garbage(fin))

runtime = time() - start
print('finished in ' + str(runtime) + ' seconds')