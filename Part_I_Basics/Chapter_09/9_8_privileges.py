# 9-7. Admin:

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
        self.login_attempts = 0

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
    
    def increment_login_attempts(self):
        """ Increment the value of login attempts by 1"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """ Resets the value of login attempts to 0"""
        self.login_attempts = 0

class Privileges:
    """Create a list of privileges"""
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Print the list of privileges of administrator"""
        print("The privileges of administrator are:\n")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    """Create a simple user type Admin"""
    def __init__(self, first_name, last_name, age, country):
        """Initialize attributes of the parent class"""

        super().__init__(first_name, last_name, age, country)
        self.privileges = Privileges() # Instance of class Privileges


# Instance the class to create a object 'first_admin'
first_administrator = Admin('Alejandro', 'Santos', 23, 'Ecuador')

first_administrator.describe_user()
first_administrator.privileges.show_privileges()