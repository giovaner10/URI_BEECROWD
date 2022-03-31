soma = cont = 0
while cont < 2:
    n=float(input())

    if n < 0 or n > 10:
        print('nota invalida')

    else:
        soma += n
        cont+=1
       
print('media = {:.2f}'.format(soma/2))
       