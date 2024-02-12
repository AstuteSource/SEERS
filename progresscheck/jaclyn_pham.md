# Week 1 (Feb 5 2024 - Feb 9 2024)

## Weekly Goals

This week's goals are:

- Installations: Python, Poetry, Pytest, Chasten, Mutmut. Update Chasten
- Find three to five open source Python projects that use Poetry for dependencies
- Determine 1-2 code quality antipatterns
- Create a rough draft of code for identifying those antipatterns with Chasten or Symbex

### Progress Notes

#### Development Tasks

1. Update all tools, installations
2. Run Chasten on the following projects. I intentionally chose projects that covers diverse code design patterns

- [code-opener-cli](https://github.com/AstuteSource/code-opener-cli): The command line interface to add any project as favorite and open it from anywhere using just one command.
- [pytemplate](https://github.com/clemens33/pytemplate): a lightweight template project for python based on poetry, pre-commit, pytest and many other tools

3. Troubleshooting Mutmut execution

Here is my current error

```code
1. Running tests without mutations
⠋ Running...Traceback (most recent call last):
  File "/opt/homebrew/bin/mutmut", line 8, in <module>
    sys.exit(climain())
             ^^^^^^^^^
  File "/Users/jaclynpham/Library/Python/3.11/lib/python/site-packages/click/core.py", line 1157, in __call__
    return self.main(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/jaclynpham/Library/Python/3.11/lib/python/site-packages/click/core.py", line 1078, in main
    rv = self.invoke(ctx)
         ^^^^^^^^^^^^^^^^
  File "/Users/jaclynpham/Library/Python/3.11/lib/python/site-packages/click/core.py", line 1688, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/jaclynpham/Library/Python/3.11/lib/python/site-packages/click/core.py", line 1434, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/jaclynpham/Library/Python/3.11/lib/python/site-packages/click/core.py", line 783, in invoke
    return __callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/lib/python3.11/site-packages/mutmut/__init__.py", line 901, in wrapper
    f(*args, **kwargs)
  File "/opt/homebrew/lib/python3.11/site-packages/mutmut/__main__.py", line 141, in run
    sys.exit(do_run(argument, paths_to_mutate, disable_mutation_types, enable_mutation_types, runner,
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/lib/python3.11/site-packages/mutmut/__main__.py", line 341, in do_run
    baseline_time_elapsed = time_test_suite(
                            ^^^^^^^^^^^^^^^^
  File "/opt/homebrew/lib/python3.11/site-packages/mutmut/__main__.py", line 480, in time_test_suite
    raise RuntimeError("Tests don't run cleanly without mutations. Test command was: {}\n\nOutput:\n\n{}".format(test_command, '\n'.join(output)))
RuntimeError: Tests don't run cleanly without mutations. Test command was: python -m pytest -x --assert=plain

Output:

/Library/Frameworks/Python.framework/Versions/3.11/bin/python: No module named pytest
```

#### Documentation Tasks

Python Anti-Patterns I looked into this week, from the book [The Little Book of Python Anti-Patterns](https://docs.quantifiedcode.com/python-anti-patterns/):

Assigning a lambda expression to a variable

If you're going to assign a name to a `lambda`, you are better off just defining it as a `def`. This is more useful for tracebacks and string representations in general.

Anti-pattern: the following code assigns a `lambda` function which returns the double of its input to a variable.

```python
f = lambda x: 2*x
```

```python
def f(x): return 2*x
```

#### Miscellaneous

### Learning Documentation

I acknowledge that my knowledge of this field is very limited, and I would like to use this section as an opportunity to document what I've learned.

#### READ

- [pybugs](https://github.com/cbrentharris/pybugs): Python library for finding common bugs and anti patterns
- [The Little Book of Python Anti-Patterns](https://docs.quantifiedcode.com/python-anti-patterns/)
- [Python anti patterns](https://github.com/GalvanizeDataScience/python-anti-patterns/blob/master/beginner-mistakes.ipynb): commonly observed beginner-mistakes


# Week 2 (Feb 12 2024 - Feb 16 2024)

# Week 3 (Feb 19 2024 - Feb 23 2024)

# Week 4 (Feb 26 2024 - Mar 1 2024)