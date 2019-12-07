'''
    The password is a six digit number,

    two adjacent digits are the same,

    going from left to right they increase
'''
fuck = []
i = 0
for number in range(307237,769058):

    ok = True
    word = str(number)

    lastNbr = -1
    for char in word:
        if int(char) < lastNbr:
            ok = False
        lastNbr = int(char)

    letters = {}
    for char in word:
        letters.update({char: letters.get(char, 0) + 1})

   #Check for letters with more then two pairs. If there is a bigger pair

    if max(letters.values()) < 2:
        ok = False


    if ok:
        i += 1
        fuck.append(letters)
print(i)
print(fuck)

j = 0

for entry in fuck:
    well = False
    for char in entry.values():
        if char == 2:
            print(char)
            print(entry)
            print(j)
            well = True

    if well:
        j += 1
print(len(fuck))
print(j)
