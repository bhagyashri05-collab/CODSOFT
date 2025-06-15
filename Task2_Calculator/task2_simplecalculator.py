first = input("Enter the first number: ")
second = input("Enter the second number: ")

num1 = float(first)
num2 = float(second)

while True:
    
    print("\nWhat would you like to do?")
    print("+ for Addition")
    print("- for Subtraction")
    print("* for Multiplication")
    print("/ for Division")
    print("x to Exit")

    choice = input("Enter your choice: ")

    if choice == "+":
        print("-------------------------------")
        print("The result of ADDITION is:", num1 + num2)
        print("-------------------------------")
    elif choice == "-":
        print("-------------------------------")
        print("The result of SUBTRACTION is:", num1 - num2)
        print("-------------------------------")
    elif choice == "*":
        print("-------------------------------")
        print("The result of MULTIPLICATION is:", num1 * num2)
        print("-------------------------------")
    elif choice == "/":
        if num2 == 0:
            print("-------------------------------")
            print("Oops! Can't divide by zero")
            print("-------------------------------")
        else:
            print("-------------------------------")
            print("The result of DIVISION is:", num1 / num2)
            print("-------------------------------")
    elif choice.lower() == "x":
        print("-------------------------------")
        print("Exiting the calculator!")
        print("-------------------------------")
        break
    else:
        print("-------------------------------")
        print("Invalid choice. Try again!")
        print("-------------------------------")
