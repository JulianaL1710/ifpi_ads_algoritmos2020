#Entrada
nota1 = float(input('escreva a nota1: '))
nota2 = float(input('escreva a nota2: '))
nota3 = float(input('escreva a nota3: '))
peso1 = int(input('escreva peso1: '))
peso2 = int(input('escreva peso2: '))
peso3 = int(input('escreva peso3: '))

#Processamento
media_ponderada = (nota1+nota2+nota3) / (peso1+peso2+peso3)

#Saida
print(f'{media_ponderada} e a media ponderada das 3 notas, com seus respectivos pesos')