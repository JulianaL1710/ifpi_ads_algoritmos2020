#Entrada
num1 = int(input('Digite o valor de A: '))
num2 = int(input('Digite o valor de B: '))
num3 = int(input('Digite o valor de C: '))

#Processamento
r = (num1 + num2) ** 2
s = (num2 + num3) ** 2

d = (r + s) / 2

#Saída
print(f'O valor da expressão D = (R + S) / 2 é igual a {d}')
