
class Circle():
    def __init__(self, n:int = 10):
        self.radius = n

    def get_r(self):
        return self.radius

    def set_r(self, n:int = 10):
        self.radius = n

c = Circle(n=20)

print(c.get_r())

c.set_r(20)

print(c.get_r())
