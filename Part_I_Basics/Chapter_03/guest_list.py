#3-4. Guest List:
# list of guests i invite for dinner
list_guests = ['Misato Katsuragi', 'Ana de Armas', 'Asuna Yuuki']

# creating invitation message
message = "i wanted to invite you to do dinner tonight, do you tink you can?"

# print the message for each one
print(f"Invitations: \n\tHi {list_guests[0]} {message}.\n\tHi {list_guests[1]} {message}.\n\tHi {list_guests[-1]} {message}")

#3-5. Changing Guest List:
# one invited cant make the dinner
print(f"\nCant assist: {list_guests[-1]}")

#remplace the name of the guest who cant make it with the name of the new person
list_guests[-1] = 'Ludovico P.Luche'

print(f"\nNew invitations: \n\tHi {list_guests[0]} {message}.\n\tHi {list_guests[1]} {message}.\n\tHi {list_guests[-1]} {message}")

#3-6. More Guests:
print("\nHi guys i found a bigger dinner table, the dinner will be more bigger")
list_guests.insert(0, 'Jose Madero')
list_guests.insert(2, 'Gerard Way')
list_guests.append('Zero Two')

print(f"\nMore invitations:\n\tHi {list_guests[0]} {message}.\n\tHi {list_guests[1]} {message}.\n\tHi {list_guests[2]} {message}.\n\tHi {list_guests[3]} {message}/\n\tHi {list_guests[4]} {message}.\n\tHi {list_guests[-1]} {message}")  

#3-7. Shrinking Guest List:

apology_message = "\ni'm sorry, I can only invite two people to dinner this time. When my table arrives, I hope you'll come :)"

list_guests_two = list_guests.pop()
print(f"\nHi {list_guests_two} {apology_message}")
list_guests_two = list_guests.pop()
print(f"Hi {list_guests_two} {apology_message}")
list_guests_two = list_guests.pop()
print(f"Hi {list_guests_two} {apology_message}")
list_guests_two = list_guests.pop()
print(f"Hi {list_guests_two} {apology_message}")

n_inv_message = ", i hope you're doing well. I'll be waiting for you tonight for dinner (don't miss it!)."

print(f"\nHi {list_guests[0]} {n_inv_message}")
print(f"Hi {list_guests[1]} {n_inv_message}")

del list_guests[0]
del list_guests[-1]

print(f"Empty list_guests:  {list_guests}")

