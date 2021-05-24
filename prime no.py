a=int(input("enter the no"))

for i in range(2,a):
    h=a%i
    if(h==0):
        print("value is not prime no")
        break
else:
        print("value is prime no")
