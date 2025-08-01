try:
 def add(x, y):
 return x + y
def substract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def power(x, Y):
    return x ** Y
def modulus(x, y):
    return x % y
def calculator():
    print(" Welcome to the calculator !")
while True:
    print("Please select an operation!")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Exit!")
    choice = input("Enter your choice (1-6):")
    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", substract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", power(num1, num2))
        elif choice == '6':
            print("Result:", modulus(num1, num2))
        else:
            print("Invalid choice, please try again!")
except exception as e:
    print("An unsuggested error occured:", e)
