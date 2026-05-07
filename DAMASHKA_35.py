"""
This module defines the User class with validation and counter.
"""
class User:
    """Class representing a user with name and password validation """
    total_users = 0

    def __init__(self, user_name, password):
        if not user_name.strip() or len(password.strip()) < 5:
            raise ValueError("Invalid name or password")

        self.user_name = user_name
        self.password = password
        User.total_users += 1


    def __str__(self):
        """Return a string representation of the user."""
        return f"User: {self.user_name}"

    @classmethod
    def get_total(cls):
        """Return the total number of users created."""
        return cls.total_users

user1 = User("alice", "secret")
user2 = User("bob", "12345")
#user3 = User("bob", "qwe")

print(f"Total users: {user1.get_total()}",user1,sep="\n")
