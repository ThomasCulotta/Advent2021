filename = "Inputs/" + __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.readlines()

import math

nums = [int(num) for num in data[0].split(",")]
boards = [[int(num) for board in data[index:index+5] for num in board.split()] for index in range(2, len(data), 6)]

def Part1():
    quickestTurn = len(nums) + 1
    quickestScore = 0

    for board in boards:
        rows = [0 for index in range(5)]
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
        rows = [0 for index in range(5)]
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
