#python program to findout the profit
#taking input from user
cp=float(input("enter the cost price(in RS)"))
sp=float(input("enter the  selling price(in RS)"))
#validating input
if(cp<0):
    print("price is invalid")
elif(sp<0):
    print("price is invalid")
    #calculating profit and loss
else:
    if(sp>cp):
        print("profit:Rs",(sp-cp))
    elif(cp>sp):
        print("loss Rs",(cp-sp))
    else:
        print("no profit no loss")