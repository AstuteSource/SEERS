<img src="https://github.com/AstuteSource/SEERS/blob/cleanup/.github/images/comma-logo.svg" alt="Comma Logo"
    title="Comma" />

# 🧬 Comma

## 🎉 Introduction

## 🔋Features

## ⚡️ Requirements

- Python 3.11
- [Rich](https://github.com/Textualize/rich): Full-featured formatting and display of text in the terminal
- The developers of Comma use [Poetry](https://github.com/python-poetry/poetry) for packaging and dependency management

## 🔽 Installation

Follow these steps to install the `chasten` program:

- Install Python 3.11 for your operating system
- Clone this repo `git clone git@github.com:AstuteSource/SEERS.git`

# ✨ Analysis

- The `analyzer` folder currently contains our project.In order to run it, put desired projects to test on in the `demo` folder.
This can be done by navigating into the `demo` folder in a terminal and
running `git clone` for desired project repositories.

- Then, return to the `analyzer` folder and run `poetry install`.

- Once this is complete, the user can run `poetry run analyzer`, with optional parameters
for which path will be searched for a project, where the files will be saved, and where
the desired config files are. These are all `Path` objects, which can be passed in in a
manner resembling this command: 
`poetry run analyzer --search-path demo --save-directory subject-data --chasten-config-path Config`

- Once the analysis and unfication complete, the following message will pop up

```script
Code analysis and mutation complete!
Result is stored in file named combined_result.json
🧹 Final sweeping, saved to new_output_with_functions.json
```

The complete data exists in `new_output_with_functions.json`

- Now, you can scan the ouput to confirm that, for instance, the mutation score for pattern named `add_files` that was inserted 3 mutants (01 survived, 02 killed) has a mutation score of 0.3333333333333333.
  
```script
{
    "file": "/Users/jaclynpham/AstuteSource/SEERS/scripts/analyzer/demo/lazytracker/lazytracker/lazytracker.py",
    "pattern": {
      "lineno": 29,
      "coloffset": 4,
      "linematch": "def add_files(self, filepaths: List[str], chunk_num_blocks=128):",
      "context": "        files_to_check = sorted(files_to_check)\n\n        self.add_files(files_to_check, chunk_num_blocks)\n\n    def add_files(self, filepaths: List[str], chunk_num_blocks=128):\n        \"\"\"Include hash of files\n\n        Args:\n            filepaths (List[str]): List of paths to files\n            chunk_num_blocks (int, optional): How many chunks to read at once. Defaults to 128.",
      "min": 1,
      "max": 10,
      "pattern": ".//FunctionDef",
      "check_id": "F001",
      "check_name": "all-function-definition",
      "description": "Ensure the presence of function definitions in the codebase."
    },
    "function_name": "add_files",
    "function_scope": "29-42",
    "mutants": [
      {
        "name": "Mutant #6",
        "line": 29,
        "description": [
          "    def add_files(self, filepaths: List[str], chunk_num_blocks=128):"
        ],
        "failure": [
          {
            "inner": "--- lazytracker/lazytracker.py\n+++ lazytracker/lazytracker.py\n@@ -26,7 +26,7 @@\n \n         self.add_files(files_to_check, chunk_num_blocks)\n \n-    def add_files(self, filepaths: List[str], chunk_num_blocks=128):\n+    def add_files(self, filepaths: List[str], chunk_num_blocks=129):\n         \"\"\"Include hash of files\n \n         Args:\n",
            "type": "failure",
            "message": "bad_survived"
          }
        ]
      },
      {
        "name": "Mutant #7",
        "line": 38,
        "description": [
          "                with open(p, \"rb\") as f:"
        ],
        "failure": []
      },
      {
        "name": "Mutant #8",
        "line": 39,
        "description": [
          "                    while chunk := f.read(chunk_num_blocks * self._hasher.block_size):"
        ],
        "failure": []
      }
    ],
    "mutation_score": 0.3333333333333333
  },
```
