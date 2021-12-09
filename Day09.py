filename = __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.readlines()

heightMap = [[int(height) for height in line[:-1]] for line in data]
heightMapEx = heightMap.copy()
heightMapEx.append([9 for index in range(len(heightMap[0]))])
heightMapEx.insert(0, [9 for index in range(len(heightMap[0]))])

for index in range(len(heightMapEx)):
    heightMapEx[index].insert(0, 9)
    heightMapEx[index].append(9)

def Part1():
    riskLevels = [point + 1 for y in range(len(heightMapEx)) for x in range(len(heightMapEx[y]))
                  if (point := heightMapEx[y][x]) < heightMapEx[y - 1][x] and
                     point < heightMapEx[y + 1][x] and
                     point < heightMapEx[y][x - 1] and
                     point < heightMapEx[y][x + 1]]

    return sum(riskLevels)

def BasinSearch(x,y):
    heightMapEx[y][x] = 9
    basinSize = 1

    if heightMapEx[y - 1][x] < 9: basinSize += BasinSearch(x, y - 1)
    if heightMapEx[y + 1][x] < 9: basinSize += BasinSearch(x, y + 1)
    if heightMapEx[y][x - 1] < 9: basinSize += BasinSearch(x - 1, y)
    if heightMapEx[y][x + 1] < 9: basinSize += BasinSearch(x + 1, y)

    return basinSize

def Part2():
    basins = []
    for y in range(len(heightMapEx)):
        for x in range(len(heightMapEx[y])):
            if heightMapEx[y][x] < 9:
                basins.append(BasinSearch(x, y))

    max1 = max(basins)
    basins.remove(max1)
    max2 = max(basins)
    basins.remove(max2)
    max3 = max(basins)
    basins.remove(max3)

    return max1 * max2 * max3

print(Part1())
print(Part2())
