#Entrada
valor_f = float(input('Qual o custo de fábrica de um carro? '))

#Processamento
d = valor_f + (valor_f * (28/100))
i = valor_f + (valor_f *(45/100))

custo_total = valor_f + d + i

#Saída
print(f'Um carro com custo de fábrica de R$ {valor_f} \n chegará ao consumidor com o valor de {custo_total}')
