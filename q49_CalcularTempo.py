#Primeiro tempo:
horasInic = int(input('Hora inicial: '))
minutosInic = int(input('Minuto inicial: '))
segundosInic = int(input('Segundo inicial: '))
#Segundo tempo:
horasFim = int(input('\nHora final: '))
minutosFim = int(input('Minuto final: '))
segundosFim = int(input('Segundo final: '))
#Correções:
if segundosFim < segundosInic:
    segundosFim = segundosFim + 60
    minutosFim = minutosFim - 1

if minutosFim < minutosInic:
    minutosFim = minutosFim + 60
    horasFim = horasFim - 1
#Calculo:
horasTotal = horasFim - horasInic
minutosTotal = minutosFim - minutosInic
segundosTotal = segundosFim - segundosInic
print(f'\nTempo transcorrido: \n{horasTotal} : {minutosTotal} : {segundosTotal}')
