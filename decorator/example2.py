def add_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function : {wrapper.__name__}, Called With Arguments : {args}, {kwargs}")
        return func(kwargs["num1"], kwargs["num2"])
    return wrapper
    
@add_decorator
def add(num1, num2):
    return num1 + num2

print(add(num1 = 10, num2 = 20))