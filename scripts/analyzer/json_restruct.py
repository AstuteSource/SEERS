"""Danny's Approach to tidy Json data from both Chasten and Mutmut"""
import json

def restructure_json(chasten_data, mutmut_data):
    structured_data = []

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
            mutants = []
            for testcase in mutmut_data['testsuite'][0]['testcase']:
                if testcase['file'].endswith(source_file.split('/')[-1]) and testcase['line'] == pattern['lineno']:
                    mutant = {
                        'name': testcase['name'],
                        'line': testcase['line'],
                        'description': testcase['system-out'],
                        # Include failure information if present
                        'failure': testcase.get('failure')
                    }
                    mutants.append(mutant)

            structured_data.append({
                'file': source_file,
                'pattern': pattern,
                'mutants': mutants,
            })

    return structured_data

def main():
    with open('combined_result.json') as f:
        data = json.load(f)

    chasten_result = data['chasten_result']
    mutmut_result = data['mutmut_result']

    structured_result = restructure_json(chasten_result, mutmut_result)

    with open('restructured_result.json', 'w') as f:
        json.dump(structured_result, f, indent=2)

if __name__ == '__main__':
    main()
