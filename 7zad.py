x=float(input("пробежал в первый день "))
y=float(input("всего киллометров "))
d=int(1)
while x<=y:
   x=x*0.1+x
   d=d+1
print("номер дня: ",d)