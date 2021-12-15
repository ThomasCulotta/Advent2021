filename = "Inputs/" + __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.readlines()

from heapq import heappush, heappop

grid = [[int(point) for point in line.strip()] for line in data]

def Part1():
    searching = [(0, 0, 0)]
    visited = set()
    maxX, maxY = len(grid[0]), len(grid)

    while any(searching):
        risk, x, y = heappop(searching)

        if (x, y) == (maxX - 1, maxY - 1):
            print()
            return risk

        if (x, y) in visited:
            continue

        visited.add((x,y))
        print(len(visited), end="\r", flush=True)

        offsets = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        nextTiles = [(nextX,
                      nextY,
                      risk + grid[nextY][nextX]) for offset in offsets if (nextX := x + offset[0]) in range(maxX) and
                                                                          (nextY := y + offset[1]) in range(maxY)]

        for x, y, risk in nextTiles:
            heappush(searching, (risk, x, y))

    return -1

def Part2():
    global grid

    gridEx = [[point+index if point+index <= 9 else point+index-9 for index in range(5) for point in row] for row in grid]
    gridEx = [[point+index if point+index <= 9 else point+index-9 for point in row] for index in range(5) for row in gridEx]

    grid = gridEx
    return Part1()

#print(Part1())
print(Part2())
