f = open("FemaleNamesSortedMatchedSoundex.txt", "r")
f2 = open("FemaleNamesSortedMatchedSoundexCompressed.txt", "w")
line1 = f.readline()
line2 = f.readline()
list1 = line1.split()
list2 = line2.split()
f2.write(list1[1] + ' ')

while line1:
    if len(list1) > 0 and len(list2) > 0 and line1 and list2:
        while len(list1) > 0 and len(list2) > 0 and list1[0] == list2[0]:
            f2.write(list2[1] + ' ')
            line2 = f.readline()
            list2 = line2.split()

        # get a new line, since the list value is no longer the same
        line1 = line2
        list1 = list2
        f2.write('\n')
    else:
        break

