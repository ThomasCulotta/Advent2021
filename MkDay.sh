fname="Day"$1

if [ $fname = "Day" ]
then
    fname=`date +"%d"`
    if [ $(date +"%H") -ge 20 ]
    then
        fname="$((fname+1))"
    fi
    fname="Day"$fname
fi

touch $fname".py"
touch Inputs/$fname".txt"

printf "filename = \"Inputs/\" + __file__.strip(\"py\") + \"txt\"
with open(filename, \"r\") as file:
    data = file.readlines()

def Part1():
    return 0

def Part2():
    return 0

print(Part1())
print(Part2())
" > $fname".py"
