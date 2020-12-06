file = open("input.txt").read().splitlines()

part1 = 0
part2 = 0
for string in file:
    temp, password = string.split(":")
    numbers, letter = temp.split(" ")
    first, second = map(int, numbers.split("-"))

    # part 1
    if first <= password.count(letter) <= second:
        part1 += 1

    # part 2
    if (password[first] == letter) != (password[second] == letter):
        part2 += 1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
