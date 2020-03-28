#Entrada
a = int(input('Insira o valor de a: '))
b = int(input('Insira o valor de b: '))
c = int(input('Insira o valor de c: '))
d = int(input('Insira o valor de d: '))
e = int(input('Insira o valor de e: '))
f = int(input('Insira o valor de f: '))

#Processamento
x = ((c*e) - (b*f)) / ((a*e) - (b*d))

y = ((a*f) - (c*d)) / ((a*e) - (b*d))

#Saída
print(f'O valor de X e Y em uma determinada equação linear,\n equivale a {x} e {y}, respectivamente.')
