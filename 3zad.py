a=int(input("введите a "))
b=int(input("введите b "))
c=int(input("введите c "))
if (a+b>c) and (a+c>b) and (b+c>a):
    print("треугольник с такими сторонами есть.")
else:
    print("треугольника с такими сторонами нет.")