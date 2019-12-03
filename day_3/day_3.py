f_1 = open("wire_1.txt", "r")
list_1 = f_1.read().split(",")

f_2 = open("wire_2.txt", "r")
list_2 = f_2.read().split(",")

''' Make a list of the coordinates of the wires. Check if any of them match


    1. Read all the lines and make a list with pairs for all the discrete coordinates of the wires

    2. Check if there is any overlap between the two lists

    3. Make a list of the overlaps and calculate their distance. Smallest distance winns.

'''
print(list_1)

def make_coordinates(x, y, distance, list, dir):
    if dir == "R":
        for n in range(distance):

            x += 1
            list.append((x, y))


    elif dir == "L":
        for n in range(distance):

            x += -1
            list.append((x, y))


    elif dir == "U":
        for n in range(distance):

            y += 1
            list.append((x, y))


    elif dir == "D":
        for n in range(distance):

            y += -1
            list.append((x, y))

    return (x, y, list)


wire_1 = []
wire_2 = []

i = 0

x = 0
y = 0

while(i < len(list_1)):

    dir = list_1[i][0]
    length = len(list_1[i])
    dist = int(list_1[i][1:length])


    #Find all  the coordinates
    result = make_coordinates(x, y, dist, wire_1, dir)
    x = result[0]
    y = result[1]
    wire_1 = result[2]




    i += 1

print("wire_1 done")

j = 0

x = 0
y = 0

while(j < len(list_2)):

    dir = list_2[j][0]
    length = len(list_2[j])
    dist = int(list_2[j][1:length])


    #Find all  the coordinates
    result = make_coordinates(x, y, dist, wire_2, dir)
    x = result[0]
    y = result[1]
    wire_2 = result[2]




    j += 1
print("wire_2 done")

#Find the overlap

intersections = list(set(wire_1).intersection(wire_2))

print(len(wire_1))
print(len(wire_2))
print(intersections)

shortest = abs(intersections[0][0]) + abs(intersections[0][1])

for intersection in intersections:
    if abs(intersection[0]) + abs(intersection[1]) < shortest:
        shortest = abs(intersection[0]) + abs(intersection[1])

print(shortest)


#Del 2 
# Since we know the intersections we can map each intersection to a number of steps for both wires.
# Then we can find the smallest sum and send that answer.

# 1. Find the steps it takes to get to the intersections

steps_1 = {}
h = 1

for entry in wire_1:
    if entry in intersections and not entry in steps_1:
        steps_1.update({entry: h})
    h += 1

h = 1
steps_2 = {}
for entry in wire_2:
    if entry in intersections and not entry in steps_2:
        steps_2.update({entry: h})
    h += 1


print(steps_1)
print(" ")
print(steps_2)
print(" ")

smallestSum = steps_1.get(intersections[0]) + steps_2.get(intersections[0])
print(smallestSum)

for entry in intersections:
    if steps_1.get(entry) + steps_2.get(entry) < smallestSum:
        smallestSum = steps_1.get(entry) + steps_2.get(entry)

print(smallestSum)
