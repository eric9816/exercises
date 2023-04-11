class A:
    __obj = None

    def __new__(cls, *args, **kwargs):
        if cls.__obj is None:
            cls.__obj = True
            return super().__new__(cls)
        else:
            raise TypeError('Нельзя')

    def __init__(self, a):
        self.a = a


