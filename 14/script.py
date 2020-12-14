import os
import re


def list_all_addrsses(s, m):
    l = []
 
    if len(s) == 0:
        return ['']

    st = []

    if m[0] == '0':
        st.append(s[0])
 
    if m[0] == '1':
        st.append('1')
  
    if m[0] == 'X':
        st.append('0')
        st.append('1')
    
    ls = list_all_addrsses(s[1:], m[1:])
    for sst in st:
        for lss in ls:
            l.append(sst + lss)

    return l


def apply_mask(value):
    value = format(value, '#038b')[2:]

    new_val = []
    i = 0
    while i < len(mask):
        if mask[i] != 'X':
            new_val.append(mask[i])
        else:
            new_val.append(value[i])
        i += 1

    new_val = ''.join(map(str, new_val))
    return str(new_val)


def handle_mem_op(addr, val):
    val = int(apply_mask(val), 2)
    global memory
    memory[addr] = val


def handle_mem_op_2(addr, val):
    addr = format(addr, '#038b')[2:]
    addresses = list_all_addrsses(addr, mask)
    global memory
    for a in addresses:
        a = int(a, 2)
        memory[a] = val



def dispatch_instruction(instruction):
    if re.match('mask', instruction):
        global mask
        mask = instruction.split("=")[1]
    if re.match('mem', instruction):
        instr = re.findall(r'\d+', instruction)
        address = int(instr[0])
        value = int(instr[1])
        
        if part == 1:
            handle_mem_op(address, value)
        else:
            handle_mem_op_2(address, value)


def solve(part):
    global mask, memory, Lines
    mask = 'X' * 36
    memory = {}
    for line in Lines:
        line = line.replace(" ", "").replace("\n", "")
        dispatch_instruction(line)

    print('part ' + str(part) + ': ' + str(sum(memory.values())))


f = open(os.getcwd() + "/14/input.txt", "r")
Lines = f.readlines()

part = 1
solve(part)

part = 2
solve(part)