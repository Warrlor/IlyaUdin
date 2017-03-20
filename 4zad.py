a=int(input("от "))
b=int(input("до "))
c=int(input("дают остаток "))
d=int(input("при делении на "))
if a<b:
    print("в отрезок входят ")
    for i in range(a, b):
        if (i%d==c):
            print(i)
elif a>b:
    print("в отрезок входят ")
    for i in range(b, a):
        if (i%d==c):
            print(i)
else:
    print("нет чисел")