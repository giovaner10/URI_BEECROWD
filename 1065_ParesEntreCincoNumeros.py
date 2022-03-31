c = p = 0

while c < 5:
    n = int(input())
    if (n%2) == 0:
        p += 1
    c+=1
print('{} valores pares' .format(p))
