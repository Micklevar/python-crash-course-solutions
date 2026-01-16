#3-8. Seeing the World:
places = ['Akihabara', 'Slovenia', 'Didgori Monument', 'Evangelion Kyoto Base', 'Shibuya']

print(f"Original order: {places}")

#I print the same list in alphabetical order temporarily
print(f"\n\nSame list in alphabetical order temporarily:\n\t{sorted(places)}")
#original order again
print(f"Original order:\n\t{places}")

#I print the same list in reverse-alphabetical order temporarily
print(f"\n\nSame list in reverse-alphabetical order temporarily: \n\t{sorted(places, reverse=True)}")
#original order again
print(f"Original order:\n\t{places}")

#I print the same list but this time in reverse order
places.reverse()
print(f"\n\nSame list in reverse order: {places}")
#I print the same list in reverse order again to show its back to its original order
places.reverse()
print(f"Same list in reverse order again to back to original order: {places}")

#I use sort to change the list to alphabetical order permanent
places.sort()
print(f"\n\nList in permanent alphabetical order: {places}")
#I use sort to sorted in reverse-alphabetical order
places.sort(reverse=True)
print(f"List in permanent reverse-alphabetical order: {places}")

#3-9. Dinner Guests:
list_guests = ['Misato Katsuragi', 'Ana de Armas', 'Asuna Yuuki']

print(f"\n\nThe number guests: {len(list_guests)}")



#3-10: Every Function:

my_favorite_animes = ['Punpun', 'Death Note', 'Evangelion', 'Berserk', 'Chainsaw Man', 'Digimon', 'Dragon Ball', 'Shigatsu wa kimi no uso', 'Tokio Ghoul']
print(f"\n\nOriginal anime list: {my_favorite_animes}")

# Adding an anime to the end of the list
my_favorite_animes.append('Darling in the Franxx')
print(f"\nAdded 'Darling in the Franxx' as the last item: {my_favorite_animes}")

# Inserting an anime into a specific position (index 5)
my_favorite_animes.insert(5, 'Bleach')
print(f"\nList with 'Bleach' inserted: {my_favorite_animes}")

# Permanently deleting an item by index
del my_favorite_animes[7]
print(f"\nList after removing the item at position 8 (index 7): {my_favorite_animes}")

# Popping (removing and storing) the anime I last watched
last_anime = my_favorite_animes.pop(4)
print(f"\nLast anime watched: {last_anime}")

# Removing 'Death Note' by value because I didn't like the ending
my_favorite_animes.remove('Death Note')
print(f"\nList without 'Death Note': {my_favorite_animes}")

# Sorting the list alphabetically (temporary)
print(f"\nAlphabetical order (temporary): {sorted(my_favorite_animes)}")

# Sorting the list alphabetically (permanent)
my_favorite_animes.sort()
print(f"\nAlphabetical order (permanent): {my_favorite_animes}")

# Reversing the current order of the list
my_favorite_animes.reverse()
print(f"\nList in reverse order: {my_favorite_animes}")

# Counting the total number of elements in the list
print(f"\nTotal number of items in the list: {len(my_favorite_animes)}")



