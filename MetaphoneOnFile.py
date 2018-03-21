import Metaphone

f = open("FemaleNamesSortedUnique.txt", "r")
f2 = open("FemaleNamesMatchedMetaphone.txt", "w")
line = f.readline()
while line:
    lineMetaphone = Metaphone.metaphone(line)
    f2.write(lineMetaphone + ' ' + line)
    line = f.readline()

f.close()
f2.close()