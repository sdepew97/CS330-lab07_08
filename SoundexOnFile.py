import Soundex

f = open("FemaleNamesSortedUnique.txt", "r")
f2 = open("FemaleNamesMatchedSoundex.txt", "w")
line = f.readline()
while line:
    lineSoundex = Soundex.soundexNaive(line.upper(), len(line))
    f2.write(lineSoundex + ' ' + line)
    line = f.readline()

f.close()
f2.close()