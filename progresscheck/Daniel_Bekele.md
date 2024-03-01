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

##### Wednesday Febuary 14, 2024
        - Divide up work to two team for analysising anti patterns for python and another team to work on a script that will run all the tool we are using to create a unified json with all there output. 
        - Started testing a new tool for mututation test `Mutatest`
        - switched out subject python program due to finding out that the test cases were written poorly
        New Projects
                - https://github.com/Danniyb/fastapi_quickstart
                - https://github.com/UltiRequiem/python-playground
                - https://github.com/timhughes/cookiecutter-poetry

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

##### Wednesday Febuary 28, 2024
        - I have been trying to restructure the json that is created by running analyzer, if you look in the seers repo for a jsonRestrut branch you
        should find a python script that does the following
        - The script provided operates by parsing two sets of JSON data—one from the chasten tool and the other from mutmut. It then restructures
        this data into a new format that aligns related information from both tools by their location within the codebase.
        - I wrote another program that was able to take in the old json file to include what function each pattern is in and the line where the
        fucntion starts. This json file is what is produced from the orginal script I wrote. This step involes using the python ast library to find
        the nodes each line exist in to identify what the function it is inclosed in. 
        -  I have been working on the Json_restruct.py to meet the new requirement for the ML team. Caleb Kendra mentioned to me that the json
        structure was faulty, the first thing was mutants were stored in a list but that was causing issues while the ML team was trying to get it
        to a panda data frame. I changed it to a dict to fix this. Next thing was the mutation score was not being included in the reconstructed
        json from the original json. Lastly was making sure that when there was no mutant in a given pattern to return a null value.
