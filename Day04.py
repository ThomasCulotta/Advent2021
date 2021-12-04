filename = __file__.strip("py") + "txt"
file = open(filename, "r")
data = file.readlines()

import math

nums = [int(x) for x in data[0].split(",")]
boards = [[int(x) for y in data[i:i+5] for x in y.split()] for i in range(2, len(data), 6)]

def Part1():
    quickestTurn = len(nums) + 1
    quickestScore = 0

    for board in boards:
        rows = [0 for i in range(5)]
        cols = rows.copy()
        solvedBoard = board.copy()

        for turn, num in enumerate(nums):
            if num in solvedBoard:
                solvedBoard.remove(num)
                cols[board.index(num) % 5] += 1
                rows[math.floor(board.index(num) / 5)] += 1

                if max(max(cols),max(rows)) == 5:
                    if turn < quickestTurn:
                        quickestTurn = turn
                        quickestScore = sum(solvedBoard) * num
                    break

    return quickestScore

def Part2():
    slowestTurn = 0
    slowestScore = 0

    for board in boards:
        rows = [0 for i in range(5)]
        cols = rows.copy()
        solvedBoard = board.copy()

        for turn, num in enumerate(nums):
            if num in solvedBoard:
                solvedBoard.remove(num)
                cols[board.index(num) % 5] += 1
                rows[math.floor(board.index(num) / 5)] += 1

                if max(max(cols),max(rows)) == 5:
                    if turn > slowestTurn:
                        slowestTurn = turn
                        slowestScore = sum(solvedBoard) * num
                    break

    return slowestScore

print(Part1())
print(Part2())
