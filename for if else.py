##a=int(input("enter the 1st sub marks:"))
##b=int(input("enter the 2nd sub marks:"))
##c=int(input("enter the 3rd sub marks:"))
##d=int(input("enter the 4th sub marks:"))
##e=int(input("enter the 5th sub marks:"))
##f=int(input("enter the 6th sub marks:"))
sum=0
for i in range(6):
    marks=int(input("enter the marks"))
    
    sum=sum+marks    
print("addition of marks",sum)
S=sum
P=S/6
print("percentage",P)
if(P>90):
    print("A+")
elif(P>80):
    print("A")
elif(P>700):
    print("B+")
elif(P>60):
    print("B")
elif(P>50):
    print("C+")
elif(P>40):
    print("c")
else:
    print("FAIL")

       
   
