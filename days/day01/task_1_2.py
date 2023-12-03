with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

# Find first / last string that is a digit
first_nums = [next(n for n in line if n.isdigit()) for line in lines]
last_nums = [next(n for n in line[::-1] if n.isdigit()) for line in lines]

# Task 1
print(sum([int(a + b) for a, b in zip(first_nums, last_nums)]))

# Task 2
nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def find_first_last_match(line):
    """Iterate over line, get first num, keep track of last visited num"""
    first = None
    last = None
    idx = 0
    while idx < len(line):
        if line[idx].isdigit():
            # Digit in string
            if first is None:
                first = int(line[idx])
            last = int(line[idx])

        for n_idx, num in enumerate(nums):
            if line[idx:].startswith(num):
                # Substring of line starting at current idx is a number
                if first is None:
                    first = n_idx + 1
                last = n_idx + 1
        idx += 1
    return int(f'{first}{last}')

print(sum([find_first_last_match(line) for line in lines]))
