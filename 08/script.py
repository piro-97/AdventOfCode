import os

f = open(os.getcwd() + "/8/input.txt", "r")
Lines = f.readlines()

class ComputationState:
    def __init__(self):
        self.instruction_pointer = 0
        self.accumulator = 0
        self.loop_found = False
        self.computation_terminates = False
        self.mask = []

def execute_instruction(comp_state, instructions):
    # computation is over
    if comp_state.instruction_pointer >= len(instructions):
        comp_state.computation_terminates = True
        return

    # loop found
    if comp_state.instruction_pointer in comp_state.mask:
        comp_state.loop_found = True
        return

    # execute instruction
    current_instruction = instructions[comp_state.instruction_pointer].replace("\n", "").split(" ")
    opcode = current_instruction[0]
    value = int(current_instruction[1])

    comp_state.mask.append(comp_state.instruction_pointer)

    if opcode == "acc":
        comp_state.accumulator += value
        comp_state.instruction_pointer += 1

    elif opcode == "jmp":
        comp_state.instruction_pointer += value

    elif opcode == "nop":
        comp_state.instruction_pointer += 1

def modify_instr(list, index):
    modified = False
    I = list[index].split(" ")
    op = I[0]
    val = I[1]
    
    if op == "jmp":
        op = "nop"
        modified = True
    elif op == "nop":
        op = "jmp"
        modified = True

    if modified:
        list[index] = op + " " + val

    return modified

# part 1

comp = ComputationState()
while not comp.loop_found and not comp.computation_terminates:    # we try to modify one instruction of the code
    execute_instruction(comp, Lines)

print("part 1: " + str(comp.accumulator))


# part 2

go_on = True
instructions = Lines.copy()

# we brutally try to modify each instruction of the code
i = 0
while i < len(instructions) and go_on:

    if modify_instr(instructions, i):  # modified instruction was "nop" or "jmp"
        computation = ComputationState()   
        while not computation.loop_found and not computation.computation_terminates:
            execute_instruction(computation, instructions)

        if computation.computation_terminates:
            go_on = False
            
    instructions = Lines.copy()
    i += 1

print("part 2: " + str(computation.accumulator))