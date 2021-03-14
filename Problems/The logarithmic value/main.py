import math

x = int(input())
base = int(input())

if base <= 0 or base == 1:
    result = math.log(x)
else:
    result = math.log(x, base)
print(round(result, 2))
