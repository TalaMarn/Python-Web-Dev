import string
import itertools

char = string.ascii_lowercase
combinations = [''.join(p) for p in itertools.product(char, repeat=4)]

print({len(combinations)})
for combination in combinations:
    print(f'May{combination}')