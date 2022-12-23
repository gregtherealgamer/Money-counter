# Define a dictionary to store the denominations and their corresponding values
denominations = {
  "penny": 0.01,
  "nickel": 0.05,
  "dime": 0.1,
  "quarter": 0.25,
  "dollar": 1.0
}

# Initialize a variable to store the total value of the money
total_value = 0

# Prompt the user for input
print("Enter the denominations and quantities, separated by a space (e.g. 'penny 10', 'dollar 1').")
print("Enter 'done' when you are finished.")

# Continuously prompt the user for input until they enter 'done'
while True:
  # Get the input from the user
  input_str = input()

  # Check if the user entered 'done'
  if input_str.lower() == "done":
    # If the user entered 'done', break out of the loop
    break

  # Split the input string into a denomination and a quantity
  denomination, quantity = input_str.split()

  # Convert the quantity to an integer
  quantity = int(quantity)

  # Add the value of the denomination to the total value
  total_value += denominations[denomination] * quantity

# Print the total value of the money
print("Total value: $" + str(total_value))
