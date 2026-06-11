# 9-4. Number Served:

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
        self.number_served = 10

    def describe_restaurant(self):
        """Describe a name and type of cuisine of restaurant"""
        print(f"The name of restaurant is {self.name} and the type of his cuisine is {self.type}")
        
    def open_restaurant(self):
        """Report that restaurant open"""
        print("The restaurant is open!")
    def set_number_served(self, served):
        """Set the number of customers that have been served"""
        self.number_served = served
    def increment_number_served(self, served):
        """Increment the number of customers that have been served"""
        self.number_served += served


restaurant = Restaurant('Rukito', 'barbecue')
restaurant.set_number_served(20)
restaurant.increment_number_served(3)
print(restaurant.number_served)
