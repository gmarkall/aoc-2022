with open('day1.txt') as f:
    lines = [line.strip() for line in f.readlines()]

calories = []

total = 0
for line in lines:
    if line:
        total += int(line)
    else:
        calories.append(total)
        total = 0

print(max(calories))
print(sum(sorted(calories)[-3:]))
