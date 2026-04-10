import itertools

# Input list
colors = ['red', 'green', 'blue']

# Generate Cartesian product of size 2 (combinations with repetition AND order)
result = list(itertools.product(colors, repeat=2))

for item in result:
    print(item)
