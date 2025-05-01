def greet_decoretor(func):
    def wrapper(*args, **kwargs):
        print("This Is Before Function Call")
        func()
        print("This Is After Function Call")
    return wrapper
@greet_decoretor
def greet():
    print("Hello There !!!")
    
greet()