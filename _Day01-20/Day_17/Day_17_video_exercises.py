class User:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
    
    def has_birthday(self):
        self.age += 1

user_1 = User("0001", "John", 40)
print(user_1.age)
user_1.has_birthday()
print(user_1.age)