#6-1. Person:

personal_information = {
    "first_name" : "Gabriel", 
    "last_name" : "Feijoo", 
    "age" : 21, 
    "city" : "Machala",
    }

for clave, valor in personal_information.items():
    print(clave , valor)

#6-2. Favorite Numbers:
favorite_numbers = {
    "gabriel" : 4,
    "david" : 2,
    "steve" : 21,
    "alejandro": 6,
    "viki" : 1,
}

for clave, valor in favorite_numbers.items():
    print(clave,valor)

#6-3. Glossary:

programming_words = {
    "iteration" : "the repetition of a process or utterance",
    "slicing" : "cut (something, especially food) into slices",
    "inmutability" : "the quality or state of being unchangeable, constant, and unable to be altered once created",
    "elif" : "It is used in conditional statements to check multiple conditions in sequence",
    "boolean" : "is a fundamental concept used for logical operations and decision-making"
}

for clave, valor in programming_words.items():
    print(f"{clave}:\n\t{valor}")