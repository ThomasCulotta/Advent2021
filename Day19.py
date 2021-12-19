filename = "Inputs/" + __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.readlines()

import operator

scanners = []

scannerIndex = 0
for line in data:
    if line.startswith("---"):
        scanners.append([])
        continue

    if line.isspace():
        scannerIndex += 1
        continue

    coords = line.split(",")
    scanners[scannerIndex].append((int(coords[0]), int(coords[1]), int(coords[2])))

# XYZ    = 0   YZX    = 4   ZXY    = 8
# XZIY   = 1   YXIZ   = 5   ZYIX   = 9
# XIYIZ  = 2   YIZIX  = 6   ZIXIY  = 10
# XIZY   = 3   YIXZ   = 7   ZIYX   = 11
#
# IXZY   = 12  IYXZ   = 16  IZYX   = 20
# IXYIZ  = 13  IYZIX  = 17  IZXIY  = 21
# IXIZIY = 14  IYIXIZ = 18  IZIYIX = 22
# IXIYZ  = 15  IYIZX  = 19  IZIXY  = 23

def RotateScanner(scanner, space):
    rotatedBeacons = []

    for beacon in scanner:
        x, y, z = 0, 0, 0

        if   space in range(4):        x =  beacon[0]
        elif space in range(4,   8):   x =  beacon[1]
        elif space in range(8,  12):   x =  beacon[2]
        elif space in range(12, 16):   x = -beacon[0]
        elif space in range(16, 20):   x = -beacon[1]
        else:                          x = -beacon[2]

        if   space in [5,  8, 16, 21]: y =  beacon[0]
        elif space in [0,  9, 13, 20]: y =  beacon[1]
        elif space in [1,  4, 12, 17]: y =  beacon[2]
        elif space in [7, 10, 18, 23]: y = -beacon[0]
        elif space in [2, 11, 15, 22]: y = -beacon[1]
        else:                          y = -beacon[2]

        if   space in [4, 11, 19, 20]: z =  beacon[0]
        elif space in [3,  8, 12, 23]: z =  beacon[1]
        elif space in [0,  7, 15, 16]: z =  beacon[2]
        elif space in [6,  9, 17, 22]: z = -beacon[0]
        elif space in [1, 10, 14, 21]: z = -beacon[1]
        else:                          z = -beacon[2]

        rotatedBeacons.append((x, y, z))

    return rotatedBeacons

def Part1And2():
    trueScanners = [[] for index in range(len(scanners))]
    trueScanners[0] = scanners[0]
    scannerPositions = [(0,0,0)]

    checkedScanners = {0}
    checkingScanners = [0]
    while len(checkingScanners) and len(checkedScanners) < len(trueScanners):
        latestScanner = checkingScanners.pop()
        for index in range(len(scanners)):
            if index in checkedScanners:
                continue

            for space in range(24):
                scanner = RotateScanner(scanners[index], space)

                scannerFound = False
                for fixedBeacon in trueScanners[latestScanner]:
                    for beacon in scanner[:-11]:
                        offset = tuple(map(operator.sub, fixedBeacon, beacon))
                        offsetScanner = [tuple(map(operator.add, offset, curBeacon)) for curBeacon in scanner]

                        if len(set(trueScanners[latestScanner]) & set(offsetScanner)) >= 12:
                            trueScanners[index] = offsetScanner
                            scannerPositions.append(offset)
                            checkedScanners.add(index)
                            checkingScanners.append(index)
                            scannerFound = True
                            break

                    if scannerFound:
                        break

                if scannerFound:
                    break

    beaconSet = set()
    beaconSet = beaconSet.union(*trueScanners)

    scannerDistances = [sum(tuple(map(abs, map(operator.sub, scanner1, scanner2)))) for scanner1 in scannerPositions for scanner2 in scannerPositions]

    return len(beaconSet), max(scannerDistances)

print(Part1And2())
