carro = int(input('digite a velocidade do carro: '))

if carro > 80:
    print('voce foi multado')
    multa = (carro - 80) * 5
    print(f'voce deve pagar uma multa de {multa}')
else:
    print('dirija com cuidado')