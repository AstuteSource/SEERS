<img src="https://github.com/AstuteSource/SEERS/blob/cleanup/.github/images/comma-logo.svg" alt="Comma Logo"
    title="Comma" />

# 🧬 Comma

[![Language](https://img.shields.io/badge/language-Python-blue.svg)](https://www.python.org/)
[![Chat](https://img.shields.io/badge/chat-on%20Discord-brightgreen)](https://discord.com/channels/877320365825749002/1204147098363232338)


## 🎉 Introduction

**Comma** is a custom tool developed as part of the Junior Seminar Research group project [SEERS](https://github.com/AstuteSource/SEERS/tree/main), focusing on the topic of empirically studying the relationship between code quality anti-patterns and mutation scores for Python projects.

**Comma** is designed to execute static analysis tools, notably [Chasten](https://github.com/AstuteSource/chasten/tree/master), and the mutation tool [Mutmut](https://github.com/boxed/mutmut) on selected subject programs. It identifies specific anti-patterns associated with low code quality, as collected from [Zhu et al.(2021)](https://www.sciencedirect.com/science/article/pii/S0164121220302545), and correlates them with mutation scores at the function level. Comma overcomes the limitation of per-line mutants returned by Mutmut by parsing the Abstract Syntax Tree (AST) of programs. Additionally, it unifies the output data from Chasten and Mutmut into a cohesive dataset, facilitating further analysis.
Comma aims to train and evaluate machine learning models to predict mutation scores based on code quality anti-patterns.

## 🔋Features

* ✨ Granular analysis of Python programs' abstract syntax trees (AST) for code quality anti-patterns
* 📊 Correlation of detected anti-patterns with mutation scores at the function level
* 🔄 Unification of output data from static analysis and mutation testing tools into a cohesive dataset
* 🔀 Seamless integration of result files from multiple runs of the tool for comprehensive analysis

## ⚡️ Requirements

- Python 3.11
- [Rich](https://github.com/Textualize/rich): Full-featured formatting and display of text in the terminal
- [Poetry](https://github.com/python-poetry/poetry): Packaging and dependency management

## 🔽 Installation

Follow these steps to install the `chasten` program:

- Install Python 3.11 for your operating system
- Clone this repository:  `git@github.com:AstuteSource/SEERS.git`

## ✨ Analysis

To analyze code using Comma:

1. Place the desired projects to test in the `demo` folder. Navigate into the `demo` folder in a terminal and use `git clone` to clone the desired project repositories.

2. Return to the `analyzer` folder and run the following command to install dependencies using Poetry `poetry install`

3. Once the installation is complete, execute the following command to run the analysis:

```bash
poetry run analyzer --search-path demo --save-directory subject-data --chasten-config-path Config

```

Replace the options --search-path, --save-directory, and --chasten-config-path with the desired paths where the project will be searched, files will be saved, and configuration files will be located, respectively. These should be Path objects passed in a manner similar to the example command provided above.

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

## 🧗Improvement

Found a bug or have a feature that the development team should implement? [Raise an issue!](https://github.com/AstuteSource/SEERS/issues)