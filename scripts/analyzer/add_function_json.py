"""Parses existing json file to add what function mutants exist in."""

import json
import ast
import os


class FunctionVisitor(ast.NodeVisitor):
    def __init__(self):
        self.function_data = {}

    def visit_FunctionDef(self, node):
        function_name = node.name
        start_line = node.lineno
        # Try to get the last line of the function body
        if node.body:
            end_line = max(
                node.body[-1].end_lineno
                if hasattr(node.body[-1], "end_lineno")
                else node.body[-1].lineno,
                start_line,
            )
        else:
            end_line = start_line
        self.function_data[function_name] = {"start": start_line, "end": end_line}


def load_json_data(file_path):
    with open(file_path) as f:
        return json.load(f)


def parse_source_code(file_path):
    with open(file_path) as f:
        source_code = f.read()
    node = ast.parse(source_code, filename=file_path)
    visitor = FunctionVisitor()
    visitor.visit(node)
    return visitor.function_data


def match_patterns_to_functions(json_data, functions):
    for entry in json_data:
        lineno = int(entry["pattern"]["lineno"])  # Ensure lineno is an integer
        entry_file = entry["file"]
        for function, details in functions.items():
            start = int(details["start"])  # Ensure start is an integer
            end = int(details["end"])  # Ensure end is an integer, handle None case
            if start <= lineno <= (end or lineno):
<<<<<<< HEAD
                entry["function_name"] = function
                entry["function_start_line"] = start  # Add the function's start line
                break
        if "function_name" not in entry:
            entry["function_name"] = None  # or 'global scope' if you prefer
            entry["function_start_line"] = None
=======
                entry['function_name'] = function
                entry['function_scope'] = f"{start}-{end}"  # Add the function's start line
                break
        if 'function_name' not in entry:
            entry['function_name'] = None  # or 'global scope' if you prefer
            entry['function_scope'] = None
>>>>>>> 9b8123598ab3a654ddf0a729707bb395915cb86f


def process_directory(directory, json_data):
    for entry in json_data:
        file_path = entry["file"]
        relative_path = os.path.relpath(file_path, start=directory)
        full_path = os.path.join(directory, relative_path)
        if os.path.isfile(full_path):
            functions = parse_source_code(full_path)
            match_patterns_to_functions([entry], functions)


def save_output(data, output_file):
    with open(output_file, "w") as f:
        json.dump(data, f, indent=2)


def add_function_to_json(json_file, source_directory, output_file):
    data = load_json_data(json_file)
    process_directory(source_directory, data)
    save_output(data, output_file)

<<<<<<< HEAD

if __name__ == "__main__":
    json_input_file = "restructured_result.json"  # Path to your JSON input
    source_code_directory = "demo/lazytracker"  # Path to your source code directory
    json_output_file = "output_with_functions.json"  # Path to your JSON output
=======
if __name__ == '__main__':
    json_input_file = 'combined_result.json'  # Path to your JSON input
    source_code_directory = 'demo/lazytracker'    # Path to your source code directory
    json_output_file = 'output_with_functions.json'  # Path to your JSON output
>>>>>>> 9b8123598ab3a654ddf0a729707bb395915cb86f
    add_function_to_json(json_input_file, source_code_directory, json_output_file)
