print("calculator")
def cals():
    a=int(input("enter the no"))
    b=int(input("enter the no"))
    
    c=int(input("enter the choice"))
    if(c==1):
         Add=a+b
         print("Addition of no",Add)
    elif(c==2):
        sub=a-b
        print("subtraction of no",sub)
    elif(c==3):
        mul=a*b
        print("mul of no",mul)
    elif(c==4):
        div=a/b
        print("div of no",div)

            
print("prime no")
def prime():
    n=int(input("enter the no"))
    for i in range (2,n):
            
            if(n%i==0):
                print("not prime no")
                break
    else:
        print("Prime No")



print("swapping no")
def swap():
    a=int(input("enter the no of a"))
    b=int(input("enter the no of b"))
    q=a
    a=b
    b=q
    print("value of a after swapping of a",a)
    print("value of b after swapping of b",b)



print("odd even no")
def num():
    a=int(input("enter the no"))
    c=a%2
    if(c==1):
          print("no is odd",c)
    else:
          print("no is even")



print("factorial")
def facto():
    h=1
    a=int(input("enter the no:"))
    for i in range(1,a+1):
          h=h*i
          
    print("fact no",h)
          


    
    

         
















            
