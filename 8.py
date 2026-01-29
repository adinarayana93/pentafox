import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function '{func.__name__}' took {end - start:.4f} seconds to complete.")
        return result
    return wrapper


@time_it
def add_numbers(a, b):
    time.sleep(1)   # simulate delay
    return a + b


print(add_numbers(10, 20))
