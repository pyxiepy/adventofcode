"""An intcode computer process 4 digit instructions consisting of an opcode
at address 0 and paramaters at addresses 1-3. 

In this program, the value placed in address 1 is called the noun, and the 
value placed in address 2 is called the verb. Each of the two input values 
will be between 0 and 99, inclusive.

This program finds the values for noun and verb  that produce the output 
19690720."""

def get_zeroth_val(input_tup):
    """Execute all instructions in the program using all possible variables in
    sequence from lowest to highest until desired output is achieved.

    Args:
        input_tup:  values for noun (address 1) and verb (address 2) 
    """
    
    prog_str = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,10,23,2,13,23,27,1,5,27,31,2,6,31,35,1,6,35,39,2,39,9,43,1,5,43,47,1,13,47,51,1,10,51,55,2,55,10,59,2,10,59,63,1,9,63,67,2,67,13,71,1,71,6,75,2,6,75,79,1,5,79,83,2,83,9,87,1,6,87,91,2,91,6,95,1,95,6,99,2,99,13,103,1,6,103,107,1,2,107,111,1,111,9,0,99,2,14,0,0'

    prog = [int(n) for n in prog_str.split(',')] 
    intcode = prog[:]
    intcode[1], intcode[2] = input_tup
    i = 0
    opcode = intcode[i]
    print(opcode)
    while opcode != 99:
        opcode_seq = intcode[i:i+4]
        print(opcode_seq) 
        p1 = opcode_seq[1]
        p2 = opcode_seq[2]
        p3 = opcode_seq[3]

        if opcode == 1:
            intcode[p3] = intcode[p1] + intcode[p2]

        elif opcode == 2:
            intcode[p3] = intcode[p1] * intcode[p2]

        i = i+4
        opcode = intcode[i] 

    return intcode[0]


def get_nounverb(desired_out, poss_inputs, outputs):
    """Iterates over a map object of outputs in conjunction with possible
    inputs to determine which inputs result in the desired output.

    Args:
        desired_out:    the output desired for the zeroth address of an intcode
                        program.

        poss_inputs:    a list of tuples of input combinations for addresses 
                        1 and 2.

        outputs:        the map object of all possible results for the zeroth
                        address.

    Returns:            the tuple of inputs which produce the desired output,
                        if found, -1 otherwise.
    """ 
    i = 0
    for o in outputs:
        if o == desired_out:   
            return poss_inputs[i]
        i += 1
    return -1


prog_str = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,10,23,2,13,23,27,1,5,27,31,2,6,31,35,1,6,35,39,2,39,9,43,1,5,43,47,1,13,47,51,1,10,51,55,2,55,10,59,2,10,59,63,1,9,63,67,2,67,13,71,1,71,6,75,2,6,75,79,1,5,79,83,2,83,9,87,1,6,87,91,2,91,6,95,1,95,6,99,2,99,13,103,1,6,103,107,1,2,107,111,1,111,9,0,99,2,14,0,0'

program = [int(n) for n in prog_str.split(',')]

nouns = [n for n in range(0, len(program)-1)]

nouns_verbs = {noun:[verb for verb in range(0, len(program)-1)] for noun in nouns}

nounverb_tups = []

for noun, verbs in nouns_verbs.items():
    for verb in verbs:
        nounverb_tups.append((noun, verb))

desired_output = 19690720

results = map(get_zeroth_val, nounverb_tups)

#this will be an int of -1 if no successful noun-verb pair is found.
nounverb_tup = get_nounverb(desired_output, nounverb_tups, results)

print(nounverb_tup)
