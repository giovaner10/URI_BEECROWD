p=input().split()
x,y,z=p
x=int(x)
y=int(y)
z=int(z)

if x>y and x>z:
    a=x
    if y>z:
        b=y
        c=z
    else:
        b=z
        c=y
elif y>x and y>z:
    a=y
    if x>z:
        b=x
        c=z
    else:
        b=z
        c=x
elif z>x and z>y:
    a=z
    if x>y:
        b=x
        c=y
    else:
        b=y
        c=x
print(c)
print(b)
print(a)
print()
print(x)
print(y)
print(z)