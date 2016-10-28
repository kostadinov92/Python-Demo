class Singleton(type):
    instance = None

    def __call__(cls, *args, **kwargs):  # by convention instead of 'self' we use 'cls' as an instance argument
        if not cls.instance:
            cls.instance = super(Singleton, cls).__call__(*args, *kwargs)
        return cls.instance


# now we define a class that uses Singleton as a metaclass


class ASingleton(metaclass=Singleton):
    pass

a = ASingleton()
b = ASingleton()

print(a is b)  # true

print(hex(id(a)))  # same ref
print(hex(id(b)))  # same ref
