inputfile = open("input.txt", "r")
array = []


sum = 0

for line in inputfile:
    array.append(list(line.strip()))

def checkSymbol(aboveOrBelow):
    for char in aboveOrBelow:
        if char != "." and not char.isnumeric():
            return True
    return False

def checkNumber(current_number, rowid, colid):
    if len(current_number) > 0:
        number = int("".join(current_number))
        numberstartcolid = colid - len(current_number)
        numberendcolid = colid - 1
        hasSymbol = False
        if numberstartcolid != 0 and (array[rowid][numberstartcolid - 1] != "."):
            hasSymbol = True
        if numberendcolid < len(array[rowid]) - 1 and (array[rowid][numberendcolid + 1] != "."):
            hasSymbol = True
        above = []
        if rowid != 0:
            above = array[rowid - 1][max(0,numberstartcolid-1):min(numberendcolid + 2, len(array[rowid]))]
        below = []
        if rowid != len(array) - 1:
            below = array[rowid + 1][max(0,numberstartcolid-1):min(numberendcolid + 2, len(array[rowid]))]
        if checkSymbol(above) or checkSymbol(below):
            hasSymbol = True
        if hasSymbol:
            return number
    return 0

for rowid in range(len(array)):
    current_number = []
    for colid in range(len(array[rowid])):
        if array[rowid][colid].isnumeric():
            current_number.append(array[rowid][colid])
        else:
            sum += checkNumber(current_number, rowid, colid)
            current_number = []
    sum += checkNumber(current_number, rowid, len(array[rowid]))

print(sum)