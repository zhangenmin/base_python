# -*- coding: utf-8 -*-
# @Time    : 2025/1/11 23:07
# @Author  : xtldn
# @File    : list.py
squares = [value**2 for value in range(1,11)]
print(squares)
number_20 = [value for value in range(1,21)]
print(number_20)

number_mililion = [value for value in range(1,100000001)]
print(min(number_mililion))
print(max(number_mililion))
print(sum(number_mililion))