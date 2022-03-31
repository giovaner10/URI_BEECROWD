i = 1
soma = pos = 0
while i <= 6:
    n = float(input())
    if n > 0:
        pos = pos + 1
        soma = soma + n
    i= i + 1
media = soma / pos
print ('{} valores positivos' .format(pos))
print('{:.1f}' .format(media))
    