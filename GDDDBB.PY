numbers = [4, 8, 15, 16, 23, 42]

# Sum
total = 0
for n in numbers:
    total += n
print("Sum:", total)

# Maximum
maximum = numbers[0]
for n in numbers:
    if n > maximum:
        maximum = n
print("Max:", maximum)

# Minimum
minimum = numbers[0]
for n in numbers:
    if n < minimum:
        minimum = n
print("Min:", minimum)

# Count how many are greater than 10
count = 0
for n in numbers:
    if n > 10:
        count += 1
print("Count > 10:", count)

# Average
average = total / len(numbers)
print("Average:", average)