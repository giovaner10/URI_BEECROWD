while True:
    v=input().split()
    x,y=v
    x=int(x)
    y=int(y)
    if x!=y:
        if x>y:
            print('Decrescente')
        else:
            print('Crescente')
    else:
        break
    