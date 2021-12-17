filename = "Inputs/" + __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.readlines()[0].split()

rangeX = [int(bound) for bound in data[2].lstrip("x=").rstrip(",").split("..")]
rangeY = [int(bound) for bound in data[3].lstrip("y=").split("..")]

def Part1():
    velY = abs(rangeY[0]) - 1

    return velY * (velY + 1) // 2

def Part2():
    minX, minY = 0, rangeY[0]
    maxX, maxY = rangeX[1], abs(rangeY[0]) - 1
    validValues = 0

    index = 0
    while minX == 0:
        index += 1
        if index * (index + 1) / 2 >= rangeX[0]:
            minX = index

    for velX in range(minX, maxX + 1):
        for velY in range(minY, maxY + 1):
            curVelX, curVelY = velX, velY
            curX, curY = 0, 0

            while curX <= rangeX[1] and curY >= rangeY[0]:
                if curX >= rangeX[0] and curY <= rangeY[1]:
                    validValues += 1
                    break

                curX += curVelX
                curY += curVelY

                if curVelX > 0:
                    curVelX -= 1

                curVelY -= 1

    return validValues

print(Part1())
print(Part2())
