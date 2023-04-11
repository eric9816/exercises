
def func(a):
    print()
    for i in range(40,50):
        pass
    for i in range(a):
        yield i

a = func(10)

print(a)