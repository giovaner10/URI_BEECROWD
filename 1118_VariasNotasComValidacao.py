soma = cont = f = 0
continuar = True
while continuar == True:
    n=float(input())

    if n < 0 or n > 10:
        print('nota invalida')

    else:
        soma += n
        cont+=1
        if cont == 2:
            print('media = {:.2f}'.format(soma/2))
            while True:
                f=float(input('novo calculo (1-sim 2-nao)\n'))
                if f ==1:
                    soma = cont = 0
                    continuar = True
                    break
                elif f ==2:
                    continuar = False
                    break
