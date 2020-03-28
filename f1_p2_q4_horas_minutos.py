#Entrada
s = int(input('Digite um valor em segundos: '))

#Processamento
h = s // 3600
m = (s % 3600) // 60
seg = (s % 3600) % 60

#Saída
print(f'{s} segundos corresponde a {h} horas e {m} minutos e {seg} segundos')