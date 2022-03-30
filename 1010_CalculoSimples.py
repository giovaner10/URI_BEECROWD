l1=input().split()
l2=input().split()
c1, n1, v1=l1
c2, n2, v2=l2
t=int(n1)*float(v1) + int(n2)*float(v2)
print('VALOR A PAGAR: R$ %0.2f' %t)
