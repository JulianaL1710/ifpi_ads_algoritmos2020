#Entrada
num_anos = int(input('anos: '))
num_meses = int(input('meses: '))
num_dias = int(input('dias: '))

#Processamento
total_dias = (num_anos * 365) + (num_meses * 30) + (num_dias)

#Saída
print('A idade de uma pessoa com {} anos, {} meses e {} dias equivale a {} em dias'
.format(num_anos, num_meses, num_dias, total_dias))


