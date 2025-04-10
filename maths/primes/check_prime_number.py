import math


def check_one(value):
    if value <= 1:
        return False
    is_prime = True
    for i in range(2, value - 1):
        if value % i  == 0:
            is_prime = False
    return is_prime
def check_two(value):
    
    for i in range(2, int(math.sqrt(value)) + 1):
        if value % i == 0:
            return False
    return True and value > 1



print(check_two(11))