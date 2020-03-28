#Entrada
x1 = int(input('Informe o valor de x1: '))
x2 = int(input('Informe o valor de x2: '))

y1 = int(input('Informe o valor de y1: '))
y2 = int(input('Informe o valor de y2: '))

#Processamento
d = (((x2 - x1)**2) + ((y2 - y1)**2)) ** (1/2)

#Saída
print(f'O resultado da expressão d = (((x2 - x1)**2) + ((y2 - y1)**2)) ** (1/2) \n é igual a {d}')