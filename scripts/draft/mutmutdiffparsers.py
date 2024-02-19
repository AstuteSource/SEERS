import subprocess
import re

def parse_mutant_ids(output):
    # Matches numbers at the start of each line
    return re.findall(r'^\d+', output, re.MULTILINE)

def get_function_name_from_diff(diff):
    # Matches the 'def' keyword and captures the function name
    pattern = re.compile(r'^\+.*def (\w+)\(.*\):', re.MULTILINE)
    match = pattern.search(diff)
    if match:
        return match.group(1)
    else:
        return 'Unknown function'  # Default value if function name is not found

def main():
    # Get the list of all mutants from mutmut results
    result = subprocess.run(['mutmut', 'results'], capture_output=True, text=True)
    mutant_ids = parse_mutant_ids(result.stdout)

    mutants_by_function = {}
    killed_count = 0
    survived_count = 0

    # Get the diff for each mutant and organize by function
    for mutant_id in mutant_ids:
        diff = subprocess.run(['mutmut', 'show', str(mutant_id)], capture_output=True, text=True).stdout
        function_name = get_function_name_from_diff(diff)

        # Determine if the mutant was killed or survived
        if 'Survived' in diff:
            survived_count += 1
        elif 'Killed' in diff:
            killed_count += 1

        if function_name not in mutants_by_function:
            mutants_by_function[function_name] = []
        mutants_by_function[function_name].append((mutant_id, diff))

    # Write the organized mutants and summary to a file
    with open('mutants_by_function.txt', 'w') as file:
        file.write(f"Total Mutants Killed: {killed_count}\n")
        file.write(f"Total Mutants Survived: {survived_count}\n\n")
        
        for function, mutants in mutants_by_function.items():
            file.write(f"Function: {function}\n")
            for mutant_id, diff in mutants:
                status = 'Survived' if 'Survived' in diff else 'Killed'
                file.write(f"Mutant ID: {mutant_id} - {status}\nDiff:\n{diff}\n")
            file.write("\n")

if __name__ == "__main__":
    main()
