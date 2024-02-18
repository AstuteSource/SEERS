# Week 4 02/05 -02/11

# Goal
Install all of the tools that we will use for this empirical study (e.g., python, poetry, pytest, chasten and mutmut although this might change)

Find at least 3 to 5 subjects and fork them into the AstuteSource organization. Then, complete the following steps for each subject:

It provides the basic functionality to help write tooling that generates distribution files from Python projects.
https://github.com/pypa/pyproject-hooks

This package is a plugin that updates dependencies and bumps their versions in pyproject.toml file. The version constraints are respected, unless the --latest flag is passed, in which case dependencies are updated to latest available compatible versions.
https://github.com/MousaZeidBaker/poetry-plugin-up


https://github.com/sphinx-toolbox/sphinx-pyprojecto

# Week 5 02/12 -02/18  (Antipattern team)

# Goal   
Document and define Python programming antipatterns in the SEERS documentation 

| #   | Name        |  Definition |         
| --- | ----------- | ------------------------------------------------------------------| 
| 1   |   is_void          | Whether the return value of the function is None or not |
| 2   |   non_void_percent |The percentage of functions returning non-None values|
| 3   |   getter_percentage|The percentage of getter methods in the class|
| 4   |   is_public        | Whether the function is public or not |
| 5   |   is_static        |'Static' isn't a concept in Python, however it might refer to whether or not a method is class method|
| 6   |   is_nested        |Is the function declared within another function (closure) or not?|
| 7   |   nested_depth     | The highest level of layering in function declarations. In this case, the maximum nested depth is 3.|
| 8   |   num_conditions   |The quantity of conditions (`if, if-else, and switch`) in the function|
| 9   |   (cond(cond))     |The number of nested conditions ( `if { if {} }`) in the function|
| 10  |   (cond(loop))     | The number of nested condition-loops ( `if { for {} }`) in the function|
| 11  |   (loop)           |The number of loops (`for, while, and do-while`) in the function|
| 12  |   (loop(cond))     |The number of nested loop-conditions ( `for { if {} }`) in the function|
| 13  |   (loop(loop))     |The number of nested loop-conditions  (`for { for {} }`) in the function|
| 14  |   method_length    | The amount of lines of code within the function|
| 15  |   direct_test_no.  |The number of test functions/methods that directly call the function/method under test |
| 16  |   test_distance    |The shortest function/method call sequence necessary to activate the function/method (production code) by testing functions/methods|                           
| 17  |  assertion_no                |The number of assertions in direct tests|
| 18  |  assertion-McCabe_Ratio      |The relationship between the total amount of assertions in direct tests and the McCabe Cyclomatic complexity.|
| 19  |  assertion_density           |The proportion of the total number of assertions in direct tests to the lines of code in direct tests |
| 20  |  not_using_context_manager   |Whether file handling is done without using the context manager (with statement).|
| 21  |  using_manual_indexing       |Whether manual indexing is used instead of Python's enumerate function.|
| 22  |  modifying_mutable_default_arguments   |Whether mutable default arguments are modified within the function.|
| 23  |  deep_nesting                | The number of levels of nesting within loops, conditional statements, or function calls in the code.|
| 24  |  Polluting_namespace         |Importing all symbols from a module using `import *`, leading to namespace pollution and potential confusion about symbol origins.|
| 25  |  Misuse_of_List_Comprehensions|Overusing or misusing list comprehensions, leading to reduced readability, complexity, or performance issues.|

