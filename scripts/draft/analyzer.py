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