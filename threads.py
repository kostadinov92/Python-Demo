import threading


def func_to_be_exec(*args, **kwargs):
    for i in args:
        print(i)
    for i in kwargs.items():
        print(i)


t = threading.Thread(target=func_to_be_exec, args=(1, 2, 3))
t.daemon = True
t.start()
