class A:
    def __init__(self, num):
        self.num = num

    def __add__(self, other: 'A') -> 'A':
        return A(self.num + other.num)

a = A(2)
b = A(5)
c = a + b
print()