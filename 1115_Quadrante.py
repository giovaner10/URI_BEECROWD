while True:
    v=input().split()
    x,y=v
    x=int(x)
    y=int(y)
    if y==0 or x==0:
        break
    else:
        if x > 0 and y>0:
            print('primeiro')
        if x > 0 and y < 0:
            print('quarto')
        if x < 0 and y < 0:
            print('terceiro')
        if  x < 0 and y > 0:
            print('segundo')
            