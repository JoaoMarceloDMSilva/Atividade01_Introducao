quantSegundos = int(input('Quantidade de segundos: '))
if quantSegundos >= 3600:
    horas = quantSegundos//3600
    minutos = (quantSegundos % 3600)//60
    segundos = (quantSegundos % 3600)%60
    print(f'{horas} : {minutos} : {segundos}')
else:
    minutos = quantSegundos//60
    segundos = quantSegundos % 60
    print(f'00 : {minutos} : {segundos}')
