filename = __file__.strip("py") + "txt"
file = open(filename, "r")
data = file.readlines()

fish = [int(x) for x in data[0].split(",")]

def Part1And2(days):
    tracker = [len([y for y in fish if y == x]) for x in range(10)]

    for i in range(days):
        tracker = [x for x in tracker[1:] + tracker[:1]]
        tracker[8] = tracker[9]
        tracker[6] += tracker[9]
        tracker[9] = 0

    return sum(tracker)

print(Part1And2(80))
print(Part1And2(256))
