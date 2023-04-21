a=int(input("enter: "))
b=len(str(a))
temp=a
print("power",b)
sum=0
while(a!=0):
    rem=a%10
    sum+=pow(rem,b)
    a=a//10
if temp==sum:
    print("armstrong")
else:
    print("not armstrong")