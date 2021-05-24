a=int(input("enter the amount"))
if(a>2000):
     n=a//2000
     print("no 2000 of notes",n)
     a=a-2000*n
     print(a)
if(a>500):
     m=a//500
     print("number of 500 notes",m)
     a=a-500*m
     print(a)
if(a>200):
     l=a//200
     print("number of 200 notes",l)
     a=a-200*l
     print(a)
if(a>100):
     o=a//100
     print("number of 100 notes",o)
     a=a-100*o
     print(a)
if(a>50):
     h=a//50
     print("number of 50 notes",h)
     a=a-50*h
     print(a)
if(a>20):
     g=a//20
     print("number of 20  notes",g)
     a=a-20*g
     print(a)
if(a>10):
     f=a//10
     print("number of 10 notes",f)
     a=a-10*f
     print(a)
     
     
    
