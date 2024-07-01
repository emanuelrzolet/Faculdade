vExato = 0.5672
vRelativo = 0.55

eAbsoluto = abs(vExato-vRelativo)
print("Erro Absoluto: ",format(eAbsoluto))

eRelativo = abs(vExato-vRelativo)/abs(vExato)
print("Erro Relativo: ",format(eRelativo))