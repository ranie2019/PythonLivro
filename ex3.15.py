cigarro = int(input('quantidade de cigarros por dia: '))
anos = int(input('quantos anos: '))

soma1 = anos * 365 * cigarro * 10
soma2 = soma1 / (60 * 24)
print(f'voce perdeu {soma2:.0f} Dias de vida')