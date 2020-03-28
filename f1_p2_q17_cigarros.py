#Entrada
n_anos = float(input('Quantos anos ele fuma? '))
n_cigarros = float(input('Quantos cigarros por dia? '))
preco_carteira = float(input('Quanto custa uma carteira de cigarros? '))

#Processamento
valor_um_cigarro = preco_carteira / n_cigarros
gasto_dia = n_cigarros * valor_um_cigarro
gasto_mes = gasto_dia * 30
gasto_ano = gasto_mes * 12

gasto_total = n_anos * gasto_ano

#Saída
print(f'Uma pessoa que fuma a {n_anos} anos gastou um total de R$ {gasto_total} em cigarros.')

