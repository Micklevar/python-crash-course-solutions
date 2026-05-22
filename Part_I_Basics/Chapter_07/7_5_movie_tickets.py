# 7.5. Movie Tickets:

age = int(input("Welcome to Supercines, how old are you?: "))

while True:
    if age < 3:
        print("Entry is free for you, enjoy your movie")
        break
    elif age > 3 and age < 12:
        print("10 dolars")
        break
    elif age > 12:
        print("15 dolars")
    elif age == 0:
        break