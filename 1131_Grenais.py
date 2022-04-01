cont = 0
continuar = True
gre = inter = emp = 0
while continuar == True:
    n=input().split()
    x,y = n
    x=int(x)
    y=int(y)
    cont+=1
    if x > y:
        inter +=1
    elif x < y:
        gre+=1
    elif x == y:
        emp+=1
    while True:
        
        print('Novo grenal (1-sim 2-nao)')
        v=int(input())
        if v == 1:
            continuar=True
            break
        elif v == 2:
            continuar = False
            break
print('{} grenais' .format(cont))
print('Inter:{}' .format(inter))
print('Gremio:{}' .format(gre))
print('Empates:{}' .format(emp))
if gre > inter:
      print('Gremio venceu mais')
elif gre < inter:
    print('Inter venceu mais')
elif gre == inter:
    print('Nao houve vencedor')
    