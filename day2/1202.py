def exec_opcode(opcode_seq, intcode_seq):
    """Perform addition if opcode is 1.
    Perform multiplication if opcode is 2.
    Add (if opcode 1) or multiply (if opcode 2) the values at positions in the intcode sequence indicated at indices 1 and 2 of the opcode sequence.
The opcode is the integer found at index 0 of the opcode sequence.

    Args:
        intcode_seq:    the entire intode list of 4 digit opcodes
        opcode_seq:     the 4 digit opcode sequence

    This function does not return anything, but directly updates the value at the position indicated by the integer at index 3 of the opcode sequence with the sum or product.
    """

    opcode = opcode_seq[0]
    pos1 = opcode_seq[1]
    pos2 = opcode_seq[2]
    pos3 = opcode_seq[3]

    if opcode == 1:
        intcode_seq[pos3] = intcode_seq[pos1] + intcode_seq[pos2]

    elif opcode == 2:
        intcode_seq[pos3] = intcode_seq[pos1] * intcode_seq[pos2]

    
intcode_str = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,10,23,2,13,23,27,1,5,27,31,2,6,31,35,1,6,35,39,2,39,9,43,1,5,43,47,1,13,47,51,1,10,51,55,2,55,10,59,2,10,59,63,1,9,63,67,2,67,13,71,1,71,6,75,2,6,75,79,1,5,79,83,2,83,9,87,1,6,87,91,2,91,6,95,1,95,6,99,2,99,13,103,1,6,103,107,1,2,107,111,1,111,9,0,99,2,14,0,0'

intcode_seq = [int(n) for n in intcode_str.split(',')]

opcodes = [1, 2, 99]

for i in range(0, len(intcode_seq), 4):
    opcode_seq = intcode_seq[i:i+4]
    opcode = opcode_seq[0]
    if opcode in opcodes:
        if opcode == 99:
            print(f"""Opcode {opcode} at index {str(intcode_seq.index(99))} 
            Program halted.""")
            break
        exec_opcode(opcode_seq, intcode_seq)

print(intcode_seq)
