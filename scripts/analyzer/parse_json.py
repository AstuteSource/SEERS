"""Script to parse the json to find what function each pattern is in"""

import ast

def find_containing_function(source, line_num):
    tree = ast.parse(source)
    
    class FunctionVisitor(ast.NodeVisitor):
        def __init__(self):
            self.nearest_function = None
            self.nearest_line = None
            
        def visit_FunctionDef(self, node):
            function_lines = (node.lineno, node.lineno + len(node.body))
            if function_lines[0] <= line_num <= function_lines[1]:
                self.nearest_function = node
                self.nearest_line = function_lines[0]
            elif self.nearest_function is None or abs(line_num - function_lines[0]) < abs(line_num - self.nearest_line):
                self.nearest_function = node
                self.nearest_line = function_lines[0]

    visitor = FunctionVisitor()
    visitor.visit(tree)
    
    if visitor.nearest_function is None:
        return None
        
    return visitor.nearest_function

def find_function():
    