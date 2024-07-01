import pandas as pd
x = {'Pesos':[67.8, 78.6, 54.4, 98.6, 99.4, 130.8, 142.6, 161.6, 142.5, 158.4]}
p=pd.DataFrame(x)
desvioPadrao = p['Pesos'].std()

print(f"Desvio Padrao: {desvioPadrao}")