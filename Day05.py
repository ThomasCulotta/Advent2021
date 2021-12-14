filename = "Inputs/" + __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.readlines()

coords = [[(int((coord := coordPair.split(","))[0]), int(coord[1])) for coordPair in line.split(" -> ")] for line in data]
board = [[0 for xCoord in range(max([coord[0] for coordPair in coords for coord in coordPair]) + 1)] for yCoord in range(max([coord[1] for coordPair in coords for coord in coordPair]) + 1)]

def Part1():
    orth = [coordPair for coordPair in coords if coordPair[0][0] == coordPair[1][0] or coordPair[0][1] == coordPair[1][1]]

    for coord1, coord2 in orth:
        xDir = int((coord2[0] - coord1[0]) / abs(coord2[0] - coord1[0])) if coord2[0] - coord1[0] != 0 else 0
        yDir = int((coord2[1] - coord1[1]) / abs(coord2[1] - coord1[1])) if coord2[1] - coord1[1] != 0 else 0

        for index in range(abs(coord2[0] - coord1[0]) + abs(coord2[1] - coord1[1]) + 1):
            board[coord1[1] + index * yDir][coord1[0] + index * xDir] += 1

    return len(list(filter(lambda vent: vent >= 2, [vent for row in board for vent in row])))

def Part2():
    diag = [coordPair for coordPair in coords if coordPair[0][0] != coordPair[1][0] and coordPair[0][1] != coordPair[1][1]]

    for coord1, coord2 in diag:
        xDir = 1 if coord2[0] - coord1[0] > 0 else -1
        yDir = 1 if coord2[1] - coord1[1] > 0 else -1

        for index in range(abs(coord2[0] - coord1[0]) + 1):
            board[coord1[1] + index * yDir][coord1[0] + index * xDir] += 1

    return len(list(filter(lambda vent: vent >= 2, [vent for row in board for vent in row])))

print(Part1())
print(Part2())
