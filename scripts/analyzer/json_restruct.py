"""Tidy Json data from both Chasten and Mutmut and store in a new file."""

import json

def restructure_json(chasten_data, mutmut_data):
    structured_data = []

    # Calculate the mutation score, handling division by zero if there are no tests and failures
    total_mutants = mutmut_data.get("tests", 0) + mutmut_data.get("failures", 0)
    score = mutmut_data.get("failures", 0) / total_mutants if total_mutants > 0 else 0

   
    # Extract the summary from mutmut_data
    mutmut_summary = {
        "disabled": mutmut_data.get("disabled", 0),
        "errors": mutmut_data.get("errors", 0),
        "failures": mutmut_data.get("failures", 0),
        "tests": mutmut_data.get("tests", 0),
        "time": mutmut_data.get("time", 0),
        "score": score  # Add the calculated score
    }

    # Process Chasten results
    for source in chasten_data['sources']:
        source_file = source['filename']
        check = source['check']  # Assuming there is only one check per source
        for match in check['matches']:
            pattern = {
                'lineno': match['lineno'],
                'coloffset': match['coloffset'],
                'linematch': match['linematch'],
                'context': match['linematch_context'],
                # Include additional fields
                'min': check.get('min'),
                'max': check.get('max'),
                'pattern': check.get('pattern'),
                'check_id': check.get('id'),
                'check_name': check.get('name'),
                'description': check.get('description'),
            }
            # Find corresponding mutmut mutants
            mutants = {}
            for testcase in mutmut_data['testsuite'][0]['testcase']:
                if testcase['file'].endswith(source_file.split('/')[-1]) and testcase['line'] == pattern['lineno']:
                    mutant_name = testcase['name']
                    mutants[mutant_name] = {
                        'line': testcase['line'],
                        'description': testcase['system-out'][0] if testcase['system-out'] else "",
                        # Include failure information if present
                        'failure': testcase.get('failure', [{}])[0]
                    }

            structured_data.append({
                'file': source_file,
                'pattern': pattern,
                'mutants':mutants if mutants else None,  # Set to "NULL" if no mutants
                'mutmut_summary': mutmut_summary # Add the summary to each entry
            })

    return structured_data


def json_restruct():
    with open('combined_result.json') as f:
        # load in data
        data = json.load(f)

    chasten_result = data['chasten_result']
    mutmut_result = data['mutmut_result']

    structured_result = restructure_json(chasten_result, mutmut_result)

    with open('restructured_result.json', 'w') as f:
        # rewrite results json
        json.dump(structured_result, f, indent=2)

if __name__ == '__main__':
    json_restruct()
