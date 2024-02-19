import subprocess

def run_mutpy():
    # Run the mut.py command and redirect its output to mutated_code.txt
    mutpy_command = [
        'mut.py', '--target', 'ultiplayground', '--unit-test', 'tests', '--show-mutants'
    ]
    with open('mutated_code.txt', 'w') as file:
        subprocess.run(mutpy_command, stdout=file, stderr=subprocess.STDOUT)

def run_chasten():
    # Run the chasten command and append its output to mutated_code.txt
    chasten_command = [
        'chasten', 'analyze', 'multicounter',
        '--config', '/Users/danielbekele/jsem/chasten-configuration',
        '--search-path', '/Users/danielbekele/jsem/subject-data/python-playground',
        '--save-directory', '/Users/danielbekele/jsem/subject-data/python-playground',
        '--save',
        '--verbose'
    ]
    with open('mutated_code.txt', 'a') as file:
        subprocess.run(chasten_command, stdout=file, stderr=subprocess.STDOUT)

def main():
    run_mutpy()
    run_chasten()

if __name__ == '__main__':
    main()
