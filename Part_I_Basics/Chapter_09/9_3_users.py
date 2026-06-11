# 9-3. Users:

class User:
    """
    Represent a basic user

    Args:
        first_name (str): First name of user
        last_name (str): Last name of user
        age (int): Age of user
        country (str): Country of user
    """
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    def describe_user(self):
        """
        Describe the atributes of user

        return:
            string: summary of user information
        """
        
        print(f"--- User Data ---\n")
        print("--------------------")
        print(f"-First name: {self.first_name}\n-Last name: {self.last_name}\n-Age: {self.age}\n-Country: {self.country}")

    def greet_user(self):
        """
        Greet the user

        return:
            string: personalized greeting to the user
        """
        print(f"Hi {self.first_name} welcome!")
        
first_user = User("Alejandro", "Santos", 23, "Ecuador")
second_user = User("Jeremy", "Bravo", 26, "Ecuador")


first_user.describe_user()
first_user.greet_user()

second_user.describe_user()
second_user.greet_user()