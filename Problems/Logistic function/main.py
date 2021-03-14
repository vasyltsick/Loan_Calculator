import math

x = int(input())
logistic = math.exp(x) / (math.exp(x) + 1)
print(round(logistic, 2))
