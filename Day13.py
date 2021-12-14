filename = "Inputs/" + __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.readlines()

dots = [(int(pair[0]), int(pair[1])) for line in data if len(pair := line.split(",")) == 2]
intstructions = [((pair := line.split("="))[0][-1], int(pair[1])) for line in data[len(dots) + 1:]]

def Part1():
    fold = intstructions[0]
    dots1 = []

    if fold[0] == "x":
        dots1 = [dot if diff < 0 else
                 (fx, dot[1]) for dot in dots if (diff := dot[0] - fold[1]) < 0 or
                                                 ((fx := dot[0] - 2 * diff), dot[1]) not in dots]
    else:
        dots1 = [dot if diff < 0 else
                 (dot[0], fy) for dot in dots if (diff := dot[1] - fold[1]) < 0 or
                                                 (dot[0], (fy := dot[1] - 2 * diff)) not in dots]

    return len(dots1)

def Part2():
    global dots

    for fold in intstructions:
        if fold[0] == "x":
            dots = [dot if diff < 0 else
                    (fx, dot[1]) for dot in dots if (diff := dot[0] - fold[1]) < 0 or
                                                    ((fx := dot[0] - 2 * diff), dot[1]) not in dots]
        else:
            dots = [dot if diff < 0 else
                    (dot[0], fy) for dot in dots if (diff := dot[1] - fold[1]) < 0 or
                                                    (dot[0], (fy := dot[1] - 2 * diff)) not in dots]

    maxX = max([dot[0] for dot in dots])
    maxY = max([dot[1] for dot in dots])

    printDots = [["█" if (x, y) in dots else
                  " " for x in range(maxX + 1)] for y in range(maxY + 1)]

    for line in printDots:
        print("".join(line))

print(Part1())
Part2()
