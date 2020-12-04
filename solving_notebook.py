#%%
from typing import List
from advent_utils import input_to_str_list
from day2 import valid_passwords, passwords_redux
from day3 import toboggan_1
#%%
# Day 2 test and answer
input_list = input_to_str_list('day2/input.txt')
valids = valid_passwords(input_list)
print(f"there are {len(valids)} valid passwords")
redux = passwords_redux(input_list)
print(f"under the new system {len(redux)} passwords are valid")
# %%
input_course = input_to_str_list('day3/input.txt')
encountered_trees = toboggan_1(3, 1, input_course)
print(f"encountered {encountered_trees} trees")
# %%
from functools import reduce
speeds = [(1,1), (3, 1), (5,1),(7,1),(1,2)]
alltrees: List[int] = []
for x,y in speeds:
    trees = toboggan_1(x,y, input_course)
    alltrees.append(trees)
    print(f"encountered {trees} with slope ({x},{y})")
print(reduce(lambda x, y: x * y, alltrees, 1))
#%%
from advent_utils import input_to_str_list
my_l = input_to_str_list('day4/smol.txt')
print(my_l)
# %%
from day4 import valid_passports , extra_valid
valids = valid_passports('day4/input.txt')
print(f"there are {valids} valid passports")
# %%
from day4 import extra_valid
xtra_valids = extra_valid('day4/input.txt')
print(f"there are {xtra_valids} xtra valid passports")
# %%
