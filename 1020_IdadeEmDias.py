N=int(input())
a=N//365
N=N - a*365
m=N//30
N=N-m*30
d=N//1
print('%d ano(s)' %a)
print('%d mes(es)' %m)
print('%d dia(s)' %d)


