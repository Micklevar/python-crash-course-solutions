#5-3. Alien Colors #1:
alien_color = 'green'

if alien_color == 'green':
    print("You gain 5 points")

if alien_color == 'red':
    print("You gain 5 points")

#5-4. Alien Colors #2:
alien_color = 'red'

if alien_color == 'green':
    print("You gain 5 points")
else:
    print("You gainn 10 points!")

#5-5. Alien Colors #3:
alien_color = 'yellow'

if alien_color == 'green':
    print("You gain 5 points")
elif alien_color == 'yellow':
    print("You gain 10 points")
elif alien_color == 'red':
    print("You gain 15 points")

#5-6. Stages of life:
age = 15

if age < 2:
    print("The person is a baby")
elif (age >= 2) and (age < 4):
    print("The person is a toddler")
elif (age >= 4) and (age < 13):
    print("The person is a kid")
elif (age >= 13) and (age < 20):
    print("The person is a teenager")
elif (age >= 20) and (age < 65):
    print("The person is an adult")
else:
    print("The person is an elder")

#5-7. Favorite Fruit:
favorite_fruits = ['melon', 'mango', 'strawberry']

if 'melon' in favorite_fruits:
    print("You really like melons!")
if 'mango' in favorite_fruits:
    print("You really like mangos!")
if 'strawberry' in favorite_fruits:
    print("You really like strawberrys!")
