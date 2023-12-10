inputfile = open("input.txt", "r")
sum = 0
max_green = 13
max_red = 12
max_blue = 14
for line in inputfile:
    gameid = int(line.split(":")[0].replace("Game ", ""))
    impossible = False
    rounds = line.split(":")[1].split(";")
    for round in rounds:
       cubes = round.split(",")
       red = 0
       green = 0
       blue = 0
       for cube in cubes:
           cube = cube.strip()
           color = cube.split(" ")[1]
           num = int(cube.split(" ")[0])
           if (color == "red"):
               if (num > max_red):
                   impossible = True
           elif (color == "green"):
               if (num > max_green):
                   impossible = True
           elif (color == "blue"):
               if (num > max_blue):
                   impossible = True
    if not impossible:
        sum += gameid
print(sum)

inputfile = open("input.txt", "r")
sum = 0
for line in inputfile:
    gameid = int(line.split(":")[0].replace("Game ", ""))
    impossible = False
    rounds = line.split(":")[1].split(";")
    min_red = 0
    min_blue = 0
    min_green = 0
    for round in rounds:
       cubes = round.split(",")
       red = 0
       green = 0
       blue = 0
       for cube in cubes:
           cube = cube.strip()
           color = cube.split(" ")[1]
           num = int(cube.split(" ")[0])
           if (color == "red"):
               if (num > min_red):
                   min_red = num
           elif (color == "green"):
               if (num > min_green):
                   min_green = num
           elif (color == "blue"):
                if (num > min_blue):
                   min_blue = num
    power = min_red * min_green * min_blue
    sum += power
print(sum)