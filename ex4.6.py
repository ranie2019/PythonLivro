n = int(input('digite uma distacia em em km: '))
soma = n * 0.50
soma2 = n * 0.45
if n >= 200:
    print(f'o valor da carrida fico em R${soma:.2f}')
else:
    print(f'o valor da carrida fico em R${soma2:.2f}')