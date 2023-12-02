import re

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

inputfile = open('input.txt', 'r')
lines = inputfile.readlines()
total = 0

def is_possible(line:str):
    line_sets = line.split(":")[1].split(";")
    for set in line_sets:
        reds = re.findall('(\d+)(?=\sred)', set)
        greens = re.findall('(\d+)(?=\sgreen)', set)
        blues = re.findall('(\d+)(?=\sblue)', set)
        if len(reds) > 0 and int(reds[0]) > RED_MAX:
            return False
        if len(greens) > 0 and int(greens[0]) > GREEN_MAX:
            return False
        if len(blues) > 0 and int(blues[0]) > BLUE_MAX:
            return False
    return True

for line in lines:
    id = re.findall('(?<=Game )\d+(?=:)', line.strip())[0]
    if is_possible(line.strip()):
        total += int(id)
print(total)
