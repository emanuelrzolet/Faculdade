



numero=int(input('Digite um número inteiro: '))

print(f'O hexadecimal correspondente é: {hex(numero)[2:]}')

binario=''
while numero > 0:
 binario+=str(numero%2)
 numero//=2
print(f'O binário correspondente é: {binario[::-1]}')
