filename = __file__.strip(".py") + ".txt"
file = open(filename, "r")
data = [((y := x.split(" "))[0][0], int(y[1])) for x in file.readlines()]

def Part1():
    forward = sum([x[1] for x in data if x[0] == "f"])
    down    = sum([x[1] for x in data if x[0] == "d"])
    up      = sum([x[1] for x in data if x[0] == "u"])

    return forward * (down - up)

def Part2():
    forward = sum([x[1] for x in data if x[0] == "f"])
    aim = depth = 0

    for x, y in data:
        if x == "f":
            depth += y * aim
        elif x == "d":
            aim += y
        else:
            aim -= y

    return forward * depth

print(Part1())
print(Part2())
