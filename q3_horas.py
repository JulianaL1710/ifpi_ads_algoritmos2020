#Entrada
valor_em_minutos = float(input('minutos: '))

#Processamento
horas = valor_em_minutos // 60
minutos = (valor_em_minutos)-(horas*60)

#Saida
print(f'{horas} e o equivalente em horas e {minutos} e o equivalente em minutos')