horasInic = int(input('Hora inicial: '))
minutosInic = int(input('Minuto inicial: '))
segundosInic = int(input('Segundo inicial: '))

horasDur = int(input('\nDuração em horas: '))
minutosDur = int(input('Duração em minutos: '))
segundosDur = int(input('Duração em segundos: '))
minutosAux = 0
horasAux = 0


if (segundosInic + segundosDur) >= 60:
    segundosTotal = segundosInic + segundosDur - 60
    minutosAux =  1
else:
    minutosTotais = segundosInic + segundosDur

if (minutosInic + minutosDur + minutosAux) >= 60:
    minutosTotais = minutosInic + minutosDur + minutosAux - 60
    horasAux =  1
else:
    minutosTotais = minutosInic + minutosDur + minutosAux

horasTotais = horasInic + horasDur + horasAux

print(f'\nHorário final:\n{horasTotais} : {minutosTotais} : {segundosTotal}')
