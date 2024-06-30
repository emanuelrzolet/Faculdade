# python -m pip install scipy
from scipy.interpolate import lagrange

# Os valores de x sao array[0] e y array[1]
x = (0,3,5,7)
y = (2,-4,1,6)

p = lagrange(x,y)
print(p)

# Resposta A