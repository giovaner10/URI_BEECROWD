n=input().split()
a,b,c,d=n
a=float(a)
b=float(b)
c=float(c)
d=float(d)


m=(2*a+3*b+4*c+d)/10
print('Media: %0.1f' %m)
if m>=7:
    print('Aluno aprovado.')
elif m<5:
    print('Aluno reprovado.')
elif 5 <=m and m<=6.9:
    print('Aluno em exame.')
    ne=float(input())
    print('Nota do exame: %0.1f' %ne)
    mf= (ne+m)/2
    if mf >=5:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(mf))
    else:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(mf))
    