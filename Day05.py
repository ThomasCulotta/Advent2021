filename = __file__.strip("py") + "txt"
file = open(filename, "r")
data = file.readlines()

coords = [[(int((z := y.split(","))[0]), int(z[1])) for y in x.split(" -> ")] for x in data]
board = [[0 for x in range(max([i[0] for j in coords for i in j]) + 1)] for y in range(max([i[1] for j in coords for i in j]) + 1)]

def Part1():
    orth = [x for x in coords if x[0][0] == x[1][0] or x[0][1] == x[1][1]]

    for coord1, coord2 in orth:
        xDir = int((coord2[0] - coord1[0]) / abs(coord2[0] - coord1[0])) if coord2[0] - coord1[0] != 0 else 0
        yDir = int((coord2[1] - coord1[1]) / abs(coord2[1] - coord1[1])) if coord2[1] - coord1[1] != 0 else 0

        for i in range(abs(coord2[0] - coord1[0]) + abs(coord2[1] - coord1[1]) + 1):
            board[coord1[1] + i * yDir][coord1[0] + i * xDir] += 1

    return len(list(filter(lambda x: x >= 2, [x for y in board for x in y])))

def Part2():
    diag = [x for x in coords if x[0][0] != x[1][0] and x[0][1] != x[1][1]]

    for coord1, coord2 in diag:
        xDir = 1 if coord2[0] - coord1[0] > 0 else -1
        yDir = 1 if coord2[1] - coord1[1] > 0 else -1

        for i in range(abs(coord2[0] - coord1[0]) + 1):
            board[coord1[1] + i * yDir][coord1[0] + i * xDir] += 1

    return len(list(filter(lambda x: x >= 2, [x for y in board for x in y])))

print(Part1())
print(Part2())
