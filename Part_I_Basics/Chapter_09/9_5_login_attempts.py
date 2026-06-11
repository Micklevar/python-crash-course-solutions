# 9-5. Login Attempts:

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


first_user = User("Alejandro", "Santos", 23, "Ecuador")

first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.increment_login_attempts()

print(f"Number of login attempts: {first_user.login_attempts}")

first_user.reset_login_attempts()
print(f"Number of login attempts: {first_user.login_attempts}")


    