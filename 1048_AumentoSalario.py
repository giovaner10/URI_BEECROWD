s=float(input())
if s <= 400:
    print('Novo salario: {:.2f}' .format(s*1.15))
    print('Reajuste ganho: {:.2f}' . format((s*1.15)-s))
    print('Em percentual: 15 %')
elif s <= 800:
    print('Novo salario: {:.2f}' .format(s*1.12))
    print('Reajuste ganho: {:.2f}' . format((s*1.12)-s))
    print('Em percentual: 12 %')
elif s <= 1200:
    print('Novo salario: {:.2f}' .format(s*1.10))
    print('Reajuste ganho: {:.2f}' . format((s*1.10)-s))
    print('Em percentual: 10 %')
elif s <=2000:
    print('Novo salario: {:.2f}' .format(s*1.07))
    print('Reajuste ganho: {:.2f}' . format((s*1.07)-s))
    print('Em percentual: 7 %')
elif s > 2000:
    print('Novo salario: {:.2f}' .format(s*1.04))
    print('Reajuste ganho: {:.2f}' . format((s*1.04)-s))
    print('Em percentual: 4 %')
