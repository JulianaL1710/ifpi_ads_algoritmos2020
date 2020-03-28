# ENTRADA
valor = int(input('Qual o valor do saque: '))

# PROCESSAMENTO
cem = valor//100
cinquenta = (valor%100)//50
vinte = ((valor%100)%50)//20
dez = (((valor%100)%50)%20)//10
cinco = ((((valor%100)%50)%20)%10)//5
dois = (((((valor%100)%50)%20)%10)%5)//2

# SAIDA
print(f'Serão sacadas {cem} nota de cem, {cinquenta} notas de cinquenta, {vinte} notas de vinte,\n {dez} notas de dez, {cinco} notas de cinco reais e {dois} notas de dois reais.')


