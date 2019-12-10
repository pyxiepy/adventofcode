grav_assist_str = '1,1,1,4,99,5,6,0,99'

grav_assist = [int(n) for n in grav_assist_str.split(',')]

print(f'Starting program: {grav_assist}')

for i in range(0, len(grav_assist), 4):
    opcode = grav_assist[i:i+4]
    pos1 = opcode[1]
    pos2 = opcode[2]
    pos3 = opcode[3]

    if opcode[0] == 1:
        result = grav_assist[pos1] + grav_assist[pos2]

    elif opcode[0] == 2:
        result = grav_assist[pos1] * grav_assist[pos2]

    elif opcode[0] == 99:
        print("Prgram halted.")
        break

    else:
        print("Something went wrong.")
        raise ValueError("Something went wrong - invalid opcode.")

    grav_assist[pos3] = result

print(f'Ending program: {grav_assist}')

print(grav_assist[0])

