filename = "Inputs/" + __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.readlines()[0].strip()

dataInt = int(data, 16)
dataBin = bin(dataInt).lstrip("0b")

dataPadding = len(data) * 4 - len(dataBin)
dataBin = "".join(["0" for pad in range(dataPadding)]) + dataBin

def ParsePacket(binStr):
    ver, tId = int(binStr[:3], 2), int(binStr[3:6], 2)
    binStr = binStr[6:]
    totalVersion, totalValue = ver, 0

    if tId == 4:
        literal = ""

        while binStr[0] != "0":
            literal += binStr[1:5]
            binStr = binStr[5:]

        literal += binStr[1:5]
        binStr = binStr[5:]

        totalValue = int(literal, 2)

    else:
        lenId = int(binStr[0], 2)
        binStr = binStr[1:]
        subValues = []

        if lenId == 0:
            length = int(binStr[:15], 2)
            binStr = binStr[15:]

            binSubStr = binStr[:length]
            binStr = binStr[length:]

            while len(binSubStr):
                versionSubtotal, subValue, binSubStr = ParsePacket(binSubStr)
                totalVersion += versionSubtotal
                subValues.append(subValue)

        else:
            packetNum = int(binStr[:11], 2)
            binStr = binStr[11:]

            for index in range(packetNum):
                versionSubtotal, subValue, binStr = ParsePacket(binStr)
                totalVersion += versionSubtotal
                subValues.append(subValue)

        if tId == 1:
            totalValue = 1
            for subValue in subValues:
                totalValue *= subValue
        elif tId == 0: totalValue = sum(subValues)
        elif tId == 2: totalValue = min(subValues)
        elif tId == 3: totalValue = max(subValues)
        elif tId == 5: totalValue = 1 if subValues[0] > subValues[1] else 0
        elif tId == 6: totalValue = 1 if subValues[0] < subValues[1] else 0
        elif tId == 7: totalValue = 1 if subValues[0] == subValues[1] else 0

    return totalVersion, totalValue, binStr


def Part1():
    totalVersion, totalValue, dataBin1 = ParsePacket(dataBin)

    return totalVersion

def Part2():
    totalVersion, totalValue, dataBin1 = ParsePacket(dataBin)

    return totalValue

print(Part1())
print(Part2())
