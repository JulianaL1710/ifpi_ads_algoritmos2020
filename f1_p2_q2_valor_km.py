#Entrada
num_metros = int(input('digite um valor em metros:'))

#Processamento
quilometros = (num_metros)//1000
metros = (num_metros)%1000

#Saida
print(f'{num_metros} m equivale a {quilometros} km e {metros} m')
