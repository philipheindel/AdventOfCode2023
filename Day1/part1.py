import re

inputfile = open('input.txt', 'r')
lines = inputfile.readlines()
total = 0

for line in lines:
    firstnumber = re.findall('(\d)', line.strip())[0]
    lastnumber = re.findall('(\d)(?!.*\d)', line.strip())[0]
    fullnumber = "{}{}".format(firstnumber, lastnumber)
    total += int(fullnumber)
    print("{} : {}".format(line.strip(), fullnumber))

print(total)
