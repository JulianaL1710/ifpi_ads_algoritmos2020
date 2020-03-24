#Entrada
valor_horas = float(input('escreva o valor em horas: '))
valor_minutos = float (input('escreva o valor em minutos'))

#Processamento
valor_convertido = valor_horas * 60
valor_total = (valor_convertido)+(valor_minutos)

#Saida
print(f'{valor_horas} horas convertidas em minutos e igual a:{valor_convertido}') 
print(f'a soma dos valores convertidos e igual a: {valor_total}')