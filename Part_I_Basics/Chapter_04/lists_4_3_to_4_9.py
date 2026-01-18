#4-3. Counting to Twenty:

twenty = []

for value in range(1,21):
    twenty.append(value)

print(f"4-3. Twenty: \n\t{twenty}")

#4-4. One million:
million = list(range(1, 1000001))

#for number in million:
    #print(number)

#4-5. Summing a million:
million = list(range(1,1000001))

minimum = min(million)
maximum = max(million)
addition = sum(million)

print(f"4-4. One Million: \n\tMinimum: {minimum}\n\tMaximum: {maximum}\n\tAddition: {addition}")

#4-6. Odd numbers:
odd_numbers = list(range(1, 21, 3))
print(f"4-6. Odd numbers:")
for number in odd_numbers:
    print(f"\t{number}")

#4-7. Threes:

threes = []

for value in range(3, 31, 3):
    threes.append(value)
print(f"4-7.Threes: \n\t{threes}")

#4-8. Cubes:
cubes = []

for cube in range(1,11):
    raised = cube**3
    cubes.append(raised)
print(f"4-8. Cubes: \n\t{cubes}")


#4-9. Cube comprehension:

cubes_2 = [cube**3 for cube in range(1, 11)]
print(f"4-9. Cube comprehension: \n\t{cubes_2}")