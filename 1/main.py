# read input.txt
inputfile = open("input.txt", "r")
sum = 0
for line in inputfile:
    firstdigit = None
    lastdigit = None
    for char in list(line):
        if char.isnumeric():
            if (firstdigit == None):
                firstdigit = char
            lastdigit = char
    number = firstdigit + lastdigit
    sum += int(number)
print(sum)

sum = 0
numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
inputfile = open("input.txt", "r")
for line in inputfile:
    firstdigit = None
    lastdigit = None
    for i in range(len(line)):
        digit = None
        for j in range(len(numbers)):
            if line[i:].startswith(numbers[j]):
                digit = str(j)
                break
        char = line[i]
        if digit != None:
            if (firstdigit == None):
                firstdigit = digit
            lastdigit = digit
        elif char.isnumeric():
            if (firstdigit == None):
                firstdigit = char
            lastdigit = char
    number = firstdigit + lastdigit
    sum += int(number)
print(sum)