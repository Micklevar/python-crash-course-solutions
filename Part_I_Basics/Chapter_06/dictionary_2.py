#6-4. Glossary 2:
programming_words = {
    "iteration" : "the repetition of a process or utterance",
    "slicing" : "cut (something, especially food) into slices",
    "inmutability" : "the quality or state of being unchangeable, constant, and unable to be altered once created",
    "elif" : "It is used in conditional statements to check multiple conditions in sequence",
    "boolean" : "is a fundamental concept used for logical operations and decision-making",
    "looping": "the process of repeatedly executing a block of code until a specific condition is met or for each item in a sequence",
    "Key": "a unique, immutable identifier used to access a corresponding value within a dictionary",
    "Object": "the fundamental abstraction for data",
    "Dictionaries": "a built-in, mutable data structure that stores data in a collection of key-value pairs",
}

for key, value in programming_words.items():
    print(f"{key}:\n\t{value}")

#6-5. Rivers:
rivers = {
    "Amazonas" : "Ecuador",
    "Nilo" : "Egipto",
    "Danubio" : "Alemania",
}

print("\nValues:")
for value in rivers.values():
    print(f"\n\t{value}")

print("Keys: ")
for key in rivers.keys():
    print(f"\n\t{key}")

#6-7. Polling:
favorite_languages = {
    "jen" : "python",
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

new_participants = ["gabriel", "sarah", "steve", "phil"]

for participant in new_participants:
    if participant in favorite_languages:
        print(f"{participant.title()}, thank you so much for participating")
    else:
        print(f"{participant.title()}, i invite you to participate in this survey")