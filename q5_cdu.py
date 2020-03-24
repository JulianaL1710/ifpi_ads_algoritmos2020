#Entrada
numero_inteiro = int(input('insira um numero de 3 digitos: '))

#Processamento 
centena = numero_inteiro // 100
dezena = numero_inteiro % 10
unidade = (numero_inteiro)%(centena+dezena)
soma = centena+dezena+unidade

#Saida
print(f'{centena} + {dezena} + {unidade} resulta em {soma}')
