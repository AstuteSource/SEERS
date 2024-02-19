"""Program to execute and store Chasten and Mutmut analysis"""

import subprocess
import json

def install_package(package):
    """Install the specified Python package using pip"""
    subprocess.run(['pip','install',package])

def check_installation(package)->bool:
    """Check if the specified Python package is installed"""
    try:
        subprocess.run([package, '--version'], stdout=subprocess.PIPE. stderr=subprocess.PIPE, check=True )
    except subprocess.CalledProcessError:
        return False
    return True