# Система линейных уравнений - 1
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
y = (e*c-a*f)/(b*c-d*a)
x = (e*d-f*b)/(a*d-b*c)
print(x, y)