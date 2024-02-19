"""Program to execute and store Chasten and Mutmut analysis for lazytracker"""

import subprocess
import json

def install_package(package):
    """Install the specified Python package using pip."""
    subprocess.run(['pip','install',package])

def check_installation(package)->bool:
    """Check if the specified Python package is installed."""
    try:
        subprocess.run([package, '--version'], stdout=subprocess.PIPE. stderr=subprocess.PIPE, check=True )
    except subprocess.CalledProcessError:
        return False
    return True

def execute_chasten():
    """Execute the chasten analyze command for lazytracker."""
    chasten_command = [
        'chasten', 'analyze', 'lazytracker',
        '--config', '<path to the chasten-configuration/ directory>',
        '--search-path', '<path to the lazytracker/ directory>',
        '--save-directory', '<path to the subject-data/lazytracker/ directory>',
        '--save'
    ]
    subprocess.run(chasten_command, check=True)

def execute_mutmut():
    """Execute the mutmut run command."""
    mutmut_command = ['mutmut','run']
    subprocess.run(mutmut_command,check=True)

def save_results(chasten_result, mutmut_result, save_file):
    """Save chasten and mutmut results in a JSON file"""
    result = {
        'chasten_result': chasten_result,
        'mutmut_result': mutmut_result
    }
    with open(save_file, 'w') as f:
        json.dump(result,f,indent=2) 

if __name__=="__main__":
    #Step 1: Check and install chasten and mutmut if not installed
    if not check_installation('chasten'):
        install_package('chasten')

    if not check_installation('mutmut'):
        install_package('mutmut')

    #Step 2: Execute chasten and save the result
        chasten_result = execute_chasten()

    #Step 3: Run mutmut and save its result
        mutmut_result = execute_mutmut()

    #Step 4: Save results in a file
        save_results(chasten_result,mutmut_result,'combined_result.json')
        print("Code analysis and mutation complete!")
        print("Result is stored in file name combined_result.json")