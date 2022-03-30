v = float(input())
v = ("%.2f" % v)
v1 = float(v) % 100
v1 = ("%.2f" % v1)
v2 = float(v1) % 50
v2 = ("%.2f" % v2)
v3 = float(v2) % 20
v3 = ("%.2f" % v3)
v4 = float(v3) % 10
v4 = ("%.2f" % v4)
v5 = float(v4) % 5
v5 = ("%.2f" % v5)
v6 = float(v5) % 2
v6 = ("%.2f" % v6)
v7 = float(v6) % 1.00
v7 = ("%.2f" % v7)
v8 = float(v7) % 0.50
v8 = ("%.2f" % v8)
v9 = float(v8) % 0.25
v9 = ("%.2f" % v9)
v10 = float(v9) % 0.10
v10 = ("%.2f" % v10)
v11 = float(v10) % 0.05
v11 = ("%.2f" % v11)
print('NOTAS:')
print('%d nota(s) de R$ 100.00' % float((float(v)//100)))
print('%d nota(s) de R$ 50.00' % float((float(v1)//50)))
print('%d nota(s) de R$ 20.00' % float((float(v2)//20)))
print('%d nota(s) de R$ 10.00' % float((float(v3)//10)))
print('%d nota(s) de R$ 5.00' % float((float(v4)//5)))
print('%d nota(s) de R$ 2.00' % float((float(v5)//2)))
print('MOEDAS:')
print('%d moeda(s) de R$ 1.00' % float((float(v6)//1.00)))
print('%d moeda(s) de R$ 0.50' % float((float(v7)//0.50)))
print('%d moeda(s) de R$ 0.25' % float((float(v8)//0.25)))
print('%d moeda(s) de R$ 0.10' % float((float(v9)//0.10)))
print('%d moeda(s) de R$ 0.05' % float((float(v10)//0.05)))
print('%d moeda(s) de R$ 0.01' % float((float(v11)/0.01)))
