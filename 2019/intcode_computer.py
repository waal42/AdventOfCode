class IntcodeComputer:

    def __init__(self, intcode, noun = None, verb = None, intcode_input = None):
        self.intcode = intcode
        self.noun = noun
        self.verb = verb
        self.intcode_input = intcode_input
        self.index = 0

    def execute_optcode(self, intcode, index):
        pass


def load_intcode(file_input):
    with open(file_input, 'r') as fin:
        intcode = [int(x) for x in fin.read().rstrip().split(",")]
    return intcode

def run_intcode(intcode, noun = None, verb = None, intcode_in = None):
    index = 0
    intcode_out = list()
    if noun and verb:
        intcode[1] = noun
        intcode[2] = verb
    while (index <= len(intcode)):
        opcode = ''.join(['0' for x in range(5 - len(str(intcode[index])))]) + str(intcode[index])
        # print(opcode)
        ### ADDITION
        if opcode[-2:] == '01':
            if opcode[2] == '0':
                c = intcode[intcode[index + 1]]
            elif opcode[2] == '1':
                c = intcode[index + 1]
            if opcode[1] == '0':
                b = intcode[intcode[index + 2]]
            elif opcode[1] == '1':
                b = intcode[index + 2]
            if opcode[0] == '0':
                intcode[intcode[index + 3]] = b + c
            elif opcode[0] == '1':
                intcode[index + 3] = b + c
            index += 4
        ### MULTIPLICATION
        elif opcode[-2:] == '02':
            if opcode[2] == '0':
                c = intcode[intcode[index + 1]]
            elif opcode[2] == '1':
                c = intcode[index + 1]
            if opcode[1] == '0':
                b = intcode[intcode[index + 2]]
            elif opcode[1] == '1':
                b = intcode[index + 2]
            if opcode[0] == '0':
                intcode[intcode[index + 3]] = b * c
            elif opcode[0] == '1':
                intcode[index + 3] = b * c
            index += 4
        ### WRITE INPUT
        elif opcode[-2:] == '03':
            if isinstance(intcode_in, list):
                this_input = intcode_in[0]
                if len(intcode_in) == 2:
                    intcode_in = intcode_in[1]
                else:
                    intcode_in = intcode_in[1:]
            else:
                this_input = intcode_in
            if opcode[2] == '0':
                intcode[intcode[index + 1]] = this_input
            elif opcode[2] == '1':
                intcode[index + 1] = this_input
            index += 2
        ### READ OUTPUT
        elif opcode[-2:] == '04':
            if opcode[2] == '0':
                intcode_out.append(intcode[intcode[index + 1]])
            elif opcode[2] == '1':
                intcode_out.append(intcode[index + 1])
            index += 2
        ### JUMP IF TRUE
        elif opcode[-2:] == '05':
            if opcode[2] == '0':
                c = intcode[intcode[index + 1]]
            elif opcode[2] == '1':
                c = intcode[index + 1]
            if c:
                if opcode[1] == '0':
                    index = intcode[intcode[index + 2]]
                elif opcode[1] == '1':
                    index = intcode[index + 2]
            else:
                index += 3
        ### JUMP IF FALSE
        elif opcode[-2:] == '06':
            if opcode[2] == '0':
                c = intcode[intcode[index + 1]]
            elif opcode[2] == '1':
                c = intcode[index + 1]
            if not  c:
                if opcode[1] == '0':
                    index = intcode[intcode[index + 2]]
                elif opcode[1] == '1':
                    index = intcode[index + 2]
            else:
                index += 3
        ### LESS THAN
        elif opcode[-2:] == '07':
            if opcode[2] == '0':
                c = intcode[intcode[index + 1]]
            elif opcode[2] == '1':
                c = intcode[index + 1]
            if opcode[1] == '0':
                b = intcode[intcode[index + 2]]
            elif opcode[1] == '1':
                b = intcode[index + 2]
            a = 1 if c < b else 0
            if opcode[0] == '0':
                intcode[intcode[index + 3]] = a
            elif opcode[0] == '1':
                intcode[index + 3] = a
            index += 4
        ### EQUALS
        elif opcode[-2:] == '08':
            if opcode[2] == '0':
                c = intcode[intcode[index + 1]]
            elif opcode[2] == '1':
                c = intcode[index + 1]
            if opcode[1] == '0':
                b = intcode[intcode[index + 2]]
            elif opcode[1] == '1':
                b = intcode[index + 2]
            a = 1 if c == b else 0
            if opcode[0] == '0':
                intcode[intcode[index + 3]] = a
            elif opcode[0] == '1':
                intcode[index + 3] = a
            index += 4
        ### HALT CODE
        elif opcode[-2:] == '99':
            break
        else:
            print("error")
            break
    if intcode_out:
        return intcode_out[0]
    else:
        return intcode[0]

#print(run_intcode(load_intcode("day02input.txt"), 12, 2))

# print(run_intcode([1002,4,3,4,33], intcode_in=42))

#print(run_intcode([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], intcode_in=8))

# print(run_intcode([3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0], intcode_in=1))