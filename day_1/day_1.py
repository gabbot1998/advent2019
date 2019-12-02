f = open("input.txt", "r")
input = f.read().split("\n")
del input[-1] #The last \n got added. Ugly but works
input = list(map(int, input))

total = 0

for mass in input:
    print(mass)
    temp = int(mass / 3) - 2
    total += temp

    while(temp > 0):
        temp = int(temp / 3) - 2
        if temp > 0:
            total += temp

print(total)
