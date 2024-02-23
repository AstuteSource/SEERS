# Project Name: Empirically Studying the Relationship between Code Quality Anti-Patterns and Mutation Score for Python Projects

### Name: Daniel Bekele 
#### Github: Danniyb 
#### Discord: crakingdani

### Logs 
##### Wednesday febuary 7, 2024 
        - Installing chasten and running it.
        - Installing Mutmut
        - Looking for examplery project to use. Confirming that python, poetry, pytest, chasten, and mutmut (likely these tools, not guaranteed) work for each of the subjects. Documenting the steps needed to get the subjects to work with each of these tools; perhaps simply editing the README.md for each project is sufficient
        - exampler project 
                - https://github.com/Danniyb/cookiecutter-poetry
                - https://github.com/Danniyb/sidewinder
                - https://github.com/UltiRequiem/python-playground
##### Wednesday Febuary 21, 2024
        - Tried to create a tool that can hopefully parse the output from `mutmut`.
        - The `mutmutdiffparsers.py` is a code that runs mutation testing using the mutmut tool and organizes the results by function. It
        first retrieves the list of all mutant IDs from mutmut results, then for each mutant, it gets the diff (the changes made by the
        mutation) and determines the function name where the mutation occurred. It also counts how many mutants were killed and how many
        survived. Finally, it writes a summary of the results, including the total counts and the details of each mutant organized by
        function, to a file named mutants_by_function.txt
        `runningTools.py` 
        - This code runs two separate commands using the subprocess module in Python:
        `run_mutpy():`
        - It executes the mut.py command with specific arguments (--target, --unit-test, and --show-mutants).
        The output of this command is redirected to a file named mutated_code.txt, which is created or overwritten in the current
        directory.
        `run_chasten():`
        - It runs the chasten command with a series of arguments to analyze mutation counters.
        - The output of the chasten command is appended to the same mutated_code.txt file, following the output from mut.py.
        - The main() function calls both of these functions in sequence, ensuring that mut.py is run first and its output is saved,
        followed by the execution of chasten with its output appended to the same file.
