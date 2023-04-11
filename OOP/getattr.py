from dataclasses import dataclass
class Lst:

    def __init__(self, x):
        self.x = x

    def __getattribute__(self, item):
        print('__getattribute__')
        if item == 'z':
            raise AttributeError('getattribute: Z недопустимо!')
        else:
            object.__getattribute__(self, item)
            #return super().__getattribute__(item)


    def __getattr__(self, item):
        print('__getattr__')
        if item == 'z':
            print('Ладно, ошибку не выведу, но верну False...')
            return False


    def __setattr__(self, key, value):
        print('__setattr__')
        if key == 'z':
            # raise AttributeError('setattr: Y недопустимо!')
            raise AttributeError('setattr: Не, но менять я уж тебе не дам, сорри')
        else:
            object.__setattr__(self, key, value)

a = Lst(1)
print(a.z)
#print(a.y)
#print(a.__dict__)