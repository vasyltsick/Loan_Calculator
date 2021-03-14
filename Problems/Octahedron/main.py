from math import sqrt

a = int(input())
s = round(2 * sqrt(3) * pow(a, 2), 2)
v = round((sqrt(2) * pow(a, 3)) / 3, 2)

print(s, v)
