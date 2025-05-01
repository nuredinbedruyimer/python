import time

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("The args : ", *args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timing
def slow_function(name):
    time.sleep(1)
    print("Finished slow function")

slow_function()
