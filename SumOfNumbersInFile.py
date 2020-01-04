
# Calculating the sum of numbers found in file

import re

file1 = open("Mayakovsky.txt")

sum = int(0)

for line in file1:
    line.rstrip()
    list_of_nums = re.findall('[0-9]+',line)
    for i in range(len(list_of_nums)):
        sum = sum + int(list_of_nums[i])

print(sum)
