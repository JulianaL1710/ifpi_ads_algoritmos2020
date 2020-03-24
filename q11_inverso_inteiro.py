#Entrada
numero = int(input('escreva o numero com 3 digitos: '))

#Processamento
centena = int(numero/100)
dezena = int((numero%100) // 10)
unidade = int(numero)%((centena*100)+((dezena*10)))

#Saida
print(f'{unidade}{dezena}{centena} e o inverso de {numero}')


