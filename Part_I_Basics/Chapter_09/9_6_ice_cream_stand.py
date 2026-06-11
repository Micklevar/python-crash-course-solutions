# 9-6. Ice Cream Stand:

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

class IceCreamStand(Restaurant):
    """Create a simple ice cream restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of the parent class.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'oreo', 'mym']
    def display_flavors(self):
        for flavor in self.flavors:
            print(flavor)


boggati = IceCreamStand('bogatti', 'dessert')
boggati.describe_restaurant()
boggati.display_flavors()