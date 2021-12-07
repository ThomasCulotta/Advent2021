filename = __file__.strip(".py") + ".txt"
with open(filename, "r") as file:
    data = [((pair := instruction.split(" "))[0][0], int(pair[1])) for instruction in file.readlines()]

def Part1():
    forward = sum([instruction[1] for instruction in data if instruction[0] == "f"])
    down    = sum([instruction[1] for instruction in data if instruction[0] == "d"])
    up      = sum([instruction[1] for instruction in data if instruction[0] == "u"])

    return forward * (down - up)

def Part2():
    forward = sum([instruction[1] for instruction in data if instruction[0] == "f"])
    aim = depth = 0

    for direction, distance in data:
        if direction == "f":
            depth += distance * aim
        elif direction == "d":
            aim += distance
        else:
            aim -= distance

    return forward * depth

print(Part1())
print(Part2())
