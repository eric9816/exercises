class A:
    MIN = 1
    def __init__(self, a):
        self.a = a
        self.func(10)

    @staticmethod
    def func(self):
        print(self)

b = A(5)
b.func(10)