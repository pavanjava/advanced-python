def method_logger(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        print(f"INFO: executed function: {function.__name__}, args : {args}, kwargs: {kwargs}")
        return value

    return wrapper


@method_logger
def compute_area(length, width):
    return length * width


print(compute_area(length=5, width=5))
