from collections import defaultdict


with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

grid = defaultdict(lambda: defaultdict(lambda: "."))  # Defaultdict to avoid index out of bounds
star_nums = defaultdict(lambda: defaultdict(lambda: []))  # Store for each star what part numbers are adjacent
for i in range(len(lines)):
    grid[i] = defaultdict(lambda: ".")
    star_nums[i] = defaultdict(lambda: [])
    for j in range(len(lines[i])):
        grid[i][j] = lines[i][j]

def is_symbol(s: str) -> bool:
    return not s.isdigit() and not s == '.'

def is_adjacent_to_symbol(i: int, j: int) -> bool:
    valid = False
    valid = valid or is_symbol(grid[i - 1][j]) # Above
    valid = valid or is_symbol(grid[i + 1][j]) # Below
    valid = valid or is_symbol(grid[i][j + 1]) # Left
    valid = valid or is_symbol(grid[i][j - 1]) # Right
    valid = valid or is_symbol(grid[i + 1][j - 1]) # Above Left
    valid = valid or is_symbol(grid[i + 1][j + 1]) # Above Right
    valid = valid or is_symbol(grid[i - 1][j - 1]) # Above Left
    valid = valid or is_symbol(grid[i - 1][j + 1]) # Above Right
    return valid

sum = 0  # Sum of all gear numbers

for curr_line in range(len(lines)):
    idx = 0

    # Walk to start of next number, add number if allowed
    while idx < len(lines[curr_line]):

        # Walk until the start of a new number is found
        while idx < len(lines[curr_line]) and not lines[curr_line][idx].isdigit():
            idx += 1

        # Walk till end of number, check at each step if adj to symbol
        is_valid = False
        current_number = ""
        while idx < len(lines[curr_line]) and lines[curr_line][idx].isdigit():
            is_valid = is_valid or is_adjacent_to_symbol(curr_line, idx)
            current_number += lines[curr_line][idx]
            idx += 1

        # No number found at end of line
        if not current_number:
            continue


        print(f'Number: {current_number} - valid: {is_valid}')
        if is_valid:
            sum += int(current_number)  # Task 1 (sum of valid numbers)

            # Check for each spot adj to this number if it is a star, if yes, add the number to the list for this star
            for area_j in range(curr_line - 1, curr_line + 2):
                for area_i in range(idx - len(current_number) - 1, idx + 1):
                    if grid[area_j][area_i] == "*":
                        star_nums[area_j][area_i] += [current_number]
                    print(grid[area_j][area_i], end='')
                print('\n')

        # Move on
        idx += 1

print(sum)  # Task 1


# Check for each star if it has exactly two stars next to each other
gear_ratios = 0
for i in star_nums:
    for j in star_nums[i]:
        if len(star_nums[i][j]) == 2:
            gear_ratios += int(star_nums[i][j][0]) * int(star_nums[i][j][1])

print(gear_ratios)
