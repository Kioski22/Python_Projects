# entry = input("name, income, bday :")
# parts = entry.split(", ")
# print(parts[0])



list = [input("type: "), int(input("amount")), input("description: ")]
print(len(list))
print(list)

def split (list):
    for type in list:
        data = type.split(",")
        print("type = "+ data[1] , "amount = " + data[2] , "description = " + data[3])

split(list)
        
        
        
