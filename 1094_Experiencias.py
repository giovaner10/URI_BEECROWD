n= int(input())
cont=1
total=0
c = r = s = 0
while cont <= n:
    t=input().split()
    a,b=t
    
    if b =='C':
        c+=int(a)
        total+=int(a)

    elif b =='R':
        r+=int(a)
        total+=int(a)

    elif b =='S':
        s+=int(a)
        total+=int(a)
 
    cont +=1



print('Total: {} cobaias' .format(total))
print('Total de coelhos: {}'.format(c))
print('Total de ratos: {}'.format(r))
print('Total de sapos: {}'.format(s))
print('Percentual de coelhos: {:.2f} %' .format((c/total)*100))
print('Percentual de ratos: {:.2f} %' .format((r/total)*100))
print('Percentual de sapos: {:.2f} %' .format((s/total)*100))
