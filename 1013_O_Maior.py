P=input().split()
A,B,C=P
Y=(int(A)+int(B)+abs(int(A)-int(B)))/2
MaiorAB=(int(C)+(Y)+abs(Y-int(C)))/2
print('%d eh o maior' %MaiorAB)