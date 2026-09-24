"""
Created on Sun May 10 12:32:42 2020

@author: mjmacarty
"""


class User:

    def __init__(self, username=None, password=None,
                 email=None, birthday=None):
        self.username = username
        self.password = password
        self.email = email
        self.birthday = birthday

    def __str__(self):
        return f"Username: {self.username}\nPassword: {self.password}\
            \nEmail: {self.email}\nBirthday: {self.birthday}"

    def __repr__(self):
        return f"{self.__class__.__name__}{self.__dict__}"

user = User("John", 'password', 'john@some.com', '12/25/1999')
print(user.username)
print(user.password)
print(user)
print()
print(repr(user))
