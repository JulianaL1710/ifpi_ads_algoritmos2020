#Entrada
b = int(input('Insira um número binário de 4 dígitos: '))

#Processamento
m = b // 1000
resto = b % 1000
c = resto // 100
resto = resto % 100
d = resto // 10
u = resto % 10

d1 = u * (2**0)
d2 = d * (2**1)
d3 = c * (2**2)
d4 = m * (2**3)
dec = d1 + d2 + d3 + d4

#Saída
print(f'O número binário {b} equivale a {dec} na base decimal)')