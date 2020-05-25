m1 = float(input('digite a nota1: '))
m2 = float(input('digite a nota2: '))
m3 = float(input('digite a nota3: '))

s = (m1 + m2 + m3) / 3

if s >= 7:
    print(f'{s:.2f} aluno aprovado')
else:
    print(f'{s:.2f} aluno reprovado')