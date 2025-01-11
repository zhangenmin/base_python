# -*- coding: utf-8 -*-
# @Time    : 2025/1/11 23:07
# @Author  : xtldn
# @File    : list.py
squares = [value**2 for value in range(1,11)]
print(squares)
number_20 = [value for value in range(1,21)]
print(number_20)

# number_mililion = [value for value in range(1,100000001)]
# print(min(number_mililion))
# print(max(number_mililion))
# print(sum(number_mililion))


players = ['charles','martina','michael','florence','eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())


motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)


motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a "+last_owned.title()+".")