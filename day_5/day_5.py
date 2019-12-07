f = open("input.txt", "r")
intcode = f.read().split(",")
intcode = list(map(int, intcode))

i = 0
print(intcode)
while(True):
            print("entered the while")


            opcode = intcode[i]
            opcodeString = str(intcode[i])

            A = 0
            B = 0
            C = 0
            D = 0
            E = 0

            try:
                E = opcodeString[-1]
            except:
                IndexError: E = 0
            try:
                D = opcodeString[-2]
            except:
                IndexError: D = 0

            try:
                C = opcodeString[-3]
            except:
                IndexError: C = 0

            try:
                B = opcodeString[-4]
            except:
                IndexError: B = 0

            try:
                A = opcodeString[-5]
            except:
                IndexError: A = 0

            operand_1 = intcode[i + 1]
            operand_2 = intcode[i + 2]
            res = intcode[i + 3]

            A = int(A)
            B = int(B)
            C = int(C)
            D = int(D)
            E = int(E)

            #print("A = " + str(A))
            #print("B = " + str(B))
            #print("C = " + str(C))
            #print("D = " + str(D))
            #print("E = " + str(E))


            if E == 1:
                op1 = intcode[operand_1] if C == 0 else operand_1
                op2 = intcode[operand_2] if B == 0 else operand_2

                intcode[res] = int(op1) + int(op2)
                print("operand_1: " + str(operand_1))
                #print("intcode[operand_1]: " + str(intcode[operand_1]))
                print("operand_2: " + str(operand_2))
                #print("intcode[operand_2]: " + str(intcode[operand_2]))

                print("res add op1: " + str(op1) + " and op2: " + str(op2) + " which equals: "  + str(intcode[res]))
                i+=4


            elif E == 2:
                op1 = intcode[operand_1] if C == 0 else operand_1
                op2 = intcode[operand_2] if B == 0 else operand_2

                intcode[res] = op1 * op2
                print("operand_1: " + str(operand_1))
                #print("intcode[operand_1]: " + str(intcode[operand_1]))
                print("operand_2: " + str(operand_2))
                #print("intcode[operand_2]: " + str(intcode[operand_2]))
                print("res mul: " + str(intcode[res]))
                i+=4

            elif E == 3:
                print("waiting for input")
                intcode[operand_1] = input()
                i+=2

            elif E == 4:
                op1 = intcode[operand_1] if C == 0 else operand_1

                print("the diagnostics code was:  " + str(op1))
                i+=2

            elif E == 5:
                op1 = intcode[operand_1] if C == 0 else operand_1
                op2 = intcode[operand_2] if B == 0 else operand_2

                if int(op1) != 0:
                    i = int(op2)
                else:
                    i += 3

            elif E == 6:
                op1 = intcode[operand_1] if C == 0 else operand_1
                op2 = intcode[operand_2] if B == 0 else operand_2

                if int(op1) == 0:
                    i = int(op2)
                else:
                    i += 3

            elif E == 7:
                op1 = intcode[operand_1] if C == 0 else operand_1
                op2 = intcode[operand_2] if B == 0 else operand_2

                if int(op1) < int(op2):
                    intcode[res] = 1
                else:
                    intcode[res] = 0
                i += 4

            elif E == 8:
                op1 = intcode[operand_1] if C == 0 else operand_1
                op2 = intcode[operand_2] if B == 0 else operand_2

                if int(op1) == int(op2):
                    intcode[res] = 1
                else:
                    intcode[res] = 0
                i += 4

            elif E == 9 and D == 9:
                print("HALT")
                i+=4
                break
