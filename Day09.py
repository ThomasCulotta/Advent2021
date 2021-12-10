filename = __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.readlines()

heightMap = [[9] + [int(height) for height in line[:-1]] + [9] for line in data]
heightMap.append([9 for index in range(len(heightMap[0]))])
heightMap.insert(0, [9 for index in range(len(heightMap[0]))])

def Part1():
    riskLevels = [point + 1 for y in range(len(heightMap)) for x in range(len(heightMap[y]))
                  if (point := heightMap[y][x]) < heightMap[y - 1][x] and
                     point < heightMap[y + 1][x] and
                     point < heightMap[y][x - 1] and
                     point < heightMap[y][x + 1]]

    return sum(riskLevels)

def BasinSearch(x,y):
    heightMap[y][x] = 9
    basinSize = 1

    if heightMap[y - 1][x] < 9: basinSize += BasinSearch(x, y - 1)
    if heightMap[y + 1][x] < 9: basinSize += BasinSearch(x, y + 1)
    if heightMap[y][x - 1] < 9: basinSize += BasinSearch(x - 1, y)
    if heightMap[y][x + 1] < 9: basinSize += BasinSearch(x + 1, y)

    return basinSize

def Part2():
    basins = []
    for y in range(len(heightMap)):
        for x in range(len(heightMap[y])):
            if heightMap[y][x] < 9:
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
