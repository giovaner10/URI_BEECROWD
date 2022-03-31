x=int(input())
y=int(input())
soma = 0
if x>y:
    x= x - 1
    while x>y:
        if x%2!=0:
            soma +=x
        x-=1
elif y>x:
    y=y-1
    while y>x:
        if  y%2!=0:
            soma+=y
        y-=1
print(soma)
