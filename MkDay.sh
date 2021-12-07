fname="Day"$1

touch $fname".py"
touch $fname".txt"

printf "filename = __file__.strip(\"py\") + \"txt\"
with open(filename, \"r\") as file:
    data = file.readlines()

def Part1():
    return 0

def Part2():
    return 0

print(Part1())
print(Part2())
" > $fname".py"
