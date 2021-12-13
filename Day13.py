filename = __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.readlines()

dots = [(int(pair[0]), int(pair[1])) for line in data if len(pair := line.split(",")) == 2]
intstructions = [((pair := line.split("="))[0][-1], int(pair[1])) for line in data[len(dots) + 1:]]

def Part1():
    dots1 = dots.copy()
    fold = intstructions[0]
    removeDots = []
    for index in range(len(dots1)):
        dot = dots1[index]

        if fold[0] == "x":
            diff = dot[0] - fold[1]

            if diff > 0:
                if (dot[0] - 2 * diff, dot[1]) in dots1:
                    removeDots.append(dot)
                else:
                    dots1[index] = (dot[0] - 2 * diff, dot[1])
        else:
            diff = dot[1] - fold[1]

            if diff > 0:
                if (dot[0], dot[1] - 2 * diff) in dots1:
                    removeDots.append(dot)
                else:
                    dots1[index] = (dot[0], dot[1] - 2 * diff)

    for dot in removeDots:
        dots1.remove(dot)

    return len(dots1)

def Part2():
    for fold in intstructions:
        removeDots = []

        for index in range(len(dots)):
            dot = dots[index]

            if fold[0] == "x":
                diff = dot[0] - fold[1]
                if diff > 0:
                    if (dot[0] - 2 * diff, dot[1]) in dots:
                        removeDots.append(dot)
                    else:
                        dots[index] = (dot[0] - 2 * diff, dot[1])
            else:
                diff = dot[1] - fold[1]
                if diff > 0:
                    if (dot[0], dot[1] - 2 * diff) in dots:
                        removeDots.append(dot)
                    else:
                        dots[index] = (dot[0], dot[1] - 2 * diff)

        for dot in removeDots:
            dots.remove(dot)

    maxX = max([dot[0] for dot in dots])
    maxY = max([dot[1] for dot in dots])

    printDots = [["#" if (x, y) in dots else "." for x in range(maxX + 1)] for y in range(maxY + 1)]
    for line in printDots:
        print("".join(line))

    return (maxX, maxY)

print(Part1())
print(Part2())
