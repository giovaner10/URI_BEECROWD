N=int(input())
h=N//3600
N=N-h*3600
m=N//60
N=N-m*60
s=N//1
print(f'{h}:{m}:{s}')