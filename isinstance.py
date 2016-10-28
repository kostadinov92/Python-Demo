print(isinstance(1, int))


class Door:
    pass


class DerivedDoor(Door):
    pass

a = Door()
b = DerivedDoor()

print(isinstance(a, Door))
print(isinstance(a, DerivedDoor))

print(isinstance(b, Door))
print(isinstance(b, DerivedDoor))
