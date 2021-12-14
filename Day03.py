filename = "Inputs/" + __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.readlines()

import math

def Part1():
    length = len(data)
    binlength = len(data[0]) - 1

    bits = [1 if sum([(int(num[index])) for num in data]) > length / 2 else 0 for index in range(binlength)]

    gamma = epsilon = 0
    for index,bit in enumerate(bits[::-1]):
        gamma += 2 ** index * bit
        epsilon += 2 ** index * (1 - bit)

    return gamma * epsilon

def Part2():
    binlength = len(data[0]) - 1
    oxy = co2 = data

    for index in range(binlength):
        if len(oxy) > 1:
            oxyBits = math.floor(sum([(int(bit[index])) for bit in oxy]) / len(oxy) + 0.5)
            oxy = [bit for bit in oxy if int(bit[index]) == oxyBits]

        if len(co2) > 1:
            co2Bits = math.floor(sum([(int(bit[index])) for bit in co2]) / len(co2) + 0.5)
            co2 = [bit for bit in co2 if 1 - int(bit[index]) == co2Bits]

    oxyDec = 0
    for index, bit in enumerate(oxy[0][-2::-1]):
        oxyDec += 2 ** index * int(bit)

    co2Dec = 0
    for index, bit in enumerate(co2[0][-2::-1]):
        co2Dec += 2 ** index * int(bit)

    return oxyDec * co2Dec

print(Part1())
print(Part2())
