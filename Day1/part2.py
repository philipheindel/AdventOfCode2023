import re

def str_to_num(num_string:str):
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

def get_num(line:str, first_last:str):
    index = 0
    updated_line = line
    if first_last.lower() == "l":
        index = -1
    match_strings = re.findall('(?=(one|two|three|four|five|six|seven|eight|nine))', line)
    if len(match_strings) > 0:
        num_str = match_strings[index]
        updated_line = re.sub(num_str, str_to_num(num_str), line)
    if index == -1:
        return str(re.findall('(\d)(?!.*\d)', updated_line)[0])
    else:
        return str(re.findall('(\d)', updated_line)[0])

inputfile = open('input.txt', 'r')
lines = inputfile.readlines()
total = 0

for line in lines:
    first_num = get_num(line.strip(), 'f')
    last_num = get_num(line.strip(), 'l')
    full_num = f"{first_num}{last_num}"
    total += int(full_num)
print(total)
