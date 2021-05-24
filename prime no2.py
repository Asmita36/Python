a=int(input("enter the no"))
g=0
for i in range(2,a):
    h=a%i

    if(h==0):
        g=g+1

if(g==0):
        print("value is  prime no")
else:
        print("value is not prime no")
