filename = __file__.strip(".py") + ".txt"
file = open(filename, "r")
data = list(map(int, file.readlines()))

def Part1():
    count1 = 0
    for i in range(1, len(data)):
        count1 += 1 if data[i] > data[i - 1] else 0

    return count1

def Part2():
    count2 = 0
    for i in range(3, len(data)):
        count2 += 1 if data[i] > data[i - 3] else 0

    return count2

print(Part1())
print(Part2())
