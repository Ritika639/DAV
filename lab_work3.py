# 1 ZERODIVISIONERROR
num1=int(input("enter a number"))
num2=int(input("enter second number"))
try:
    print(num1/num2)
except ZeroDivisionError as e:
    print(e)
# 2 VALUEERROR
try:
    # Prompt the user to input two numbers
    num1 =int( input("Enter the first number: "))
    num2 = int( input("Enter the second number: "))

 

    # Print the numbers if they are successfully converted
    print(f"The numbers you entered are {num1} and {num2}")

except ValueError as e:
    # Raise a ValueError if the conversion fails
    print("Both inputs must be numerical values")
    
# 3 FILENOTFONDERROR 
try:
    open("anudips.txt")
except FileNotFoundError as e:
    print("file doesnot exist")

# 4 TYPEERROR

try:
    # Prompt the user to input two numbers
    a = int(input("Enter the first number: "))
    b= int(input("Enter the second number: "))

    # Try to convert inputs to float
    

    # Print the numbers if they are successfully converted
    print(f"The numbers you entered are {a} and {b}")

except (ValueError,TypeError) as e:
    # Raise a TypeError if the conversion fails
    print("Both inputs must be numerical values")

    
