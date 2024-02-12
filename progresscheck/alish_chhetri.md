# Weekly Progress Checks

## Week 4

Week 4 goals: 

* Install all of the tools that we will use for this empirical study (e.g., python, poetry, pytest, chasten and mutmut although this might change)

* Find at least 3 to 5 subjects and fork them into the AstuteSource organization. Then, complete the following steps for each subject:

--> Confirming that python, poetry, pytest, chasten, and mutmut (likely these tools, not guaranteed) work for each of the subjects

--> Document the steps needed to get the subjects to work with each of these tools; perhaps simply editing the README.md for each project is sufficient?

* Pick a name for the tool that we are going to build and then create a repository for it in the AstuteSource organization

* Make sure that you are a owner/maintainer of the AstuteSource organization and the repositories inside of it

* Divide up the implementation tasks from the whiteboard pictures for the main tool that we are going to implement

Checks used for evaluating chasten on the subject programs:

```text
checks:
  - name: "all-function-definition"
    code: "FUNC"
    id: "FUNC001"
    description: "First executable line of a function, skipping over docstrings and/or comments"
    pattern: '//FunctionDef/body/Expr[value/Constant]/following-sibling::*[1] | //FunctionDef/body[not(Expr/value/Constant)]/*[1]'
  - name: "all-function-definition-with-docstring"
    code: "FUNC"
    id: "FUNC002"
    description: "First executable line of a function with a docstring, skipping over docstrings and/or comments"
    pattern: '//FunctionDef/body/Expr[value/Constant]/following-sibling::*[1]'
```

#### Subject Programs

- [Reflex](https://github.com/reflex-dev/reflex) 
    - Python 3.11, uses poetry, uses pytest
    - Chasten works with this program

- [Onionshare](https://github.com/onionshare/onionshare) 
    - Python 3.11, uses poetry, uses pytest
    - Chasten works with this program

- [Poetry](https://github.com/python-poetry/poetry)
    - Python, uses poetry, uses pytest
    - Chasten works with this program