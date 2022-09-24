import random

numbers = []
while len(numbers) <= 6:
    number = random.randint(1, 46)
    if number not in numbers:
        numbers.append(number)

print(sorted(numbers))
