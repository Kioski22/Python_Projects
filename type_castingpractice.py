# this is a personal budget tracker
name = input('enter your name : ')
expense = []

def storeExpense (name, expense):
    print(f"\n Hi! {name} please start entering your expenses or income thank you <3")
    print ("use this format to enter your expenses (amount, description)")
    print("type 'done' when you are finished ")
    while True:
       addExpense = input('please enter your expense or income: ')
       if addExpense.lower() == "done":
           break
       try:
           amountString , description = addExpense.split(", ")
           amountString = float(amountString)
           expense.append({"amount": amountString , "description": description})
       except ValueError:
           print("oh no  you've entered a wrong value :<")
storeExpense(name, expense)
print("\nYour Recorded Expense/Income")
for item in expense:
    print(f"{item['description']}:  ₱{item['amount']}")

total = 0
for item in expense:
    total += item['amount']

print(f"\nTotal: ₱{total}")

           
           
           
       
 
            
               
           
       