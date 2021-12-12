filename = __file__.strip("py") + "txt"
with open(filename, "r") as file:
    data = file.readlines()

class Cave:
    def __init__(self, name, big, connectedCave=None):
        self.name = name
        self.big = big
        self.connections = {connectedCave} if connectedCave else set()

caves = {}

for line in data:
    name1, name2 = line.strip().split("-")

    cave1 = caves[name1] if name1 in caves else Cave(name1, name1[0].isupper())
    cave2 = caves[name2] if name2 in caves else Cave(name2, name2[0].isupper())

    cave1.connections.add(cave2)
    cave2.connections.add(cave1)

    caves[name1] = cave1
    caves[name2] = cave2

def Search(name, visited):
    paths = 0

    for cave in caves[name].connections:
        if not cave.big and (cave.name == "end" or cave.name in visited):
            if cave.name == "end":
                paths += 1

            continue

        paths += Search(cave.name, visited + [cave.name])

    return paths

def SearchEx(name, visited, extraCave):
    paths = 0

    for cave in caves[name].connections:
        if not cave.big and (cave.name == "end" or cave.name == "start" or cave.name in visited):
            if cave.name == "end":
                paths += 1
            elif cave.name != "start" and not extraCave:
                paths += SearchEx(cave.name, visited + [cave.name], True)

            continue

        paths += SearchEx(cave.name, visited + [cave.name], extraCave)

    return paths

def Part1():
    return Search("start", ["start"])

def Part2():
    return SearchEx("start", ["start"], False)

print(Part1())
print(Part2())
