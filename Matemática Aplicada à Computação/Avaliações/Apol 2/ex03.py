import pandas as pd
x = {'Pesos':[8,7,9,10,2,7,9,10,9,3,8,5]}
p=pd.DataFrame(x)
desvioPadrao = p['Pesos'].std()

print(f"Desvio Padrao: {desvioPadrao}")