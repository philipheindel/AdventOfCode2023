import re


input_str = "sevensrncljm5zmvvrtthreejonejdseven85twonepvj"
result = re.findall('(?=(one|two|three|four|five|six|seven|eight|nine))', input_str)
#print("First number spelled out as a word from the end:", result)
print(re.sub(result[0], str(7), input_str, 1))
print(re.sub(result[-1], str(1), input_str))
#print(input_str.replace(result[0], str(1)))
#print(input_str.replace(result[0], str(1)))
#print(input_str.replace(result[-1], str(1)))

