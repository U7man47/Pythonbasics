#Basic Calculator
#Malik Usman Ahmad PIAIC98144
n1= int(input("Enter 1st number:"))
n2= int(input("Enter 2nd number:"))
op=input("Enter Operator that you want to perform + - / * of your choice: ")
if op=='+':
    print("Your Number Addition = ",n1 + n2)
elif op=='-':
    print("Your Number Subtraction = ",n1 - n2)
elif op=='/':
    if n2!=0:
        print("Your Number Division = ",n1 / n2)
    else:
        print("Division by 0 is not allowed")
elif op=='*':
    print("Your Number Multiplication = ",n1 * n2)
else:
    print("Please Enter Correct Operator")
