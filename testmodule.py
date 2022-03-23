"""
This is a test module for Question 1
This module contains 5 functions

Source of test module: Alon Eshed
"""


def func1(param1: int, param2: dict[str, int]):
    """
    This function has two parameters
    """
    print("Hello")


def func2() -> list:
    """
    This function has no parameters and a return value.
    """
    return [1, 2, 3]


def func3(a: int, b: float, c, d: int) -> float:
    """
    This function has four parameters and a return value type float
    """
    return a + b + c + d


def func4(param1: list, param2: dict):
    """
    This function has two parameters
    """
    print("Func4")


def func5() -> dict:
    """
    This function has no parameters and a return value.
    """
    return {"a": 1, "b": 2, "c": 3}
