import re

inputfile = open('input.txt', 'r')
lines = inputfile.readlines()
total = 0

def get_power(line:str):
    line_sets = line.split(":")[1].split(";")
    min_red = 1
    min_green = 1
    min_blue = 1
    for set in line_sets:
        reds = re.findall('(\d+)(?=\sred)', set)
        greens = re.findall('(\d+)(?=\sgreen)', set)
        blues = re.findall('(\d+)(?=\sblue)', set)
        if len(reds) > 0 and int(reds[0]) > min_red:
            min_red = int(reds[0])
        if len(greens) > 0 and int(greens[0]) > min_green:
            min_green = int(greens[0])
        if len(blues) > 0 and int(blues[0]) > min_blue:
            min_blue = int(blues[0])
    return min_red * min_green * min_blue

for line in lines:
    total += get_power(line.strip())
print(total)
