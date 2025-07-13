# Define a function to perform addition
def add(x, y):
  return x + y

# Define a function to perform subtraction
def subtract(x, y):
  return x - y

# Define a function to perform multiplication
def multiply(x, y):
  return x * y

# Define a function to perform division
def divide(x, y):
  return x / y

# Ask the user to choose an operation
print("Please choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take the user's choice as input
choice = input("Enter your choice (1/2/3/4): ")

# Check if the choice is valid
if choice in ("1", "2", "3", "4"):
  # Ask the user to enter two numbers
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))

  # Perform the operation based on the choice and print the result
  if choice == "1":
    print(num1, "+", num2, "=", add(num1, num2))
  elif choice == "2":
    print(num1, "-", num2, "=", subtract(num1, num2))
  elif choice == "3":
    print(num1, "*", num2, "=", multiply(num1, num2))
  elif choice == "4":
    print(num1, "/", num2, "=", divide(num1, num2))
else:
  # Print an error message if the choice is invalid
  print("Invalid choice")
