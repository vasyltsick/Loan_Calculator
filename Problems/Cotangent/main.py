from math import tan, radians

degrees = int(input())

cotan = 1 / tan(radians(degrees))
print(round(cotan, 10))
