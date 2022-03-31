x=input().split()
c,q=x
c=int(c)
q=int(q)
if c==1:
    print('Total: R$ {:.2f}' .format(4*q))
elif c==2:
    print('Total: R$ {:.2f}' .format(4.5*q))
elif c==3:
    print('Total: R$ {:.2f}' .format(5*q))
elif c==4:
    print('Total: R$ {:.2f}' .format(2*q))
elif c==5:
    print('Total: R$ {:.2f}' .format(1.5*q))

