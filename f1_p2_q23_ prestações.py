#Entrada
valor_produto = int(input('Qual o valor do produto? '))

#Processamento
prestacoes = valor_produto // 3
valor_entrada = valor_produto - prestacoes * 2

#Saida
print(f'O valor de entrada é igual a R$ {valor_entrada} e o valor de prestaçoes é R${prestacoes} ')

