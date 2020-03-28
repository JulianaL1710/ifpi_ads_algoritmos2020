#Entrada
num_int = int(input('digite um numero de 3 digitos: '))

#Processamento
centena = num_int // 100
resto = num_int % 100

dezena = resto // 10
unidade = resto % 10

inverso = unidade * 100 + dezena * 10 + centena * 1
resultado = num_int - inverso

#Saida
print(f' a diferença entre {num_int} e o seu inverso {inverso} é igual a {resultado}')