while (True):
    Vin=int(input("enter the input voltage"))
    I=0.01
    ledr=(Vin-1.7)//I
    ledy=(Vin-2.2)//I
    ledg=(Vin-3.1)//I
    print("1.RED 2.Yellow 3.Green")
    x = int(input("Enter Your Led colour"))
    if(x==1):
        print(ledr)
    elif(x==2):
        print(ledy)
    elif(x==3):
        print(ledg)
