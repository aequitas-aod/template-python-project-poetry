import my_project

# this is the main module of your app
# it is only required if your project must be runnable
# this is the script to be executed whenever some users writes `python -m my_project` on the command line, eg.
x = my_project.MyClass().my_method()
print(x)
