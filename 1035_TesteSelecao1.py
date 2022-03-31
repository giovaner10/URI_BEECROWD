t=input().split()
A=int(t[0])
B=int(t[1])
C=int(t[2])
D=int(t[3])

if B>C and D>A and (C+D)> (A+B) and C>=0 and D>=0 and (A%2)==0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
    
