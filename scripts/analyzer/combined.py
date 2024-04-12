# import json
# import ast
# import os

# class FunctionVisitor(ast.NodeVisitor):
#     def __init__(self):
#         self.function_data = {}

#     def visit_FunctionDef(self, node):
#         function_name = node.name
#         start_line = node.lineno
#         if node.body:
#             end_line = max(node.body[-1].end_lineno if hasattr(node.body[-1], 'end_lineno') else node.body[-1].lineno, start_line)
#         else:
#             end_line = start_line
#         self.function_data[function_name] = {'start': start_line, 'end': end_line}

# def load_json_data(file_path):
#     with open(file_path) as f:
#         return json.load(f)

# def parse_source_code(file_path):
#     with open(file_path) as f:
#         source_code = f.read()
#     node = ast.parse(source_code, filename=file_path)
#     visitor = FunctionVisitor()
#     visitor.visit(node)
#     return visitor.function_data

# def calculate_mutation_score(mutants):
#     if len(mutants) == 0:
#         return None
#     else:
#         failures = sum(1 for m in mutants if m.get('failure'))
#         total = len(mutants)
#         return ((total-failures) / total if total > 0 else 0)*100

# def restructure_and_add_function_info(combined_data, source_directory):
#     structured_data = []

#     # Process Chasten results
#     for source in combined_data['chasten_result']['sources']:
#         source_file = source['filename']
#         functions = parse_source_code(os.path.join(source_directory, source_file))
#         check = source['check']  # 'check' is a dictionary

#         for match in check['matches']:
#             pattern = check.get('pattern')
#             check_id =  check.get('id'),
#             pattern_details = {
#                 # ... pattern details as before ...
#                 'lineno': match['lineno'],
#                 'coloffset': match['coloffset'],
#                 'linematch': match['linematch'],
#                 'context': match['linematch_context'],
#                 'min': check.get('min'),
#                 'max': check.get('max'),
#                 'check_name': check.get('name'),
#                 'description': check.get('description'),
#             }
#             lineno = match['lineno']
#             function_name, function_scope = None, None
#             for func_name, details in functions.items():
#                 if details['start'] <= lineno <= details['end']:
#                     function_name = func_name
#                     function_scope = f"{details['start']}-{details['end']}"
#                     break

#             # Find corresponding mutmut mutants
#             mutants = []
#             for testcase in combined_data['mutmut_result']['testsuite'][0]['testcase']:
#                 if testcase['file'].endswith(source_file.split('/')[-1]):
#                     if function_scope and details['start'] <= testcase['line'] <= details['end']:
#                         # Mutant is within the function scope
#                         mutants.append({
#                             'name': testcase['name'],
#                             'line': testcase['line'],
#                             'description': testcase.get('system-out', []),
#                             'failure': testcase.get('failure', [])
#                         })
#             # Calculate mutation score for the current function's scope
#             mutation_score = calculate_mutation_score(mutants)

#             structured_data.append({
#                 'file': source_file,
#                 'pattern': pattern,
#                 'check_id': check_id,
#                 'pattern_detailes': pattern_details,
#                 'function_name': function_name,
#                 'function_scope': function_scope,
#                 'mutants': mutants,
#                 'mutation_score': mutation_score,
#             })

#     return structured_data

# def save_output(data, output_file):
#     with open(output_file, 'w') as f:
#         json.dump(data, f, indent=2)

# if __name__ == '__main__':
#     json_input_file = 'combined_result.json'
#     source_code_directory = 'demo/lazytracker'
#     json_output_file = 'new_output_with_functions.json'

#     combined_data = load_json_data(json_input_file)
#     structured_data = restructure_and_add_function_info(combined_data, source_code_directory)
#     save_output(structured_data, json_output_file)



import json
import ast
import os

class FunctionVisitor(ast.NodeVisitor):
    def __init__(self):
        self.function_data = {}

    def visit_FunctionDef(self, node):
        function_name = node.name
        start_line = node.lineno
        if node.body:
            end_line = max(node.body[-1].end_lineno if hasattr(node.body[-1], 'end_lineno') else node.body[-1].lineno, start_line)
        else:
            end_line = start_line
        self.function_data[function_name] = {'start': start_line, 'end': end_line}

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

def calculate_mutation_score(mutants):
    if len(mutants) == 0:
        return None
    else:
        failures = sum(1 for m in mutants if m.get('failure'))
        total = len(mutants)
        return ((total-failures) / total if total > 0 else 0)*100

def restructure_and_add_function_info(combined_data, source_directory):
    # This will hold the final structured data
    structured_data = []

    # Map function names to their details including associated patterns and mutants
    function_map = {}

    # Parse each file's AST once and store the results
    ast_cache = {}

    # Process each source file
    for source in combined_data['chasten_result']['sources']:
        source_file = source['filename']
        relative_file_path = os.path.join(source_directory, source_file)

        # Use cached AST parse results if available
        if relative_file_path in ast_cache:
            functions = ast_cache[relative_file_path]
        else:
            functions = parse_source_code(relative_file_path)
            ast_cache[relative_file_path] = functions

        # Associate Chasten patterns with functions
        for pattern in source['check']['matches']:
            lineno = pattern['lineno']
            for func_name, func_details in functions.items():
                if func_details['start'] <= lineno <= func_details['end']:
                    if func_name not in function_map:
                        function_map[func_name] = {
                            'function_name': func_name,
                            'function_scope': f"{func_details['start']}-{func_details['end']}",
                            'patterns': [],
                            'mutants': []
                        }
                    function_map[func_name]['patterns'].append(pattern)
                    break

    # Associate Mutmut mutants with functions
    for mutant in combined_data['mutmut_result']['testsuite'][0]['testcase']:
        mutant_file = mutant['file']
        mutant_line = mutant['line']
        for func_data in function_map.values():
            start, end = map(int, func_data['function_scope'].split('-'))
            if mutant_file.endswith(source_file.split('/')[-1]) and start <= mutant_line <= end:
                func_data['mutants'].append(mutant)

    # Calculate mutation scores and construct the final structured data
    for func_name, func_data in function_map.items():
        mutation_score = calculate_mutation_score(func_data['mutants'])
        structured_data.append({
            'function_name': func_name,
            'function_scope': func_data['function_scope'],
            'patterns': func_data['patterns'],
            'mutants': func_data['mutants'],
            'mutation_score': mutation_score
        })

    return structured_data

def save_output(data, output_file):
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    json_input_file = 'combined_result.json'
    source_code_directory = 'demo/lazytracker'
    json_output_file = 'new_output_with_functions.json'

    combined_data = load_json_data(json_input_file)
    structured_data = restructure_and_add_function_info(combined_data, source_code_directory)
    save_output(structured_data, json_output_file)


            # Find corresponding mutmut mutants
    #         mutants = []
    #         for testcase in combined_data['mutmut_result']['testsuite'][0]['testcase']:
    #             if testcase['file'].endswith(source_file.split('/')[-1]):
    #                 if function_scope and details['start'] <= testcase['line'] <= details['end']:
    #                     # Mutant is within the function scope
    #                     mutants.append({
    #                         'name': testcase['name'],
    #                         'line': testcase['line'],
    #                         'description': testcase.get('system-out', []),
    #                         'failure': testcase.get('failure', [])
    #                     })
    #         # Calculate mutation score for the current function's scope
    #         mutation_score = calculate_mutation_score(mutants)

    #         structured_data.append({
    #             'file': source_file,
    #             'pattern': pattern,
    #             'check_id': check_id,
    #             'pattern_detailes': pattern_details,
    #             'function_name': function_name,
    #             'function_scope': function_scope,
    #             'mutants': mutants,
    #             'mutation_score': mutation_score,
    #         })

    # return structured_data