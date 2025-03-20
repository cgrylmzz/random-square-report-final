import random
import math
import time
from datetime import datetime

def random_square_report():
    while True:
        try:
            # Ask for the first number input from the user
            number_1 = input("Enter 1st number (press 'q' to quit): ")
            
            # If user presses 'q' or 'Q', exit the application
            if number_1.lower() == 'q':
                print("Application is closing...")
                time.sleep(2)
                print("Application is closed.")
                break

            # Ask for the second number input
            number_2 = input("Enter 2nd number (press 'q' to quit): ")
            
            # If user presses 'q' or 'Q' here as well, allow exit
            if number_2.lower() == 'q':
                print("Application is closing...")
                time.sleep(2)
                print("Application is closed.")
                break

            # Convert input values to float
            number_1 = float(number_1)
            number_2 = float(number_2)

            # Check if both numbers are integers
            if not number_1.is_integer() or not number_2.is_integer():
                print("Error: Please enter an integer number!")
                continue

            # Check if lower limit is greater than the upper limit
            elif number_1 > number_2:
                print("Error: The lower limit cannot be greater than the upper limit!")
                continue

            # Check if numbers are positive
            elif number_1 < 0 or number_2 < 0:
                print("Error: Please enter positive numbers!")
                continue

            else:
                # Generate a random number between the given limits
                random_number = random.randint(int(number_1), int(number_2))
                print("Generating random number...")
                time.sleep(2)
                print(f"Our randomly selected number: {random_number}")

                # Calculate the square of that random number
                print("Calculating square...")
                time.sleep(3)
                square_number = math.pow(random_number, 2)  # Calculate the square of the randomly selected number 
                print(f"The square of the randomly selected number is: {square_number}")

            # Get the current date and time
            now_date = datetime.now()
            # Format the date and time as DD-MM-YYYY HH:MM:SS
            format_now_time = now_date.strftime("%d-%m-%Y %H:%M:%S")
            # Print the date and time of the transaction
            print(f"The transaction was completed on:\n{format_now_time}")

        except ValueError:
            # Catch non-numeric input errors
            print("Error: Please enter a valid number!")

# Call the main function
random_square_report()