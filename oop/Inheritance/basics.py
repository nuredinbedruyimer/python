class Parent:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        
    
        
    def greet(self):
        greeting_message = f"Hello, {self.name} Welcome to this website you loged in using {self.email}"
        
        print(greeting_message)
        
        
class Child(Parent):
    def __init__(self, name , email, password, hobby):
        super().__init__(name, email, password)
        self.hobby = hobby
    def greet(self):
        greeting_message = f"Hello, {self.name} Welcome to this website you loged in using {self.email} and my hobby is {self.hobby}"
        print(greeting_message)


child_one = Child("Nuredin", "example@gmail.com", "123445", "Watching Anime")


child_one.greet()
        