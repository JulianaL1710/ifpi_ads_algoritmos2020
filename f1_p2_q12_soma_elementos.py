#Entrada
num = int(input('Digite um número de 4 dígitos: '))

#Processamento
m = num // 1000
c = (num % 1000) // 100
d = (num % 100) // 10
u = (num % 10) // 1

soma = m + c + d + u

#Saída
print(f'A soma dos elementos do número {num} é igual a {soma}.')
print(f'{m} + {c} + {d} + {u} = {soma}')