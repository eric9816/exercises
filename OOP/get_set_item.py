class A:
    def __init__(self, x, marks):
        self.x = x
        self.lst = list(marks)

    def __getitem__(self, item):
        return self.lst[item]

    def __setitem__(self, key, value):
        self.lst[key] = value

a = A(1, [6,2,3])
a[2] = 100
print(a.__dict__)