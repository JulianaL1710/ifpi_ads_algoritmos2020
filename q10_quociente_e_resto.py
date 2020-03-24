#Entrada
number1 = int(input('escreva um numero: '))
number2 = int(input('escreva um numero: '))

#Processamento
quociente = number1 // number2
resto = number1 - (number2*quociente)

#Saida
print(f'{quociente} e o quociente e {resto} e o resto')