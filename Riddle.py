

import webbrowser

# Function to check the input and redirect or print a message
def check_input(user_input):
    if user_input == 128:
        webbrowser.open('https://tigps.in/')  # Replace with your desired URL
    else:
        print("Sorry my friend, but you are just a dumb fellow")

# Get user input
try:
    user_input = int(input("Enter a number: "))
    check_input(user_input)
except ValueError:
    print("Please enter a valid number.")
