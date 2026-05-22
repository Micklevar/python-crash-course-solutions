# 7.4. Pizza Toppings:

pizza = []
prompt = "\nPlease, enter the topping for your pizza"
prompt += " (If you're done, type 'quit'): "

while True:
    topping = input(prompt)

    if topping == 'quit':
        print(f"Okay, so your pizza would have: {pizza[:]}")
        break 

    else:
        pizza.append(topping)
        print(f"Ready, {topping} has been added to your pizza")