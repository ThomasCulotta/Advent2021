filename = "Inputs/" + __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.readlines()

start = data[0].strip()
polyMap = {(pair := line.strip().split(" -> "))[0]:pair[1] for line in data[2:]}

def Part1():
    result = start

    for step in range(10):
        result = [result[0]] + [elem for index in range(1, len(result)) for elem in (polyMap[result[index - 1] + result[index]], result[index])]

    mostNum = result.count(max(set(result), key=result.count))
    leastNum = result.count(min(set(result), key=result.count))

    return mostNum - leastNum

def Part2():
    mapCounts = {(key := start[index - 1] + start[index]):start.count(key) for index in range(1, len(start))}
    elemCounts = {char:start.count(char) for char in start}

    for step in range(40):
        newMapCounts = {}

        for key, val in mapCounts.items():
            elem = polyMap[key]
            resultL = key[0] + elem
            resultR = elem + key[1]

            if elem in elemCounts: elemCounts[elem] += val
            else:                  elemCounts[elem]  = val

            if resultL in newMapCounts: newMapCounts[resultL] += val
            else:                       newMapCounts[resultL]  = val

            if resultR in newMapCounts: newMapCounts[resultR] += val
            else:                       newMapCounts[resultR]  = val

        mapCounts = {key:newMapCounts[key] if key in newMapCounts else 0 for key in newMapCounts.keys()}

    mostNum = max(elemCounts.values())
    leastNum = min(elemCounts.values())

    return mostNum - leastNum

print(Part1())
print(Part2())
