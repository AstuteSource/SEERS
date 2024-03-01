
# Scripts

This directory serves as the public workspace for creating scripts.

The goal of this directory is to create a script that can run the checks and collect patterns into a json file (ex. Run chasten for each program and save the output. Then run the mutation analysis, save it, and run our script to parse the files and convert it into a json file/an output)

The `analyzer` folder currently contains our project. 

In order to run it, put desired projects to test on in the `demo` folder.

Then, return to the `analyzer` folder and run `poetry install`.

Once this is complete, the user can run `poetry run analyzer`, with optional parameters
for which path will be searched for a project, where the files will be saved, and where
the desired config files are.
