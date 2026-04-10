import itertools

# Input list
items = [1, 2]

# Generate combinations with replacement of size 2
comb_wr = list(itertools.combinations_with_replacement(items, 2))

print(comb_wr)