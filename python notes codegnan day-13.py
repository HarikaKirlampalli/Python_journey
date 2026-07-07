'''DAY-13:
-------
passing by value:
@code
a = (1,2,3)
def some(a):
    for j in a:
        print(j)
some(a)

return keyword
---------------
>>in a function if a return is executed then it will exit from function with certain returned values.
@code
def myfunc_(b):
    return 5+b
a = myfunc_(15)
print(a)

**code to check build in functions:

import builtins
builtin_functions = [
    name for name in dir(builtins)
    if callable(getattr(builtins,name))]
print(builtin_functions)
print(f"Total built-in functions are {len(builtin_functions)}")

    RECURSIVE FUNCTION:
    ------------------
>>Recursive func that calls itself the repeatedly until a specified condition is met.
Syntax::
-------
def func_name(parameter):
    if condition: #base case
    return stmt
    else:
       return statement
print(func_name(arguments))

@code
def func_name(num):
    if num == 1: #base case
       return 1
    else:
       return num*func_name(num-1)
num = 10
print(func_name(num))
'''
