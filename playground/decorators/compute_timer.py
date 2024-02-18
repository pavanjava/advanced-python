import time


def compute_timer(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        value = function(*args, **kwargs)
        end_time = time.time()
        print(f"INFO: time to execute {function.__name__} is {end_time - start_time} secs")
        return value
    return wrapper


@compute_timer
def compute_area(length, width):
    return length * width


compute_area(length=10, width=10)
