#4-10. Slices: 
list_guests = ['Misato Katsuragi', 'Ana de Armas', 'Asuna Yuuki', 'Asuka Langley', 'Touka Kirishima', 'Aiko Tanaka', 'Casca']

#first point
print(f"The first three items in the list guests: {list_guests[:3]}")
print(len(list_guests))
#Second point
print(f"Three items from the middle of the list guests: {list_guests[2:5]}")
#Third point
print(f"The last three items in the list are: {list_guests[-3:]}")

#4-11. My Pizzas, Your Pizzas:
pizzas = ['pepperoni', 'hawaiian', 'meat lovers']

friend_pizzas = pizzas[:]
print(f"pizzas: {pizzas}\nfriend pizzas: {friend_pizzas}\n")

#First point
pizzas.append('neopolitan')
print(f"Add new pizza type in pizzas list: {pizzas}")

#Second oint
friend_pizzas.insert(2, 'colorado')
print(f"Add new pizza type in friend pizza list: {friend_pizzas}")

#Third point
for pizza in pizzas:
    print(f"My favorite pizzas are: {pizza}")
for pizza in friend_pizzas:
    print(f"My friend's favorite pizzas are: {pizza}")

print(f"\n")

#4-12. More Loops:
my_foods = ['pizza', 'falafel', 'carrot cake', 'canolli']
friend_foods = ['pizza', 'falafel', 'carrot cake', 'ice cream']

for food in my_foods:
    print(f"Elements in my foods list: {food}")

for food in friend_foods:
    print(f"Elements in friend foods list: {food}")

