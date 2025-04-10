def get_prime_factorizations(value):
    if value <= 1:
        return []
    arr = []
    for curr_value in range(2, value):
        if value % curr_value == 0:
            occ = 0
            while value % curr_value == 0:
                occ += 1
                value //= curr_value
            
            arr.append((curr_value, occ))
            
    return arr


print(get_prime_factorizations(24))
                