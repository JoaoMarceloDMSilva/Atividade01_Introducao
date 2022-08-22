valorHora = float(input('Valor por hora de serviço: '))
horasMes = int(input('Quantidade de horas trabalhadas no mês: '))
soldo = valorHora * horasMes * 1.1
print(f'Valor a ser pago ao funcionário: {soldo:.2f}')
