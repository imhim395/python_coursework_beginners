ints = int(input("enter an integer: "))
original = ints
summed = ints

while ints > 0:
    summed += ints
    ints -= 1

print("your original number was", original)
print("your summed number is", summed)

