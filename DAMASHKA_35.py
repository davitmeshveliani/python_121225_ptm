"""
This module defines the User class with validation and counter.
"""
class User:
    """Class representing a user with name and password validation """
    total_users = 0

    def __init__(self, user_name, password):

        """Initialize user and validate data."""

        if not user_name:
            raise ValueError("Invalid name")

        if len(password) < 5:
            raise ValueError(f"Invalid password: '{password}'")

        self.user_name = user_name
        self.password = password
        User.total_users += 1

    def __str__(self):
        """Return a string representation of the user."""
        return f"User: {self.user_name}"

    def get_total(self):
        """Return the total number of users created."""
        return User.total_users

user1 = User("alice", "secret")
user2 = User("bob", "123456")

#print(f"Total users: {user1.get_total()}",user1,sep="\n")
#user3 = User("bob", "qwe")
