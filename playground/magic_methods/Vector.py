"""
use of Dunder -> __ methods or otherwise called as magic methods.
the below class shows four different magic methods in which we show 'operator overloading', 'object destroying' and
'object representation'
"""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise Exception("Arguments should be vectors for the opration to be completed")
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"{self.x, self.y}"

    def __del__(self):
        print("object destroying")


if __name__ == "__main__":
    v1 = Vector(10, 20)
    v2 = Vector(30, 40)
    r = v1 + v2
    print(r)
