# Week 1

## Goals
- Install all of the tools that we will use for this empirical study (e.g., python, poetry, pytest, chasten and mutmut although this might change)
- Find 3 to 5 subjects and fork them into the AstuteSource organization. Then, complete the following steps for each subject:
- Pick a name for the tool that we are going to build and then create a repository for it in the AstuteSource organization
- Make sure that you are an owner/maintainer of the AstuteSource organization and the repositories inside of it
- Divide up the implementation tasks from the whiteboard pictures for the main tool that we are going to implement

## Log

- Ensured that all needed programming tools were installed.
- Ran development tools on example python project of [poetry](https://github.com/python-poetry/poetry).

# Week 2

## Log

- This week I worked to create the `mutmut` execution for the `analyzer` program
- I created a script test that ran `mutmut`, saved the results as a Junit XML file, then I used a `npm` program called `junit2json` to turn the file into a JSON
 - This solution was not ideal because of the use of `typescript`, but I believe this is still the best solution
- I was able to get this script to work on the `lazytracker` program

# Week 3

## Log

- This week I worked to create the overall script that can create a combined JSON file.
 - added a submodule for lazytracker in the demo folder. This folder will be used for future demo programs
 - changed the execute_chasten function to be able to use the outputted JSON
 - changed the execute_mutmut program to give formatted JSON results back
 - changed the path locations so they they hopefully work on more OS's without hard-coding
- This allowed for `mutmut` and `chasten` to be run in order to create a unified JSON with `lazytracker`'s information

# Week 4

## Log

- This week I worked on mostly turning the JSON into a Pandas data frame
 - This will allow us to feed a pandas data frame into a Machine Learning algorithm
 - This means that this step is very import to have clean data so it is easy to use moving on.
- I also added submodules for different projects such as `python-playground`
 - This allowed for the testing and creation of mutation score and antipattern tracking for a new program 

# Week 5

# Week 6
