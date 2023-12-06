import io
import re

input_file:io.TextIOWrapper = open('input.txt', 'r')
lines:list[str] = input_file.readlines()
total:int = 0

for index, line in enumerate(lines):
    print(line.strip())
    numbers:list[str] = re.finditer('\d+', line.strip())
    
    past_line:str = ''
    next_line:str = ''
    if index - 1 > -1:
        past_line = lines[index - 1].strip()
    if index + 1 < len(lines):
        next_line = lines[index + 1].strip()
    
    for num in numbers:
        past_line_text:str = ''
        next_line_text:str = ''
        start:int = num.start()
        end:int = num.end()
        length:int = end - start

        if start > 0:
            start -= 1
        if end < 139:
            end += 1
        if past_line != '':
            past_line_text = past_line[start:end]
        if next_line != '':
            next_line_text = next_line[start:end]
        print(past_line_text)
        print(line[start:end], end='')
        
        if (not line[start].isnumeric() and line[start] != '.') or (not line[end].isnumeric() and line[end] != '.') or re.search('[^.\d]', past_line_text) or re.search('[^.\d]', next_line_text):
            total += int(num.group())
            print(' ' + str(total) + ' <- is schematic')
        else:
            print(' ' + str(total))
        print(next_line_text)
        #if past_line != '':
        #    past_line_text = past_line[start:end]
        #if next_line != '':
        #    next_line_text = next_line[start:end]
        ##print(past_line)
        #print(past_line_text)
        ##print(next_line)
        #print(next_line_text)
        #if re.search('[^.\d]', past_line_text) or re.search('[^.\d]', next_line_text):
        #    total += int()


        #print(int(num.group()))

print(total)

