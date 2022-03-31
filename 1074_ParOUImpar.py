n=int(input())
cont=0
while cont < n:
    v=int(input())
    if v>0 and v%2==0:
        print('EVEN POSITIVE')
    if v>0 and v%2!=0:
        print('ODD POSITIVE')
    if v<0 and v%2==0:
        print('EVEN NEGATIVE')
    if v<0 and v%2!=0:
        print('ODD NEGATIVE')
    if v==0:
        print('NULL')
    cont +=1
    