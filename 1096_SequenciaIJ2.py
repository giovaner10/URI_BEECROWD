i = 1
j=7
cont=0
conti=1
while cont < 15:
    print('I={} J={}' .format(i,j))
    j-=1
    if j < 5:
        j=7
    cont+=1
    conti+=1
    if conti >3:
        i+=2
        conti=1
    