# Used the help of Alon Eshed through out the assignment

"""
Question 1 in Assignment 2.
This module gets a different module as a parameter and parses its
doc, functions, and function annotations into a HTML document
"""
from json.tool import main
import sys
import importlib

def validate_arguments():
    if len(sys.argv) != 3:
        error_message = "Wrong number of arguments to program! Try: doc_to_html.py module.py doc.html"
        raise RuntimeError(error_message)

def get_operands():
    module_name = sys.argv[1][0:-3]
    doc_name = sys.argv[2]
    module = importlib.import_module(module_name)
    return (module_name, module, doc_name)

def get_functions(module):
    module_attributes = [(name, type(getattr(module, name))) for name in dir(module)]
    functions = []
    for pair in module_attributes:
        if pair[1] == type(get_functions):
            functions.append(pair[0])
    return functions


def get_func_info(functions):
    info = ""
    for func_name in functions:
        func = getattr(module, func_name)
        info += f"<h1>Function {func_name}:</h1>\n"
        info += func.__doc__ + "\n"
        info += "<h3>Annotations:</h3>\n"
        annotations = str(func.__annotations__)
        annotations = annotations.replace("<", "")
        annotations = annotations.replace(">", "")
        info += annotations
    return info


if __name__ == '__main__':
    validate_arguments()
    module_name, module, doc_name = get_operands()
    functions = get_functions(module)

    prefix = "<html>\n<head>\n<title>\nDoc\n</title>\n</head>\n<body>"
    heading = f"<h1>Module {module_name}:</h1>"
    doc = module.__doc__
    functions_info = get_func_info(functions)
    suffix = "</body>\n</html>"
    
    html_content = prefix + '\n' + heading + '\n' + doc +'\n' + functions_info + '\n' + suffix

    with open(doc_name, 'w') as html:
        html.write(html_content)
