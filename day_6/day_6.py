f = open("input.txt", "r")
map = f.read().split()

#print(map)


#Since a body can only directly orbit one other body,
#we can set ut all the pairs in a tree, and then traverse
# all of the nodes. Finally adding up all the values

orbits = []

finalTree = []

for orbit in map:
    #P is for primary, S is for secondary.
    pBody = orbit[0:3]
    sBody = orbit[4:7]
    orbits.append([pBody, sBody])

total = [0]

def assembleOrbits(body, i, total):
    orbitees = []
    #print(body)
    for orbit in orbits:
        if orbit[0] == body:
            total[0] += i
            # print(i)
            orbitees.append(body)
            orbitees.append(assembleOrbits(orbit[1], i + 1, total))
    if orbitees == []:
        orbitees.append(body)
        orbitees.append([])
    return orbitees

finalTree = assembleOrbits("COM", 1, total)


# To find the two points we want to record every step we take after one has been found.
# It does not matter in which way we are stepping


def traverseTree(tree, i):
    print(tree, len(tree),len(tree[1]))
    if len(tree[1]) != 0:
        tree.pop(0)
        print(tree)
        for subTree in tree:
            traverseTree(subTree, i)


traverseTree(finalTree, 0)
#print(total[0])
