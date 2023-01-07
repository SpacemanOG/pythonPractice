# problem 1
def myFunc(x):
    return x ** 2


print(myFunc(15))

# problem 2
# a function that accepts a string as a param and prints it


def myFunc2(stringParam):
    print(str(stringParam))


myFunc2("Hello")

# problem 3
# a function with three required params and two optional params


def myFunc3(a, b, c, d=5, e=10):
    return a + b + c + d + e


print(myFunc3(5, 5, 5))


# problem 4
def func1of2(x):
    return x / 2


result_func1 = int(func1of2(10))


def func2of2(y):
    return y * 4


print(func2of2(result_func1))

# problem 5
"""
This is called a DOCSTRING comment
"""


def convertString2Float(string):
    try:
        print(float(string))
    except ValueError:
        print("Provide a number")


convertString2Float("Hello")
