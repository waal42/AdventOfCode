from time import time
from pprint import pprint

start = time()

with open("day08testinput.txt") as fin:
    tree_license = [int(x) for x in fin.read().split(" ")]


'''def read_node(tree_list, tree_dict, parent_number):
    count_children = tree_list[0]
    metadata_length = tree_list[1]
    if count_children > 0:
        for child in range(count_children):
            read_node(tree_list[2:])'''






print("computed in " + str(time() - start) + " seconds")
