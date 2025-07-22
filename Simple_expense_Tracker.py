# "simple expense tracker "
# 🛠️ Key Concepts I’ll Practice:

# Functions for modular design
# Loops and conditional menus
# List of dictionaries for storing multiple expenses
# User input handling
# Optional: use datetime to add a date stamp for each expense
import datetime

Tracker = [
 
] 
 
 
while True: 
    print(
        "1. Add Expense\n" 
        "2. View Expenses\n" 
        "3. View Total\n"  
        "4. Exit"
    )
    options = input("What would you like to do ? : ")
   
    if options == "1" or options == "add expense":
         amount = input('input the corresponding ammount :')
         category = input('input category : ')
         note = input('input note : ')
         date = datetime.datetime.now()
         Tracker.append({
            "amount": amount,
            "category":category ,
            "note" :  note,
            "date" :  date
        })
    
    
    elif options == "2" or options == "view expenses":
         for index, expense in enumerate(Tracker , start=1):
              print(f"----------{index}-----------")
              print(expense["amount"])
              print(expense["category"])
              print(expense["note"])
              print(expense["date"])
              print("------------------------------")     
    elif options == "4" or options == "exit":
         print("thank you ! Have a nice day!")
         break

    elif options == "3" or options == "view total":
         total = 0 
         for expense in Tracker:
              total += float(expense["amount"])
         print("your total expenses are : " , total)




