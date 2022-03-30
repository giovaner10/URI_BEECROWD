v=int(input())
n=v
n100= v//100
v=v-n100*100
n50=v//50
v=v-n50*50
n20=v//20
v=v-n20*20
n10=v//10
v=v-n10*10
n5=v//5
v=v-n5*5
n2=v//2
v=v-n2*2
n1=v//1
print('%d' %n)
print('%d nota(s) de R$ 100,00' %n100)
print('%d nota(s) de R$ 50,00' %n50)
print('%d nota(s) de R$ 20,00' %n20)
print('%d nota(s) de R$ 10,00' %n10)
print('%d nota(s) de R$ 5,00' %n5)
print('%d nota(s) de R$ 2,00' %n2)
print('%d nota(s) de R$ 1,00' %n1)