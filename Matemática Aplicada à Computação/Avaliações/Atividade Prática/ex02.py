# python -m pip install matplotlib
import matplotlib.pyplot as plt

# Função quadratica y=ax^2 + b * x + c


a = 10
b = -150
c = 300
xv = -b/(2*a)
delta = b ** 2 - 4 * a * c
yv = -delta / (4 * a)
print(xv)
print(yv)
