consumo = int(input("quantidade de KW/H consumida? "))

print('''qual o tipo  de instalacao
R = Residencia
C = Comercio
I = industria''')

tipo = input("Tipo da instalação (r,c ou i): ")

if tipo == "r":
    if consumo <= 500:
        preço = 0.40
    else:
        preço = 0.65
elif tipo == "i":
    if consumo <= 5000:
        preço = 0.55
    else:
        preço = 0.60
elif tipo == "c":
    if consumo <= 1000:
        preço = 0.55
    else:
        preço = 0.60
else:
    preço = 0
    print("Erro ! Tipo de instalação desconhecido!")
custo = consumo * preço
print("Valor a pagar: R$ %7.2f" % custo)