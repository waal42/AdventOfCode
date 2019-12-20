from time import time

start = time()

with open("day08input.txt", "r") as file_in:
    pixels = list(file_in.read().rstrip('\n'))
    


print("computed in " + str(time() - start) + " seconds")
