import math
import requests
import json

# Define the function for performing operations
def calculator():

  # Display the menu
  print("Welcome to the Advanced Calculator!")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Exponentiation")
  print("6. Square Root")
  print("7. Trigonometric Functions")
  print("8. Solve an equation")
  print("9. Exit")

  # Get the user's choice
  choice = int(input("Enter your choice (1-9): "))

  # Perform the selected operation
  if choice == 1:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("The sum is:", num1 + num2)
  elif choice == 2:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("The difference is:", num1 - num2)
  elif choice == 3:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("The product is:", num1 * num2)
  elif choice == 4:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("The quotient is:", num1 / num2)
  elif choice == 5:
    num1 = float(input("Enter the base number: "))
    num2 = float(input("Enter the exponent: "))
    print("The result is:", num1 ** num2)
  elif choice == 6:
    num = float(input("Enter the number: "))
    print("The square root is:", math.sqrt(num))
  elif choice == 7:
    num = float(input("Enter the angle in degrees: "))
    print("sin(", num, ") =", math.sin(math.radians(num)))
    print("cos(", num, ") =", math.cos(math.radians(num)))
    print("tan(", num, ") =", math.tan(math.radians(num)))
  elif choice == 8:
    equation = input("Enter the equation to solve: ")
    url = "https://api.mathsolver.microsoft.com/solve"
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': 'INSERT_YOUR_SUBSCRIPTION_KEY_HERE'
    }
    data = {
        'expression': equation
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_dict = json.loads(response.text)
    if response_dict['error'] is not None:
        print("Error:", response_dict['error'])
    else:
        print("Solution:", response_dict['solution'])
  elif choice == 9:
    print("Goodbye!")
    return
  else:
    print("Invalid choice!")

  # Ask the user if they want to perform another operation
  response = input("Do you want to perform another operation? (y/n): ")
  if response == 'y' or response == 'Y':
    calculator()
  else:
    print("Goodbye!")
    return

# Call the calculator function to start the program
calculator()
