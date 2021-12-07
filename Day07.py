filename = __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.read()

startPos = [int(pos) for pos in data.split(",")]
minPos = min(startPos)
maxPos = max(startPos)

def Part1():
    costs = [sum([abs(pos - target) for pos in startPos]) for target in range(minPos, maxPos + 1)]

    return min(costs)

def Part2():
    costs = [sum([int(abs(pos - target) * (abs(pos - target) + 1) / 2) for pos in startPos]) for target in range(minPos, maxPos + 1)]

    return min(costs)

print(Part1())
print(Part2())
