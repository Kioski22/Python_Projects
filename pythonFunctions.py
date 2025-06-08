# here answers my questions about functions in all programming languages


# def declares a function

# calculate() indicates the function name
# () indicates what data is needed in the function

def calculate (): 
# def declares a function
# calculate() indicates the function name
# () indicates what data is needed in the function (in simple words parameter says hey this is the data i need) in this case there is no parameter
    num1 = float(input("Enter your first number:  ")) #this stores the first number  and if data in the variable is a whole number python will convert it as float
    num2 = float(input("Enter your second number:  "))#this stores the second number  and if data in the variable is a whole number python will convert it as float
    operator = str(input("select your operator ( + , - , * , /   ) :"))
    
    
    if operator == "+": # this checks the condition that if the operator variable is equal to "+" 
        return print(num1+num2) #it will return the result and print it in the terminal
    elif operator == "-":
        return print(num1-num2)
    elif operator == "*":
        return print(num1*num2)
    elif operator == "/":
        return print(num1 / num2)
    else :
        print("there's something wrong with your code")
    
calculate()
 
 
 
 
 
 
#  def calculate(num1, num2, operator): 
#     if operator == "+":
#         return num1 + num2  this has no print in this because it will return the result  as
#     elif operator == "-":
#         return num1 - num2
#     elif operator == "*":
#         return num1 * num2
#     elif operator == "/":
#         return num1 / num2
#     else:
#         return "Invalid operator"

# # Collect inputs
# num1 = float(input("Enter your first number: "))
# num2 = float(input("Enter your second number: "))
# operator = input("Choose an operator (+, -, *, /): ")

# # Call the function with the inputs
# print(calculate(num1, num2, operator)) 


# Use return in functions, and keep print() outside if you want clean, flexible, professional code — especially for real-world projects.


# | Feature                     | Your Version (`calculate()`)  | Improved Version (`calculate(num1, num2, operator)`) |
# | --------------------------- | ----------------------------- | ---------------------------------------------------- |
# | Parameters used             | ❌ None                        | ✅ Accepts inputs via parameters                      |
# | Inputs inside function      | ✅ Yes (via `input()`)         | ❌ No (taken before calling the function)             |
# | Output with `print()`       | ✅ Yes (uses `print()` inside) | ❌ Returns value, and prints outside                  |
# | Reusability (in other code) | ❌ Hard to reuse               | ✅ Very reusable                                      |
# | Good separation of logic    | ❌ Mixed                       | ✅ Clean                                              |
# | Return + print (confusing)  | ⚠️ Yes: `return print(...)`   | ✅ Only uses `return`                                 |
