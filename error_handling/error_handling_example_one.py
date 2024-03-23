print("start code")

try:
    dividend = int(input("Enter The dividend : "))
    divisor = int(input("Enter The divisor : "))
    message = f"The result of {dividend} / {divisor} = {dividend/ divisor}"
    file_open = open("example.txt", "r")
    content = file_open.read()
    age = int("old")
    print("File Contain : ", content)
    print(message)
except ZeroDivisionError as error:
    print("Error : ", error)
except FileNotFoundError as error:
    print("File Does Not EXIST")
except ValueError as error:
    print("Value Error")
except Exception as error:
    print("Unknown Error")
finally:
    print("I am always exicute wether there is error or not")


print("Last Code ...")