from time import time
from collections import deque

start = time()
registers = dict()

with open('day18input.txt') as fin:
    tmp = fin.read().split('\n')
    instrs = list()
    for line in tmp:
        instrs.append(line.split(' '))

'''
def execute_instructions(regs, instruction, sent, rcvd, times_sent):
    rule = instruction[0]
    reg = instruction[1]
    wait = False
    offset = 0
    if len(instruction) == 3:
        val = instruction[2]
    if reg not in regs:
        regs[reg] = 0
    if rule == 'snd':
        times_sent += 1
        if reg.isalpha():
            sent.append(regs[reg])
        else:
            sent.append(int(reg))
    elif rule == 'set':
        if val.isalpha():
            regs[reg] = regs[val]
        else:
            regs[reg] = int(val)
    elif rule == 'add':
        if val.isalpha():
            regs[reg] += regs[val]
        else:
            regs[reg] += int(val)
    elif rule == 'mul':
        if val.isalpha():
            regs[reg] *= regs[val]
        else:
            regs[reg] *= int(val)
    elif rule == 'mod':
        if val.isalpha():
            regs[reg] %= regs[val]
        else:
            regs[reg] %= int(val)
    elif rule == 'rcv':
        if rcvd:
            regs[reg] = rcvd.popleft()
        else:
            wait = True
    elif rule == 'jgz':
        if regs[reg] > 0:
            if val.isalpha():
                offset = regs[val]
            else:
                offset = int(val)
    return wait, offset, times_sent


def part_two():
    reg_0 = {'p': 0}
    reg_1 = {'p': 1}
    sent_0 = deque()
    sent_1 = deque()
    index_0 = 0
    index_1 = 0
    waits_0 = False
    waits_1 = False
    deadlock = False
    offset_0 = 0
    offset_1 = 0
    sent_times_0 = 0
    sent_times_1 = 0
    while not deadlock:
        instr_0 = instrs[index_0]
        instr_1 = instrs[index_1]
        waits_0, offset_0, sent_times_0 = execute_instructions(reg_0, instr_0, sent_0, sent_1, sent_times_0)
        waits_1, offset_1, sent_times_1 = execute_instructions(reg_1, instr_1, sent_1, sent_0, sent_times_1)
        # print(reg_0, index_0, sent_0, sent_times_0, waits_0, offset_0)
        # print(reg_1, index_1, sent_1, sent_times_1, waits_1, offset_1)
        if waits_0 and waits_1:
            deadlock = True
        if not waits_0:
            if offset_0:
                index_0 += offset_0
            else:
                index_0 += 1
        if not waits_1:
            if offset_1:
                index_1 += offset_1
            else:
                index_1 += 1
    return sent_times_1


print(part_two())
'''

registers_0={"p":0,"counter":0}
registers_1={"p":1,"counter":0}
queue_for_0=deque()
queue_for_1=deque()

# runs until termination or wait state. Returns False on termination
def run_program(registers,queue_in,queue_out):

    def value(r):
        if r.isalpha():
            return registers.get(r,0)
        else:
            return int(r)

    #first_rcv_done=False
    while (registers["counter"]>=0) and (registers["counter"]<len(commands)):
        parsed=commands[registers["counter"]].strip().split()
        if parsed[0]=="rcv":
            if len(queue_in)==0:
                return True
            registers[parsed[1]]=queue_in.popleft()
        if parsed[0]=="jgz":
            if value(parsed[1])>0:
                registers["counter"]+=value(parsed[2])
                continue
        if parsed[0]=="snd":
            queue_out.append(value(parsed[1]))
            registers["sent"]=value("sent")+1
        if parsed[0]=="set":
            registers[parsed[1]]=value(parsed[2])
        if parsed[0]=="add":
            registers[parsed[1]]=value(parsed[1])+value(parsed[2])
        if parsed[0]=="mul":
            registers[parsed[1]]=value(parsed[1])*value(parsed[2])
        if parsed[0]=="mod":
            registers[parsed[1]]=value(parsed[1])%value(parsed[2])
        registers["counter"]+=1
    return False

commands=open("day18input.txt").readlines()
while True:
    if not run_program(registers_0,queue_for_0,queue_for_1): break
    if not run_program(registers_1,queue_for_1,queue_for_0): break
    if len(queue_for_0)==0 and len(queue_for_1)==0: break

print(registers_1["sent"])

def part_one():
    last_played_sound = 0
    index = 0
    offset = 0
    size = len(instrs)
    while index < size:
        instruction = instrs[index]
        rule = instruction[0]
        rgstr = instruction[1]
        if rgstr not in registers.keys():
            registers[rgstr] = 0
        if rule == 'snd':
            last_played_sound = registers[rgstr]
        elif rule == 'set':
            val = instruction[2]
            if not val.isalpha():
                registers[rgstr] = int(val)
            else:
                registers[rgstr] = registers[val]
        elif rule == 'add':
            val = instruction[2]
            if not val.isalpha():
                registers[rgstr] += int(val)
            else:
                registers[rgstr] += registers[val]
        elif rule == 'mul':
            val = instruction[2]
            if not val.isalpha():
                registers[rgstr] *= int(val)
            else:
                registers[rgstr] *= registers[val]
        elif rule == 'mod':
            val = instruction[2]
            if not val.isalpha():
                registers[rgstr] %= int(val)
            else:
                registers[rgstr] %= registers[val]
        elif rule == 'rcv':
            if registers[rgstr] != 0:
                return last_played_sound
        elif rule == 'jgz':
            if registers[rgstr] > 0:
                offset = int(instruction[2])
        # print(registers, last_played_sound, index, offset)
        if offset != 0:
            index += offset
            offset = 0
        else:
            index += 1


print(part_one())

print('finished in ' + str(time() - start) + ' seconds')