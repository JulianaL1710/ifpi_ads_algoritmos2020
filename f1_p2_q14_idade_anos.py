#Entrada
n_dias = int(input('Idade expressa em dias: '))

#Processamento
a = n_dias // 365
m = (n_dias % 365) // 30
d = (n_dias % 365) % 30

#Saída
print(f'{n_dias} dias corresponde a {a} anos, {m} meses e {d} dias')