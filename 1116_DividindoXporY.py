n= int(input())
cont = 0
while cont < n:
    v=input().split()
    x,y=v
    x=int(x)
    y=int(y)

    if y == 0:
        print('divisao impossivel')
    else:
        print('{:.1f}'.format(x/y))
    cont+=1
