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
- name: "nested-if-statements"
  code: "IFIF"
  id: "NESTEDIF001"
  description: "Detects nested 'if' statements"
  pattern: '//If/If'

- name: "print-instead-of-return"
  code: "PIR"
  id: "OUTPUT001"
  description: "Detects 'print' statements inside functions instead of 'return'"
  pattern: '//FunctionDef[body//Call[func/Name/@id="print"]][not(.//Return)]'
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