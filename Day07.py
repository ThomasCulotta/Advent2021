filename = __file__.strip("py") + "txt"
file = open(filename, "r")
data = file.readlines()

startPos = [int(pos) for pos in data[0].split(",")]

def Part1():
    minPos = min(startPos)
    maxPos = max(startPos)

    costs = [sum([abs(pos - target) for pos in startPos]) for target in range(minPos, maxPos + 1)]

    return min(costs)

def Part2():
    minPos = min(startPos)
    maxPos = max(startPos)

    costs = [sum([int(abs(pos - target) * (abs(pos - target) + 1) / 2) for pos in startPos]) for target in range(minPos, maxPos + 1)]

    return min(costs)

print(Part1())
print(Part2())
