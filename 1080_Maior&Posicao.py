cont=1
pos = 0
maior = -10**7
while cont <= 100:
    v=int(input())
    if maior < v:
        maior = v
        pos = cont
    cont+=1
print(maior)
print(pos)
