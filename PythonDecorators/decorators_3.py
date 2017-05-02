# Function as Arguments!!!

'''def hello():
    return 'Hi raihan!'


def other(func):
    print('Other code goes here!')
    print(func())


print(other(hello))'''


def new_decorator(func):
    def wrap_func():
        print("Code here, before executing the func")

        func()

        print("Code here will executer after the func()")

    return wrap_func()


def func_needs_decorator():
    print("This function needs a decorator!")


# func_needs_decorator()
# This function needs a gecorator!

func_needs_decorator = new_decorator(func_needs_decorator)
print(func_needs_decorator)
# Code here, before executing the func
# This function needs a gecorator!
# Code here will executer after the func()

@new_decorator
def func_needs_decorator():
    print("This function needs a decorator!")

func_needs_decorator
# Code here, before executing the func
# This function needs a decorator!
# Code here will executer after the func()
