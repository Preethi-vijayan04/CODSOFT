num1=float(input("Enter a num1: "))
num2=float(input("Enter a num2: "))
print("Enter a choice: ")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice=input("Enter a choice(1/2/3/4): ")
if choice == "1": 
    print("Result:",num1 + num2)
elif choice == "2":
    print("Result:",num1 - num2)
elif choice == "3":
    print("Result:",num1 * num2)
elif choice == "4":
    print("Result:",num1 / num2)
else:
    print("Invalid choice!")                