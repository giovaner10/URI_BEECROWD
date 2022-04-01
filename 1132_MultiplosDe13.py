soma=0
x=int(input())
y=int(input())
maior = menor = x
if x>y:
    maior=x
    menor=y
else:
    menor=y
    maior=y
while menor <= maior:
    if menor % 13 != 0:
        soma+=menor
    menor+=1
print(soma)
