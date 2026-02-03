#5-8. Hello Admin:
names = ["micklevar" , "sofia" , "admin" , "kirito" , "jake" , "ash"]

if names:
    for name in names:
        if name == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hi {name} it's great to see you again")
#5-9. No users:            
else:
    print("We need to find some users!")
    

#5-10. Checking Usernames:

current_users = ["micklevar", "Donbolonario", "Goldenbikes", "phoexn", "agilidan"]

new_users = ["donbolonario", "garbanzo", "goldenbikes", "Kirito", "jsteve"]

for user in new_users:
    for current in current_users:
        if user.lower() == current.lower():
            print("That name is no longer available, please enter a new one")
        else:
            print("Username is available")

#5-11. Ordinal Numbers:

ordinal_numbers = []

for ordinal in range(1,10):
    ordinal_numbers.append(ordinal)
    


for i in ordinal_numbers:
    if i == 1:
        print(f"{i}st\n")
    elif i == 2:
        print(f"{i}nd\n")
    elif i == 3:
        print(f"{i}rd\n")
    else:
        print(f"{i}th\n")

        
