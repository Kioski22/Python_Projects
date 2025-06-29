print("welcome to your personal Utility Bill Calculator!")

name = input("may i know what your name would be ?: \n")
billType = input("what type of bill do you want to compute? (kwh, cm, gb): \n")
billType = billType.lower(billType)
billAmount = int(input("input the bill amount"))

if billType == "kwh" and billAmount <= 100:
    print("you've entered and electricity bill")
    billTotal = billAmount * 10 / 10
    print ("your bill amout")
elif billAmount
    billTotal = billAmount * 20 /20

    




