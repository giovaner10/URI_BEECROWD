v=float(input())

if v>100 or v<0:
    print('Fora de intervalo')
elif v>=0 and v <=25:
    print('Intervalo [0,25]')
elif v<=50:
    print('Intervalo (25,50]')
elif v<=75:
    print('Intervalo (50,75]')
elif v<=100:
    print('Intervalo (75,100]')
