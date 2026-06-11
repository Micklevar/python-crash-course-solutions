# 9-1. Restaurant:

class Restaurant:
    """
        Create a simple restaurant

            Args:
                restaurant_name(str)
                cuisine_type(str)
    """
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        """Describe a name and type of cuisine of restaurant"""
        print(f"The name of restaurant is {self.name} and the type of his cuisine is {self.type}")
        
    def open_restaurant(self):
        """Report that restaurant open"""
        print("The restaurant is open!")


# Instance creation
restaurant = Restaurant('Rukito', 'barbecue')

# Print his atributes
print(f"Atributes:\n\t-{restaurant.name}\n\t-{restaurant.type}")

# Using the methods
restaurant.describe_restaurant()
restaurant.open_restaurant()



