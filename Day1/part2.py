import re

def num_to_str(num_string:str):
    conversion = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    return str(conversion.get(num_string))

def substitute_string(line:str):
    print(line)
    match_strings = re.findall('(?=(one|two|three|four|five|six|seven|eight|nine))', line)
    if len(match_strings) > 0:
        first_numstr = match_strings[0]
        last_numstr = match_strings[-1]
        line = re.sub(first_numstr, num_to_str(first_numstr), line, 1)
        line = re.sub(last_numstr, num_to_str(last_numstr), line)
        print(f"\t{line}")
    return line

inputfile = open('input.txt', 'r')
lines = inputfile.readlines()
total = 0

for line in lines:
    converted_line = substitute_string(line.strip())
    firstnumber = re.findall('(\d)', converted_line)[0]
    lastnumber = re.findall('(\d)(?!.*\d)', converted_line)[0]
    fullnumber = "{}{}".format(firstnumber, lastnumber)
    print(f"{total} + {fullnumber} = {total + int(fullnumber)}")
    total += int(fullnumber)
    

print(total)
