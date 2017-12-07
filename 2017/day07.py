from time import time
from pprint import pprint

start = time()

with open('day07input.txt', 'r') as fin:
    data_input = fin.read().rstrip().split('\n')
# importovat spis regularne do dictionary; klic = prvek, parametry hmotnost a list prvku, ktere nese

runtime = time() - start

print('finished in ' + str(runtime) + ' seconds')