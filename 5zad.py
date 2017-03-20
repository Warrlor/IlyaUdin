x=int(input("введите число "))
print ("натуральные делители ")
for i in range(1,x):
    if (x%i == 0):
        print(i)
print(x)