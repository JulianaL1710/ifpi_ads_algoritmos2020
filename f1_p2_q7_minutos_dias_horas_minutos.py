#Entrada
minutos = int(input('Insira um número inteiro em minutos: '))

#Processamento
dias = (minutos // 24) // 60 
horas = (minutos // 60) % 24
m = (minutos % 60) % 60

#Saída
print(f'{minutos} min corresponde a {dias} dias, {horas} horas e {m} min')