# 8-12. Sandwiches: 

def ingredients_sandwiches(*ingredients):

    print(f"\nLos ingredientes del sandwich seran:\n")

    for ing in ingredients:
        print(f"- {ing}")


ingredients_sandwiches("salchicha", "pollo", "lechuga")

ingredients_sandwiches("tomate", "papa", "pimiento", "huevo")

ingredients_sandwiches("mantequilla", "jamon", "carne")


