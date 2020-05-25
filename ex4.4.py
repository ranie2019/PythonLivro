s = float(input('digite o seu salario: '))
p = s + (s * 10 / 100)
p2 = s + (s * 15 / 100)
if s >= 1250:
    print(f'voce teve um aumento de 10 %e seu salario foi para {p}')
else:
    print(f'voce teve um aumento de 15 %e seu salario foi para {p2}')