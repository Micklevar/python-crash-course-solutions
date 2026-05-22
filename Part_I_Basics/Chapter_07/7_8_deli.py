# 7.8. Deli:

sandwich_orders = ['pastrami', 'queso', 'pollo', "pastrami", 'mortadela', 'jamon', "pastrami"]

finished_sandwiches = []

print(f"Total sandwiches prepared: {len(sandwich_orders)} \n")
for type in sandwich_orders:
    print(f"Prepare your sandwich {type}")
    
    finished_sandwiches.append(type)

size = len(finished_sandwiches)
print(f"The total number of sandwiches made was: {size}:\n")
n = 0

while n < size:
    print("=====================")
    print(f"{n} | {finished_sandwiches[n]} |")
    n += 1

print("=====================")