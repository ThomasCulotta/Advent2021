filename = __file__.strip(".py") + ".txt"
with open(filename, "r") as file:
    data = list(map(int, file.readlines()))

def Part1():
    count = 0
    for index in range(1, len(data)):
        count += 1 if data[index] > data[index - 1] else 0

    return count

def Part2():
    count = 0
    for index in range(3, len(data)):
        count += 1 if data[index] > data[index - 3] else 0

    return count

print(Part1())
print(Part2())
