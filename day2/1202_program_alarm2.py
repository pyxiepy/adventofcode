program_str = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,10,23,2,13,23,27,1,5,27,31,2,6,31,35,1,6,35,39,2,39,9,43,1,5,43,47,1,13,47,51,1,10,51,55,2,55,10,59,2,10,59,63,1,9,63,67,2,67,13,71,1,71,6,75,2,6,75,79,1,5,79,83,2,83,9,87,1,6,87,91,2,91,6,95,1,95,6,99,2,99,13,103,1,6,103,107,1,2,107,111,1,111,9,0,99,2,14,0,0'

program = [int(n) for n in program_str.split(',')] 

#restore program (intcode data) to 1202 program alarm state
program[1] = 12
program[2] = 2

i = 0

opcode = program[i]
print(opcode)
while opcode != 99:
    opcode_seq = program[i:i+4]
    print(opcode_seq) 
    p1 = opcode_seq[1]
    p2 = opcode_seq[2]
    p3 = opcode_seq[3]

    if opcode == 1:
        program[p3] = program[p1] + program[p2]

    elif opcode == 2:
        program[p3] = program[p1] * program[p2]

    else:
        print('something went wrong')
        break

    i = i+4
    opcode = program[i] 
    print(program)
print(program)
