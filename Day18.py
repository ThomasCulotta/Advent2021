filename = "Inputs/" + __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.readlines()

import ast, math, copy
from enum import Enum

dataListBase = [ast.literal_eval(line) for line in data]

class ExplodeOp(Enum):
    NONE     = 0
    SEARCH   = 1
    ADDLEFT  = 2
    ADDRIGHT = 3

class SplitOp(Enum):
    NONE   = 0
    SEARCH = 1

def SearchExplode(pair, depth=1, op=ExplodeOp.SEARCH, addVal=0):
    for index in range(2):
        if op == (ExplodeOp.ADDLEFT if index == 0 else ExplodeOp.ADDRIGHT):
            if isinstance(pair[1 - index], list):
                pair[1 - index], newOp, newAddVal = SearchExplode(pair[1 - index], depth + 1, op, addVal)
                return pair, newOp, newAddVal

            pair[1 - index] += addVal
            return pair, ExplodeOp.NONE, 0

    if depth == 4:
        for index in range(2):
            if isinstance(pair[index], list):
                if isinstance(pair[1 - index], list):
                    pair[1 - index], newOp, newAddVal = SearchExplode(pair[1 - index], depth + 1, ExplodeOp.ADDRIGHT if index == 0 else ExplodeOp.ADDLEFT, pair[index][1 - index])
                else:
                    pair[1 - index] += pair[index][1 - index]

                leftAdd = pair[index][index]
                pair[index] = 0
                return pair, ExplodeOp.ADDLEFT if index == 0 else ExplodeOp.ADDRIGHT, leftAdd

        return pair, ExplodeOp.SEARCH, 0

    newOp, newAddVal = ExplodeOp.NONE, 0
    for index in range(2):
        if isinstance(pair[index], list):
            pair[index], newOp, newAddVal = SearchExplode(pair[index], depth + 1)

            if newOp == ExplodeOp.NONE or newOp == (ExplodeOp.ADDLEFT if index == 0 else ExplodeOp.ADDRIGHT):
                return pair, newOp, newAddVal

            if newOp == (ExplodeOp.ADDRIGHT if index == 0 else ExplodeOp.ADDLEFT):
                if isinstance(pair[1 - index], list):
                    pair[1 - index], newOp, newAddVal = SearchExplode(pair[1 - index], depth + 1, newOp, newAddVal)
                    return pair, newOp, newAddVal

                pair[1 - index] += newAddVal
                return pair, ExplodeOp.NONE, 0

    return pair, ExplodeOp.SEARCH, newAddVal

def SearchSplit(pair, op=SplitOp.SEARCH):
    for index in range(2):
        if isinstance(pair[index], list):
            pair[index], newOp = SearchSplit(pair[index])

            if newOp == SplitOp.NONE:
                return pair, newOp

        elif pair[index] > 9:
            pair[index] = [pair[index] // 2, math.ceil(pair[index] / 2)]
            return pair, SplitOp.NONE

    return pair, SplitOp.SEARCH

def Reduce(pair):
    explodeOp, splitOp = ExplodeOp.NONE, SplitOp.NONE
    while (explodeOp != ExplodeOp.SEARCH or splitOp != SplitOp.SEARCH):
        explodeOp, splitOp = ExplodeOp.SEARCH, SplitOp.SEARCH
        pair, explodeOp, addVal = SearchExplode(pair)

        if explodeOp != ExplodeOp.SEARCH:
            continue

        pair, splitOp = SearchSplit(pair)

    return pair

def GetMagnitude(pair):
    if not isinstance(pair, list):
        return pair

    return (3 * GetMagnitude(pair[0])) + (2 * GetMagnitude(pair[1]))

def Part1():
    dataList = copy.deepcopy(dataListBase)
    runningList = dataList[0]

    for pair in dataList[1:]:
        runningList = Reduce([runningList, pair])

    return GetMagnitude(runningList)

def Part2():
    magnitudes = []

    for index1 in range(len(dataListBase)):
        for index2 in range(len(dataListBase)):
            if index1 == index2:
                continue

            addedList = Reduce(copy.deepcopy([dataListBase[index1], dataListBase[index2]]))
            magnitudes.append(GetMagnitude(addedList))

    return max(magnitudes)

print(Part1())
print(Part2())
