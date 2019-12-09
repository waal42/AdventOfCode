

def load_intcode(file_input):
    with open(file_input, 'r') as fin:
        intcode = [int(x) for x in fin.read().rstrip().split(",")]
    return intcode

def run_intcode(intcode, noun = None, verb = None):
    index = 0
    if noun and verb:
        intcode[1] = noun
        intcode[2] = verb
    while (index <= len(intcode)):
        if intcode[index] == 1:
            intcode[intcode[index + 3]] = intcode[intcode[index + 1]] + intcode[intcode[index + 2]]
            index += 4
        elif intcode[index] == 2:
            intcode[intcode[index + 3]] = intcode[intcode[index + 1]] * intcode[intcode[index + 2]]
            index += 4
        elif intcode[index] == 99:
            break
        else:
            print("error")
            break
    return intcode[0]

#print(run_intcode(load_intcode("day02input.txt"), 12, 2))
