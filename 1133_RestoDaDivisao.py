x=int(input())
y=int(input())
maior = menor = x
if x>y:
    maior=x
    menor=y
else:
    menor=x
    maior=y
menor +=1
while menor < maior:
    if menor % 5 == 2 or menor % 5 == 3 :
        print(menor)
    menor+=1
    