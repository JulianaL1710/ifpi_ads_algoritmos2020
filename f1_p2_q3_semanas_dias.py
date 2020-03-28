#Entrada
num_dias = int(input('numero inteiro de dias:'))

#Processamento
semanas = num_dias // 7
dias = num_dias % 7

#Saída
print(f'{num_dias} dias corresoponde a {semanas} semanas e {dias} dias')