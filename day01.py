import submit

file = list(map(int, open("input.txt").read().splitlines()))

for x in file:
    for y in file[file.index(x):]:
        for z in file[file.index(y):]:
            if x + y + z == 2020:
                print(x * y * z)
