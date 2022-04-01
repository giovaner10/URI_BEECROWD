seg = True
a = g = d = 0
while seg == True:
    while True:
        #print('1.Álcool 2.Gasolina 3.Diesel 4.Fim')
        t=float(input())
        if t==1:
            a+=1
        elif t==2:
            g+=1
        elif t==3:
            d+=1
        elif t==4:
            seg=False
            break
print('MUITO OBRIGADO')
print('Alcool: {}' .format(a))
print('Gasolina: {}' .format(g))
print('Diesel: {}' .format(d))
