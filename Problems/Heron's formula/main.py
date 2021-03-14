import math

a, b, c = int(input()), int(input()), int(input())
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(s)
