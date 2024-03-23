class AgeError(Exception):
    def __init__(self,message = "Invalid Age", *args):
        self.message = message
        super().__init__(message, *args)


def check_age(age):
    if age < 0:
        raise AgeError("Age can not be negative")
    elif age > 120:
        print("Here")
        raise AgeError("Age can not greater than 120")
    
    else:
        print("Good age !!")


try:
    age = int(input("Enter Age..."))
    print(age)
    check_age(age)
except AgeError as error:
    print(error)
finally:
    print("All Time excuted")
    