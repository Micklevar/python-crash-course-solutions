dream_vacation = []

place = True

while place:

    prompt = input("What place would you like to visit? ('0' if you don't want to enter any more places): ")
    
    if prompt != '0':
        dream_vacation.append(prompt)
    else:
        print("\nThe places you want to go are:")
        for place in dream_vacation:
            print(place)