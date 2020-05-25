n = int(input('taduada de: '))
inicio = int(input('digite o inicio da tabuada: '))
fim = int(input('digite o fim da tabuada: '))
x = inicio
while x <= fim:
    print(f'{n} x {x} = {n * x}')
    x = x + 1