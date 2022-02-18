'''

'''

from sys import path
path.append('D:\\programming\\Python\\pe2\\pe2\\module1\\modules')
path.append('D:\\programming\\Python\\pe2\\pe2\\module1\\extra')

# todo why does relative path not work?
# path.append('..\\modules')

# for p in path:
#     print(p)

#from module import suml, prodl
import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))
