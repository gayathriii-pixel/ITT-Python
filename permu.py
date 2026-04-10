import itertools

# Input string
text = '123'

# Generate all permutations
perms = list(itertools.permutations(text))

# Print each permutation joined as a string
for p in perms:
    print(''.join(p))