# 8-3. T-Shirt:

def make_shirt(size, text_message):
    """Especificar la talla y el mensaje de una camiseta"""
    print(f"- La camiseta es de talla: {size}\n- El mensaje que tendra: {text_message}\n")


make_shirt("M", "i love league of legends") # Using positional arguments
make_shirt(text_message="I love evangelion", size="L") # Using keywords arguments
