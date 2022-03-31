x = int (input())
i = 1
if x %2 !=0:
    while  i<=6:
        print(x)
        x+=2
        i+=1
elif x %2 ==0:
    x = x - 1
    while  i<=6:
        x+=2
        i+=1
        print(x)
        