def mydecorator(function):
    def wrapper():
        function()
        print("This is a decorator")

    return wrapper


@mydecorator
def hello_world():
    print("Hello World")


hello_world()