a=300
b=int(input("enter the speed"))
c=a/b
c=c*60
c=int(c)
hr=c/60
mn=c%60
print("req time is {}hrs and {}mins".format (hr,mn))
if((hr>=4)and(hr<5)):   
    print("speed is moderate")
elif(hr>=5):
    print("speed is low")
elif(hr<4):
    print("speed is fast")
    

