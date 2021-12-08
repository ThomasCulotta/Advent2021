filename = __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.readlines()

import re

# cf      : 1
# acf     : 7
# bcdf    : 4
# abdfg   : 5
# acdeg   : 2
# acdfg   : 3
# abcdfg  : 9
# abcefg  : 0
# abdefg  : 6
# abcdefg : 8

outputs = [["".join(sorted(digit)) for digit in data[index].split(" | ")[1].split()] for index in range(len(data))]

def Part1():
    return len([digit for output in outputs for digit in output if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7])

def Segment(chars, length, pattern):
    return re.sub(f"[{chars}]", "", next(digit for digit in pattern if len(digit) == length and min([char in digit for char in chars]))) # g from 9

def Part2():
    total = 0
    patterns = [["".join(sorted(digit)) for digit in data[index].split(" | ")[0].split()] for index in range(len(data))]

    for index in range(len(data)):
        one = next(digit for digit in patterns[index] if len(digit) == 2)
        seven = next(digit for digit in patterns[index] if len(digit) == 3)
        four = next(digit for digit in patterns[index] if len(digit) == 4)
        eight = next(digit for digit in patterns[index] if len(digit) == 7)

        a = re.sub(f"[{one}]", "", seven) # a from 7
        g = Segment(a + four, 6, patterns[index]) # g from 9
        d = Segment(g + seven, 5, patterns[index]) # d from 3
        b = Segment(a + d + g + one, 6, patterns[index]) # b from 9
        f = Segment(a + b + d + g, 5, patterns[index]) # f from 5
        c = one.replace(f, "") # c from 1
        e = re.sub(f"[{a + g + four}]", "", eight) # e from 8

        digitMap = {
            "".join(sorted(c+f))           : "1",
            "".join(sorted(a+c+f))         : "7",
            "".join(sorted(b+c+d+f))       : "4",
            "".join(sorted(a+b+d+f+g))     : "5",
            "".join(sorted(a+c+d+e+g))     : "2",
            "".join(sorted(a+c+d+f+g))     : "3",
            "".join(sorted(a+b+c+d+f+g))   : "9",
            "".join(sorted(a+b+c+e+f+g))   : "0",
            "".join(sorted(a+b+d+e+f+g))   : "6",
            "".join(sorted(a+b+c+d+e+f+g)) : "8"
        }

        total += int("".join([digitMap[digit] for digit in outputs[index]]))

    return total

print(Part1())
print(Part2())
