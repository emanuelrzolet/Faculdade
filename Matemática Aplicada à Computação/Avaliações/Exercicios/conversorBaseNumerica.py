# decimal para binário e hexadecimal

numero=int(input('Digite um número inteiro: '))

print(f'O hexadecimal correspondente é: {hex(numero)[2:]}')

binario=''
while numero > 0:
 binario+=str(numero%2)
 numero//=2
print(f'O binário correspondente é: {binario[::-1]}')

#  binario para decimal e Hexadecimal

binario = input('Digite um número binário: ')
decimal = 0
for digito in binario:
    decimal = decimal*2 + int(digito)

print(f'O decimal correspondente é: {decimal}')
print(f'O hexadecimal correspondente é: {hex(decimal)[2:]}')

# Hexadecimal para binario e decimal

hexadecimal = input('Digite um número hexadecimal: ')
decimal = int(hexadecimal, 16)

print(f'O decimal correspondente é: {decimal}')

binario = bin(decimal)[2:]
print(f'O binário correspondente é: {binario}')