from itertools import product
from collections import deque
from part1 import find_secret

with open("input.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

length, size = 4, 9
sequences_values = {s : 0 for s in product(range(-size, size + 1), repeat = length)}

for number in numbers:
    found_sequences = set()
    sequence = deque()
    compare = number % 10

    for i in range(2000):
        if i >= length:
            comparable = tuple(sequence)

            if comparable not in found_sequences:
                found_sequences.add(comparable)
                sequences_values[comparable] += number % 10

            sequence.popleft()

        number = find_secret(number)
        price = number % 10
        sequence.append(price - compare)
        compare = price

print(max(sequences_values.items(), key = lambda x : x[1]))