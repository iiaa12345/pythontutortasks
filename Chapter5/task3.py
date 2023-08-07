from math import *


a = input()

print(a[ceil(len(a) / 2):] + a[:ceil(len(a) / 2)])
