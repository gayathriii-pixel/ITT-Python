import itertools

# Input list
items = ['X', 'Y', 'Z']

# Generate all permutations of length 3
perms = list(itertools.permutations(items))

# Print each permutation
for p in perms:
    print(p)