#6-7. People:
person_1 = {
    'first_name': 'gabriel',
    'last_name': 'feijoo',
    'age': 21,
    'city': 'machala',
}

person_2 = {
    'first_name': 'valeria',
    'last_name': 'orozco',
    'age': 21,
    'city': 'guayaquil',
}

people_information = [person_1, person_2]

for people in people_information:
    print(people)

#6-8. Pets:

pet_1 = {
    'kind_of_animal': 'giraffe',
    'owners_name': 'gabriel',
}


pet_2 = {
    'kind_of_animal': 'owl',
    'owners_name': 'valeria',
}

pets = [pet_1, pet_2]

for pet in pets:
    print(f"Pet: {pet}")

#6-9. Favorite places:
favorite_places = {
    'gabriel': ['ciudad verde', 'el parque', 'el dalton'],
    'alexander': ['venezuela', 'africa', 'entrada a la 8'],
    'valeria' : ['daule', 'martha roldos', 'trinitaria'],

}

for person, places in favorite_places.items():
    print(f"The favorite places of {person.title()} are: ")
    for place in places:
        print(f"\t{place}")

#6-10. Favorite Numbers:
favorite_numbers = {
    "gabriel" : [4, 11],
    "david" : [2, 100],
    "steve" : [21, 1],
    "alejandro": [6, 9],
    "viki" : [1, 2, 3],
}

for person, numbers in favorite_numbers.items():
    print(f"The favorite numbers of {person.title()} are: ")
    for number in numbers:
        print(f"\t{number}")

#6-11. Cities:
cities = {
    'machala': {
        'country_located': 'ecuador',
        'aprox_population': 300000,
        'fact': 'Is the banana capital of the world',
    },

    'tokio': {
        'country_located': 'japan',
        'aprox_population': 33412512,
        'fact': 'It is considered the world capital of anime and manga',
    },

    'tallinn': {
        'country_located': 'estonia',
        'aprox_population': 456518,
        'fact': 'Is recognized as one of the best-preserved medieval cities in Europe.'
    }
}

for city, city_info in cities.items():
    country = city_info['country_located']
    population = city_info['aprox_population']
    fact = city_info['fact']
    
    print(f"{city.title()}:\n\tCountry: {country.title()}\n\tPopulation: {population}\n\tFact: {fact}")
    