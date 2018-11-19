import re

name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_155696.txt"
handle = open(name)

number = 0
total = 0
for line in handle:
    numbers = re.findall('[0-9]+', line)
    if len(numbers) < 1 : continue
    number = list(map(int, numbers))
    total = sum (number) + total
print (total)


