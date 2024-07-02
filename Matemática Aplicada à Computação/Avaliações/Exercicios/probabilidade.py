# python -m pip install scipy

import scipy.stats
media= 12450
desvio_padrao= 231
X= 1
p=0.5-scipy.stats.norm(media,desvio_padrao).cdf(X)
print(p)


# Abaixo da Media

import scipy.stats
media= 12000
desvio_padrao= 800
X= 10000
p=0.5-scipy.stats.norm(media,desvio_padrao).cdf(X)
print(p)