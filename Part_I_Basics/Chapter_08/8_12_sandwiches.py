# 8-12. Sandwiches: 

def ingredients_sandwiches(*ingredients):

    """Add ingredients to a sandwich"""

    print(f"\nThe ingredients of the sandwich will be:\n")

    for ing in ingredients:
        print(f"- {ing}")


ingredients_sandwiches("salchicha", "pollo", "lechuga")

ingredients_sandwiches("tomate", "papa", "pimiento", "huevo")

ingredients_sandwiches("mantequilla", "jamon", "carne")


