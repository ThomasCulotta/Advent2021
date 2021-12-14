filename = "Inputs/" + __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = [line.strip() for line in file.readlines()]

closeToOpen = {
    ")" : "(",
    "]" : "[",
    "}" : "{",
    ">" : "<"
}

openers = { "(", "[", "{", "<" }

def Part1():
    scoreMap1 = {
        ")" : 3,
        "]" : 57,
        "}" : 1197,
        ">" : 25137
    }

    syntaxScore = 0
    for line in data:
        stack = []
        for bracket in line:
            if bracket in openers:
                stack.append(bracket)
            elif closeToOpen[bracket] == stack[-1]:
                stack.pop()
            else:
                syntaxScore += scoreMap1[bracket]
                break

    return syntaxScore

def Part2():
    scoreMap2 = {
        "(" : 1,
        "[" : 2,
        "{" : 3,
        "<" : 4
    }

    syntaxScores = []
    for line in data:
        syntaxScore = 0
        stack = []
        for bracket in line:
            if bracket in openers:
                stack.append(bracket)
            elif closeToOpen[bracket] == stack[-1]:
                stack.pop()
            else:
                stack = []
                break

        if len(stack) > 0:
            for bracket in stack[::-1]:
                syntaxScore *= 5
                syntaxScore += scoreMap2[bracket]

            syntaxScores.append(syntaxScore)

    syntaxScores = sorted(syntaxScores)
    return syntaxScores[int(len(syntaxScores) / 2)]

print(Part1())
print(Part2())
