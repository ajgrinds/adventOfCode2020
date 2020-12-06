file = open("input.txt").read().splitlines()

max_id = 0
a = set()

for x in file:
    seat = 128 // 2
    distance = 128 / 2
    for z in x[:7]:
        distance /= 2
        if z == "F":
            seat -= distance
        elif z == "B":
            seat += distance
    seat = int(seat)
    row = 8 // 2
    distance = 8 / 2
    for z in x[7:]:
        distance /= 2
        if z == "R":
            row += distance
        if z == "L":
            row -= distance
    row = int(row)
    a.add(seat * 8 + row)

print(max(a))
for x in a:
    if x - 1 not in a and x - 2 in a:
        print(x - 1)

print("Part 1:")
print(max(int(x.translate({70:48,66:49,76:48,82:49}),2) for x in open("input.txt").readlines()))

print("Part 2:")
print((max(y:=[int(x.translate({70:48,66:49,76:48,82:49}),2) for x in open("input.txt").readlines()])**2+max(y)-min(y)**2+min(y))/2-sum(y))
