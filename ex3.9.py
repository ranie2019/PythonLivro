dia = int(input('quantidades de dias: '))
horas = int(input('quantidades de horas: '))
minutos = int(input('quantidades de minutos: '))
segundos = int(input('quantidades de segundos: '))

segundos = segundos * 1
minutos = minutos * 60
horas = horas * 3600
dia = dia * 86400

soma = segundos + minutos + horas + dia

print(f'o total de segundos e {soma:}')