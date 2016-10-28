class Executor:
    def __init__(self, function):
        self.function = function

    def execute(self):
        self.function()


def function_to_pass():
    print("I am passed to the executor.")


executor = Executor(function_to_pass)
executor.execute()
