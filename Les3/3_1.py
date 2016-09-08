def f(x, y, z):
    if type(x) == int and type(y) == int and type(z) == int:
        return x + y + z
    else:
        return 'alleen nummers'


print(f(1, 2, 3))
print(f('d',2.2, 2))