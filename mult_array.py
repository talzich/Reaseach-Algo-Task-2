"""
Question 3 in Assignment 2.
This module gets a different module as a parameter and parses its
doc, functions, and function annotations into a HTML document
"""
class List(list):
    
    def __getitem__(self, key):
        if isinstance(key, int):
            return super().__getitem__(key)
        if len(key) == 1:
            return super().__getitem__(key[0])
        return List(super().__getitem__(key[0]))[key[1:]]