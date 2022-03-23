"""
Question 2 in Assignment 2.
This module defines and demonstrates the lastcall decorator
"""

# Saves calls and arguments
func_args = {}

def lastcall(func):
    def innerfunction(arg):
        result = func(arg)
        func_never_called = not func.__name__ in func_args
        if func_never_called or func_args[func.__name__][0] != arg:
            print(result)
            func_args[func.__name__] = (arg, result)
        else:
            print(f"Saved result: {func_args[func.__name__][1]}")
        return result
    return innerfunction


if __name__ == '__main__':
    @lastcall
    def square(x: int):
        return x**2

    @lastcall
    def cube(x: int):
        return x**3

    @lastcall
    def mul_by_3(x: int):
        return x*3

    @lastcall
    def zero(x: int):
        return 0


    square(2)
    square(2)
    square(2)
    square(3)
    square(3)
    cube(3)
    square(3)
    square(3)
    mul_by_3(10)
    mul_by_3(11)
    mul_by_3(11)
    zero(2)
    zero(2)
    zero(2)
    zero(2)
    zero(3)
    zero(3)
    zero(4)
    zero(4)
