"""Program to execute and store Chasten and Mutmut analysis for lazytracker"""

import typer
import subprocess
#Resource: https://docs.python.org/3/library/subprocess.html
import json
import os
from pathlib import Path

cli = typer.Typer(no_args_is_help=True)

def install_package(package):
    """Install the specified Python package using pip."""
    subprocess.run(['pipx','install', package])

def check_installation(package)->bool:
    """Check if the specified Python package is installed."""
    try:
        subprocess.run([package, '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True )
        # I learned to use a PIPE with the subprocess module here: https://stackoverflow.com/questions/13332268/how-to-use-subprocess-command-with-pipes
    except subprocess.CalledProcessError:
        #  The package isn't installed, then return false: https://stackoverflow.com/questions/32942207/python-subprocess-calledprocesserror-command-returned-non-zero-exit-s
        return False
    return True

def execute_chasten(search_path, save_directory, save_file_path):
    """Execute the chasten analyze command for lazytracker."""
    # Resource: https://github.com/AstuteSource/chasten/tree/chastenversion
    # TODO: will be replaced by our antipattern checks
    chasten_config_path = os.getcwd() + '/chasten-configuration'
    # TODO: update to general use/take input
        
    chasten_command = [
        'chasten', 'analyze', 'lazytracker',
        '--config', chasten_config_path,
        '--search-path', search_path,
        '--save-directory', save_directory,
        '--save'
    ]

    try:
        subprocess.run(chasten_command, check=True)
    except subprocess.CalledProcessError:
        pass
    return save_file_path

def execute_mutmut(search_path):
    """Execute the mutmut run command."""
    mutmut_command = ['mutmut','run', '--paths-to-mutate', search_path]
    subprocess.run(mutmut_command,check=True)

def save_results(chasten_result, mutmut_result, save_file):
    """Save chasten and mutmut results in a JSON file"""
    result = {
        'chasten_result': chasten_result,
        'mutmut_result': mutmut_result
    }
    with open(save_file, 'w') as f:
        json.dump(result,f,indent=2).splitlines()
        # Need a custom pretty-print, so I learned from this resource: https://stackoverflow.com/questions/63949556/how-to-custom-indent-json-dump


if __name__ == "__main__":
    search_path: Path = os.getcwd() + '/lazytracker/subject-data',
    save_directory: Path = os.path.abspath(os.path.dirname(__file__)),
    #Step 1: Check and install chasten and mutmut if not installed
    # Save in the script's directory default
    save_file_path = os.path.join(save_directory, 'combined_result.json')

    if not check_installation('chasten'):
        install_package('chasten')

    if not check_installation('mutmut'):
        install_package('mutmut')

    #Step 2: Execute chasten and save the result
        chasten_result = execute_chasten(search_path, save_directory, save_file_path)

    #Step 3: Run mutmut and save its result
        mutmut_result = execute_mutmut(search_path)

    #Step 4: Save results in a file
        save_results(chasten_result,mutmut_result,'combined_result.json')
        print("Code analysis and mutation complete!")
        print("Result is stored in file name combined_result.json")


#@cli.command()
#def analyzer(
#    search_path: Path = os.getcwd() + '/lazytracker/subject-data',
#    save_directory: Path = os.path.abspath(os.path.dirname(__file__)),
#):
    #Step 1: Check and install chasten and mutmut if not installed
    # Save in the script's directory default
#    save_file_path = os.path.join(save_directory, 'combined_result.json')

#    if not check_installation('chasten'):
#        install_package('chasten')

 #   if not check_installation('mutmut'):
#        install_package('mutmut')

    #Step 2: Execute chasten and save the result
#        chasten_result = execute_chasten(search_path, save_directory, save_file_path)

    #Step 3: Run mutmut and save its result
#        mutmut_result = execute_mutmut(search_path)

    #Step 4: Save results in a file
#        save_results(chasten_result,mutmut_result,'combined_result.json')
#        print("Code analysis and mutation complete!")
#       print("Result is stored in file name combined_result.json")