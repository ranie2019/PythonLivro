dias = int(input('quantos dias alugado: '))
km = int(input('qual a quantidade de km percorrido: '))

soma = (dias * 60) + (km * 0.15)

print(f'o valor a pagar e de R$ {soma:.2f}')