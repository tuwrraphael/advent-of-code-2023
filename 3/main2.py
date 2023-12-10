inputfile = open("input.txt", "r")
array = []

stars = []


sum = 0

for line in inputfile:
    array.append(list(line.strip()))
    rowstars = []
    stars.append(rowstars)
    for i in range(len(line.strip())):
        rowstars.append([])

def checkSymbol(aboveOrBelow):
    for char in aboveOrBelow:
        if char != "." and not char.isnumeric():
            return True
    return False

def checkNumber(current_number, rowid, colid):
    global stars
    if len(current_number) > 0:
        number = int("".join(current_number))
        numberstartcolid = colid - len(current_number)
        numberendcolid = colid - 1
        if numberstartcolid != 0 and (array[rowid][numberstartcolid - 1] == "*"):
            stars[rowid][numberstartcolid - 1].append(number)
        if numberendcolid < len(array[rowid]) - 1 and (array[rowid][numberendcolid + 1] == "*"):
            stars[rowid][numberendcolid + 1].append(number)
        if rowid != 0:
            for starcolid in range(max(0,numberstartcolid-1), min(numberendcolid + 2, len(array[rowid]))):
                if array[rowid - 1][starcolid] == "*":
                    stars[rowid - 1][starcolid].append(number)
        if rowid != len(array) - 1:
            for starcolid in range(max(0,numberstartcolid-1), min(numberendcolid + 2, len(array[rowid]))):
                if array[rowid + 1][starcolid] == "*":
                    stars[rowid + 1][starcolid].append(number)

for rowid in range(len(array)):
    current_number = []
    for colid in range(len(array[rowid])):
        if array[rowid][colid].isnumeric():
            current_number.append(array[rowid][colid])
        else:
            checkNumber(current_number, rowid, colid)
            current_number = []
    checkNumber(current_number, rowid, len(array[rowid]))

for rows in stars:
    for cols in rows:
        if len(cols) == 2:
            sum += cols[0] * cols[1]
print(sum)