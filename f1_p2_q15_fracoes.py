#Entrada
num1 = int(input('Insira o primeiro numerador: '))
den1 = int(input('Insira o primeiro denominador:'))

num2 = int(input('Insira o segundo numerador: '))
den2 = int(input('Insira o segundo denominador: '))

#Processamento
denominador = den1 * den2
numerador = (denominador // den1) * num1 + (denominador // den2) * num2

#Saída
print(f'A soma das frações é igual a {numerador} / {denominador}')