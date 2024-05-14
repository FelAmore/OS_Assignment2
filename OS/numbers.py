import random

# Generate 1000 random integers ranging from 0 to 4999
random_numbers = [random.randint(0, 4999) for _ in range(1000)]

# Write the numbers to a text file
with open("input.txt", "w") as file:
    for number in random_numbers:
        file.write(str(number) + "\n")
