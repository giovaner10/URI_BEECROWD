i = 1
par = impar = pos = neg = 0

while i <= 5:
    n = int (input())
    if n%2 ==0:
        par +=1
    if n%2!=0:
        impar +=1
    if n >0:
        pos +=1
    if n < 0:
        neg +=1
    i +=1

print('{} valor(es) par(es)'.format(par))
print('{} valor(es) impar(es)' .format(impar))
print('{} valor(es) positivo(s)' .format(pos))
print('{} valor(es) negativo(s)' .format(neg))
    