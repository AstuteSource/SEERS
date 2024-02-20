import subprocess
import os

subprocess.run(['mutmut','run'],stdout=subprocess.DEVNULL)
junit = subprocess.run(['mutmut','junitxml'],capture_output=True,text=True,check=True)
with open("mutation.xml", "x") as f:
	f.write(junit.stdout)

json = subprocess.run(['npx','junit2json','mutation.xml'],capture_output=True,text=True,check=True)
os.remove('mutation.xml')
with open("mutation.json", "x") as f:
	f.write(json.stdout)