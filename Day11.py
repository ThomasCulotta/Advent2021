filename = __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.readlines()

gridBase = [[int(octopus) for octopus in row.strip()] for row in data]

def Flash(grid, x, y):
    flashCount = 1
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    coords = [(x + offset[0], y + offset[1]) for offset in offsets if x + offset[0] in range(10) and
                                                                      y + offset[1] in range(10)]

    for oX, oY in coords:
        grid[oY][oX] += 1
        if grid[oY][oX] == 10:
            flashCount += Flash(grid, oX, oY)

    return flashCount

def Part1():
    grid = gridBase.copy()

    flashCount = 0
    for step in range(100):
        grid = [[octopus + 1 for octopus in row] for row in grid]

        flashCoords = [(x, y) for y in range(10) for x in range(10) if grid[y][x] == 10]
        for x, y in flashCoords:
            flashCount += Flash(grid, x, y)

        grid = [[octopus if octopus < 10 else 0 for octopus in row] for row in grid]

    return flashCount

def Part2():
    grid = gridBase.copy()

    step = 1
    while True:
        flashCount = 0
        grid = [[octopus + 1 for octopus in row] for row in grid]

        flashCoords = [(x, y) for y in range(10) for x in range(10) if grid[y][x] == 10]
        for x, y in flashCoords:
            flashCount += Flash(grid, x, y)

        if flashCount == 100:
            return step

        grid = [[octopus if octopus < 10 else 0 for octopus in row] for row in grid]
        step += 1

    return 0

print(Part1())
print(Part2())
