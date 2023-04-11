class Descriptor:
    def __set_name__(self, owner, name):
        print('__set_name_')
        self.name = "_" + name

    def __get__(self, instance, owner):
        print('__get__')
        return getattr(instance, self.name)
        # return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('__set__')
        setattr(instance, self.name, value)
        # instance.__dict__[self.name] = value

class A:

    x = Descriptor()
    y = Descriptor()
    z = Descriptor()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        print(self.x)

p = A(1,2,3)
print(p.__dict__)
