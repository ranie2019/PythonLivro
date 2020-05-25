n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))
opcao = 0

print('''escola a opcao 
[1] +
[2] -
[3] x
[4] ÷
''')

opcao = int(input('escolar qual operacao voce quer: '))
if opcao == 1:
    soma = n1 + n2
    print(f'o resultado e {soma}')

elif opcao == 2:
    menos = n1 - n2
    print(f'o resultado e {menos}')

elif opcao == 3:
    vezes = n1 * n2
    print(f'o resultado e {vezes}')

elif opcao == 4:
    dividir = n1 / n2
    print(f'o resultado e {dividir}')
else:
    print('Opção invalida')