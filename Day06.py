filename = __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.read()

startFish = [int(fish) for fish in data.split(",")]

def Part1And2(days):
    tracker = [len([fish for fish in startFish if fish == index]) for index in range(10)]

    for day in range(days):
        tracker = [index for index in tracker[1:] + tracker[:1]]
        tracker[8] = tracker[9]
        tracker[6] += tracker[9]
        tracker[9] = 0

    return sum(tracker)

print(Part1And2(80))
print(Part1And2(256))
