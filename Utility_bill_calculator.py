print("welcome to your personal Utility Bill Calculator!")

name = input("may i know what your name would be ?: \n")
billType = input("what type of bill do you want to compute? (kwh, cm, gb): \n")
billType = billType.lower()
billAmount = int(input("input the bill amount"))

if billType == "kwh" and billAmount >= 100:
    print("you've entered and electricity bill")
    billTotal = billAmount * 1 + 3
    print("Hi! {name} your bill amount" + " " + str(billTotal))
    try:
        billTotal = billAmount + 8 
        print("Hi! {name} your bill amount" + " " + str(billTotal))
    except:
        print("there's something wrong")


elif billType == "cm" and billAmount !=0 :
    billTotal = billAmount * 20 
    print("Hi! {name} your bill amount" + " " + str(billTotal))
    try:
        billTotal = billAmount + 8 
    except ValueError:
        print("there's something wrong")

elif billType == "gb" and billAmount != 0:
    billTotal = billAmount * 20 
    print("Hi! {name} your bill amount" + " " + str(billTotal))
    try:
        billTotal = billAmount + 8 
    except ValueError:
        print("there's something wrong")
else :
    print ("check your code :>")

    




