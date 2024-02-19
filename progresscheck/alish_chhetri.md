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


    Chasten Results

    ```text
    💫 chasten: Analyze the AST of Python Source Code
    🔗 GitHub: https://github.com/gkapfham/chasten

    ✨ Configuration directory: /home/student/juniorsem/test-ground/chasten-configuration

    ✨ Validated /home/student/juniorsem/test-ground/chasten-configuration? Yes
    ✨ Validated /home/student/juniorsem/test-ground/chasten-configuration/checks.yml? Yes

    ✨ Analyzing Python source code in: /home/student/juniorsem/test-ground/reflex

    🎉 Performing 2 check(s):

    ✓ id: 'NESTEDIF001', name: 'nested-if-statements', pattern: '//If/If', min=None, max=None
    = 0 total matches

    ✓ id: 'OUTPUT001', name: 'print-instead-of-return', pattern: '//FunctionDef[body//Call[func/Name/@id="print"]][not(.//Return)]', min=None, max=None
        • /home/student/juniorsem/test-ground/reflex/scripts/wait_for_listening_port.py - 1 matches
        • /home/student/juniorsem/test-ground/reflex/reflex/testing.py - 2 matches
        • /home/student/juniorsem/test-ground/reflex/reflex/utils/console.py - 6 matches
        • /home/student/juniorsem/test-ground/reflex/reflex/utils/prerequisites.py - 1 matches
        • /home/student/juniorsem/test-ground/reflex/integration/benchmarks/test_compile_benchmark.py - 1 matches
    = 11 total matches

    💻 0 / 0 checks passed (0.0%)


    😂 All checks passed. Elapsed Time: 10.317962169647217 seconds
    ```

- [Onionshare](https://github.com/onionshare/onionshare) 
    - Python 3.11, uses poetry, uses pytest
    - Chasten works with this program

    Chasten Results

    ```text
    💫 chasten: Analyze the AST of Python Source Code
    🔗 GitHub: https://github.com/gkapfham/chasten

    ✨ Configuration directory: /home/student/juniorsem/test-ground/chasten-configuration

    ✨ Validated /home/student/juniorsem/test-ground/chasten-configuration? Yes
    ✨ Validated /home/student/juniorsem/test-ground/chasten-configuration/checks.yml? Yes

    ✨ Analyzing Python source code in: /home/student/juniorsem/test-ground/onionshare

    🎉 Performing 2 check(s):

    ✓ id: 'NESTEDIF001', name: 'nested-if-statements', pattern: '//If/If', min=None, max=None
    = 0 total matches

    ✓ id: 'OUTPUT001', name: 'print-instead-of-return', pattern: '//FunctionDef[body//Call[func/Name/@id="print"]][not(.//Return)]', min=None, max=None
        • /home/student/juniorsem/test-ground/onionshare/desktop/scripts/macos-merge-universal.py - 1 matches
        • /home/student/juniorsem/test-ground/onionshare/desktop/scripts/get-tor.py - 4 matches
        • /home/student/juniorsem/test-ground/onionshare/desktop/scripts/macos-check-arch.py - 1 matches
        • /home/student/juniorsem/test-ground/onionshare/desktop/scripts/build-macos.py - 3 matches
        • /home/student/juniorsem/test-ground/onionshare/desktop/scripts/build-windows.py - 3 matches
        • /home/student/juniorsem/test-ground/onionshare/desktop/onionshare/connection_tab.py - 1 matches
        • /home/student/juniorsem/test-ground/onionshare/desktop/onionshare/__init__.py - 1 matches
        • /home/student/juniorsem/test-ground/onionshare/flatpak/poetry-to-requirements.py - 1 matches
        • /home/student/juniorsem/test-ground/onionshare/cli/onionshare_cli/__init__.py - 1 matches
        • /home/student/juniorsem/test-ground/onionshare/cli/onionshare_cli/common.py - 2 matches
        • /home/student/juniorsem/test-ground/onionshare/cli/onionshare_cli/onion.py - 1 matches
        • /home/student/juniorsem/test-ground/onionshare/cli/onionshare_cli/web/share_mode.py - 1 matches
        • /home/student/juniorsem/test-ground/onionshare/cli/onionshare_cli/web/receive_mode.py - 1 matches
    = 21 total matches

    💻 0 / 0 checks passed (0.0%)


    😂 All checks passed. Elapsed Time: 5.572923183441162 seconds
    ```

- [Poetry](https://github.com/python-poetry/poetry)
    - Python, uses poetry, uses pytest
    - Chasten works with this program

    Chasten Results
    
    ```text
    💫 chasten: Analyze the AST of Python Source Code
    🔗 GitHub: https://github.com/gkapfham/chasten

    ✨ Configuration directory: /home/student/juniorsem/test-ground/chasten-configuration

    ✨ Validated /home/student/juniorsem/test-ground/chasten-configuration? Yes
    ✨ Validated /home/student/juniorsem/test-ground/chasten-configuration/checks.yml? Yes

    ✨ Analyzing Python source code in: /home/student/juniorsem/test-ground/poetry

    🎉 Performing 2 check(s):

    ✓ id: 'NESTEDIF001', name: 'nested-if-statements', pattern: '//If/If', min=None, max=None
    = 0 total matches

    ✓ id: 'OUTPUT001', name: 'print-instead-of-return', pattern: '//FunctionDef[body//Call[func/Name/@id="print"]][not(.//Return)]', min=None, max=None
        • /home/student/juniorsem/test-ground/poetry/tests/packages/test_locker.py - 1 matches
        • /home/student/juniorsem/test-ground/poetry/tests/utils/fixtures/setups/sqlalchemy/setup.py - 1 matches
    = 2 total matches

    💻 0 / 0 checks passed (0.0%)


    😂 All checks passed. Elapsed Time: 14.058250904083252 seconds
    ```


## Week 5

Table 5 from Zhu:

| #   | Name                 | Definition                                                                                  |
|-----|----------------------|---------------------------------------------------------------------------------------------|
| 1   | is_void              | Whether the return value of the method is void or not                                       |
| 2   | non_void_percent     | (class-level) The percent of non-void methods in the class                                   |
| 3   | getter_percentage    | The percentage of getter methods in the class                                               |
| 4   | is_public            | Whether the method is public or not                                                         |
| 5   | is_static            | Whether the method is static or not                                                         |
| 6   | is_nested            | (class-level) Whether the method is located in a nested class or not                         |
| 7   | nested_depth         | The maximum number of nested depth (MDN from Section 2.2)                                    |
| 8   | (cond)               | The number of conditions (if, if-else and switch) in the method                              |
| 9   | (cond(cond))         | The number of nested conditions (e.g.,if{if{}}) in the method                                |
| 10  | (cond(loop))         | The number of nested condition-loops (e.g.,if{for{}}) in the method                           |
| 11  | (loop)               | The number of loops (for, while and do-while) in the method (LOOP from Section 2.2)          |
| 12  | (loop(cond))         | The number of nested loop-conditions (e.g.,for{if{}}) in the method.                          |
| 13  | (loop(loop))         | The number of nested loop-conditions (e.g.,for{for{}}) in the method.                         |
| 14  | method_length        | The number of lines of code in the method (NLOC from Section 2.2)                             |
| 15  | direct_test_no.      | The number of test methods directly invoking the method under test (production code)         |
| 16  | test_distance        | The shortest method call sequence required to invoke the method (production code) by test methods |
| 17  | assertion_no.        | The number of assertions in direct tests                                                   |
| 18  | assertion-McCabe_Ratio | The ratio between the total number of assertions in direct tests and the McCabe Cyclomatic complexity |
| 19  | assertion_density    | The ratio between the total number of assertions in direct tests and the lines |


My anti-pattern table:

| #   | Name                           | Definition                                                                                          |
|-----|--------------------------------|-----------------------------------------------------------------------------------------------------|
| 1   | wildcard imports               | An import statement in the pattern of `import MODULE from *`                                        |
| 2   | boolean comparison             | Using `=` or `==` operators to compare boolean values or None values                                |
| 3   | return in `__init__`           | Using an explicit return statement in the `__init__` function                                       |
| 4   | No exception type(s)           | A function that uses `try` and `except` does not define the exception type                          |
| 5   | function annotations           | A function does not explicitly annotate arguments/parameters or the expected output                 |
