f = open("metaphoneClasses.txt", "r")
f2 = open("analysisMetaphone.txt", "w")
line1 = f.readline()
count = 0

while line1:
    list1 = line1.split()
    count += 1
    length = len(list1)
    f2.write(str(length) + " " + line1)
    line1 = f.readline()

print("Lines in File: " + str(count))
f.close()
f2.close()
