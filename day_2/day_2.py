def run(par1, par2, intcode):
    i = 0
    intcode[1] = par1
    intcode[2] = par2

    while(True):

            if i > (len(intcode) - 3):
                break
            else:


                opcode = intcode[i]
                operand_1 = intcode[i + 1]
                operand_2 = intcode[i + 2]
                res = intcode[i + 3]

                if opcode == 1:
                    intcode[res] = intcode[operand_1] + intcode[operand_2]
                    print("res add: " + str(intcode[res]))

                elif opcode == 2:
                    intcode[res] = intcode[operand_1] * intcode[operand_2]
                    print("res mul: " + str(intcode[res]))

                elif opcode == 99:
                    print("HALT")
                    break

                i+=4


# There are multiple ways of doing this. One way is to force it which should be pretty quick since we only
# have 100 000 possible combinations

for x1 in range(100):
    print(x1)
    for x2 in range(100):
        print(x2)
        f = open("input.txt", "r")
        intcode = f.read().split(",")
        intcode = list(map(int, intcode))

        run(x1, x2, intcode)
        if intcode[0] == 19690720:
            break
        else:
            print(intcode)


    if intcode[0] == 19690720:
        print((100 * x1) + x2)
        break
