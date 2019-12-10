"""Restore the gravity assist program, an intcode program, to the 1202 program 
alarm state present just before the last computer burst into flames 
by changing the inputs at positions 1 and 2 with 12 and 2 respectively, 
then performing calculations and input replacements based on the opcodes 
and positions indicated in each 4 unit sequence.

Opcodes are 1, 2, and 99 (99 means halt).

Opcode 1 means add values at positions indicated in the subsequent 2 inputs,
and replace the value at the position indicated by the last input with the sum.

Opcode 2 means perform multiplication rather than addition, and replace 
with the product.

The 1st of every 4-input sequence is a new opcode.
"""

opcode1 = 1
opcode2 = 2
opcode99 = 99

def restore_1202(gravity_assist):
    """Restore the gravity assist program to the 1202 program alarm state.

    Args:
        gravity_assist: a string of intcode digits

    Returns:    a list of 1202 program alarm state intcode digits
    """

    return [int(n) for n in gravity_assist.split(',')]


def process_opcode(opcode_seq, intcode_seq):
    """Add or multiply (for opcodes 1, or 2, respectively - 
    indicated the the integer at index 0) the values at the positions 
    in the sequence indicated by the integers at indices 1 and 2, then 
    update the value at the position indicated by the integer at index 3 
    with the sum or product.

    Args:
        optcode_seq:    a list of four integers, which is a slice of the
        intcode_seq.
        intcode_seq:    a list of intcode integers.
    """

    pos1 = opcode_seq[1]
    pos2 = opcode_seq[2]
    pos3 = opcode_seq[3]
 
    opcode = opcode_seq[0]

    if opcode == 1:
        intcode_seq[pos3] = intcode_seq[pos1] + intcode_seq[pos2]   
    elif opcode == 2:
        intcode_seq[pos3] = intcode_seq[pos1] * intcode_seq[pos2]

    
