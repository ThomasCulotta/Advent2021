filename = __file__.strip("py") + "txt"
file = open(filename, "r")
data = file.readlines()

import math

def Part1():
    length = len(data)
    binlength = len(data[0]) - 1

    bits = [1 if sum([(int(x[y])) for x in data]) > length / 2 else 0 for y in range(binlength)]

    gamma = epsilon = 0
    for i,x in enumerate(bits[::-1]):
        gamma += 2 ** i * x
        epsilon += 2 ** i * (1 - x)

    return gamma * epsilon

def Part2():
    binlength = len(data[0]) - 1
    oxy = co2 = data

    for i in range(binlength):
        if len(oxy) > 1:
            oxyBits = math.floor(sum([(int(x[i])) for x in oxy]) / len(oxy) + 0.5)
            oxy = [x for x in oxy if int(x[i]) == oxyBits]

        if len(co2) > 1:
            co2Bits = math.floor(sum([(int(x[i])) for x in co2]) / len(co2) + 0.5)
            co2 = [x for x in co2 if 1 - int(x[i]) == co2Bits]

    print(oxy,co2)
    oxyDec = 0
    for i,x in enumerate(oxy[0][-2::-1]):
        oxyDec += 2 ** i * int(x)

    co2Dec = 0
    for i,x in enumerate(co2[0][-2::-1]):
        co2Dec += 2 ** i * int(x)

    return oxyDec * co2Dec

print(Part1())
print(Part2())
