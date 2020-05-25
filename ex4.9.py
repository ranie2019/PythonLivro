casa = float(input('digite o valor da casa: '))
salario = float(input('digite o seu salario: '))
anos = int(input('digite a quantidades de anos a pagar: '))

prestacao = casa / (anos * 12)
minimo = salario - (salario * 30 / 100)

if prestacao > salario:
    print(f'uma casa no valor {casa:.2f} \ncom um salario de {salario:.2f} \npagando em {anos} \na prestacao vai ficar {prestacao:.2f} \nemprestimo NEGADO')
else:
    print(f'uma casa no valor {casa:.2f} \ncom um salario de {salario:.2f} \npagando em {anos} \na prestacao vai ficar {prestacao:.2f} \nemprestimo APROVADO')