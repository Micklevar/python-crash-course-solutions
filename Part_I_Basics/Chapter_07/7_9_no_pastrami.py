# 7.9. No Pastrami:

sandwich_orders = ['pastrami', 'queso', 'pollo', "pastrami", 'mortadela', 'jamon', "pastrami"]

finished_sandwiches = []

print("We're out of pastrami, pastrami orders will be cancelled.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print(f"Total sandwiches prepared: {len(sandwich_orders)} \n")
for tipo in sandwich_orders:
    print(f"Prepare your sandwich {tipo}")
    
    finished_sandwiches.append(tipo)

size = len(finished_sandwiches)
print(f"The total number of sandwiches made was: {size}:\n")
n = 0

while n < size:
    print("=====================")
    print(f"{n} | {finished_sandwiches[n]} |")
    n += 1

print("=====================")