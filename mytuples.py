"""
Commands for running mypy from shell:

cd path/to/project
mypy mytuples.py

"""

def my_tuple0(a: int, b: int, c:int) -> tuple:
    return tuple((a, b, c))


t47_5 = my_tuple0(4, 7, -5)
print('A tuple of int: ', t47_5)
print('Type annotations of my_tuple function: \n', my_tuple0.__annotations__)
#%%


def my_tuple0(a: int, b: int, c:int) -> tuple:
    return tuple((a, b, c))


t47_5 = my_tuple0(4, 7, -5)
print('A tuple of int: ', t47_5)
print('Type annotations of my_tuple function: \n', my_tuple0.__annotations__)