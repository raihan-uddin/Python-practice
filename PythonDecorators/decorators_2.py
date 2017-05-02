# Functions within functions


def hello(name = "Raihan"):

    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return '\t This is inside the welcome() fucntion'


    if name == "Raihan":
        return greet
    else:
        return welcome

x = hello()
print(x)
# <function hello.<locals>.greet at 0x000001AA332EDE18>
print(x())
	 # This is inside the greet() function

