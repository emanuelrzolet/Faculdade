# python -m pip install matplotlib
import matplotlib.pyplot as plt

# Função quadratica y=ax^2 + b * x + c


a = -340
b = 5700
c = -9500
xv = -b/(2*a)
delta = b ** 2 - 4 * a * c
yv = -delta / (4 * a)
print(xv)
print(yv)
