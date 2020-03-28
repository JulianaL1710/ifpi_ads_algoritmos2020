#Entrada
n_horas = int(input('Número inteiro de horas: '))

#Processamento
sem = (n_horas // 24) // 7
dias = (n_horas // 24) % 24 
hrs =  (n_horas % 24) % 60

#Saída
print(f'{n_horas} corresponde a {sem} semanas e {dias} dias e {hrs} horas')