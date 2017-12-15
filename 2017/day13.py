from time import time
import re
start = time()

firewall = dict()

with open('day13testinput.txt', 'r') as fin:
    layers = fin.read().rstrip().split('\n')
    for layer in layers:
        tmplist = re.findall(r'\d+', layer)
        firewall[int(tmplist[0])] = [0 for x in range(int(tmplist[1]))]


def change_direcion(layer):




print('finished in ' + str(time() - start) + ' seconds')