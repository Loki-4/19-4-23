a=int(input("enter: "))
b=int(input("enter"))
c=int(input("enter"))
if a==b and a==c :
    print("same",a,b,c)
elif a<b and b<c:
    print("already in order")
else:
    if a>b and a>c:
        if b>c:
            print(c," ",b,"",a)
        else:
             print(b," ",c,"",a)
    elif b>a and b>c :
        if a>c:
             print(c," ",a,"",b)
        else:
             print(a," ",c,"",b)
    else:
        if a>b:
             print(b," ",a,"",c)
        else:
             print(a," ",b,"",c)