with open('day2.txt') as f:
    lines = [line.strip() for line in f.readlines()]

move_points = {'X': 1, 'Y': 2, 'Z': 3}

wins = [
    ('A', 'Y'),
    ('B', 'Z'),
    ('C', 'X')
]

draws = [
    ('A', 'X'),
    ('B', 'Y'),
    ('C', 'Z')
]


score = 0
for line in lines:
    moves = tuple(line.split())
    score += move_points[moves[1]]
    if moves in wins:
        score += 6
    elif moves in draws:
        score += 3

print(score)
