x=1
print(type (x))
a=float(x)
print(type (a))
y=34.4
print(type (y))
a=complex(y)
print(type (a))
y=1+6j
print(type (y))


import random

print(random.randrange(1, 10))

import random

# Generate a random number between 1 and 100
print(random.randint(1, 100))

# Randomly select an element from a list
colors = ['red', 'blue', 'green', 'yellow']
print(random.choice(colors))

# Shuffle a list of numbers
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
# print(numbers)

import random
print(random.randint(1,10))

colors=["blue","green","yellow","gray","pink"]
print(random.choice(colors))

random.shuffle(colors)
print(colors)

