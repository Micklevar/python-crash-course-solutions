from user import User

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