n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))
n3 = int(input('digite um numero: '))

if n1 > n2 > n3:
    print(f'o maior numero e {n1}')
if n2 > n3 > n1:
    print(f'o maior numero e {n2}')
if n3 > n2 > n1:
    print(f'o maior numero e {n3}')

if n1 < n2 < n3:
    print(f'o menor numero e {n1}')
if n2 < n3 < n1:
    print(f'o menor numero e {n2}')
if n3 < n2 < n1:
    print(f'o menor numero e {n3}')
