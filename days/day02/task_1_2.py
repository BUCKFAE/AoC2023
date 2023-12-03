with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

limit = {'r': 12, 'g': 13, 'b': 14}

legal = 0  # Sum of legal game ids (Task 1)
power = 0  # Power of multiplied minimal cubes required (Task 2)

for game_id, line in enumerate(lines):

    # Extract draws and sets
    game, draws = line.split(': ')
    sets = draws.split('; ')

    is_legal = True # Game is legal until proven otherwise

    min_cubes = {}

    # Check if each game is valid, extract minimum number of cubes required
    for set in sets:

        # Extract current draw
        drawn = set.split(', ')
        draw_colors = {}

        for draw in drawn:
            amount, color = draw.split(' ')
            draw_colors[color[0]] = draw_colors.get(color[0], 0) + int(amount) # Total cubes of color this set
            min_cubes[color[0]] = max(min_cubes.get(color[0], 0), int(amount)) # Min number of cubes for all games

        if any([v > limit[c] for c, v in draw_colors.items()]):
            # Any color is above the limit
            is_legal = False

    if is_legal:
        # Add if game id is legal (index starts at one)
        legal += game_id + 1

    # Power is product of all cubes
    power += min_cubes['r'] * min_cubes['g'] * min_cubes['b']

print(legal) # Task 1
print(power) # Task 2
