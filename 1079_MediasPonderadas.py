n=int(input())
cont=1
while cont <=n :
    v=input().split()
    a,b,c=v
    a=float(a)
    b=float(b)
    c=float(c)
    print('{:.1f}' .format(  (a*2 + b*3 + c*5)/10))
    cont+=1
    