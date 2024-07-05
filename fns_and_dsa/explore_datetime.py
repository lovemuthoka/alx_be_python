from datetime import datetime

def display_current_datetime():
    # Obtain the current date and time
    current_date = datetime.now()
    
    # Format the current date and time in a readable format
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the formatted date and time
    print(f"The current date and time is: {formatted_date}")

# Call the function to display the current date and time
display_current_datetime()
from datetime import datetime, timedelta

def calculate_future_date(days):
    # Obtain the current date and time
    current_date = datetime.now()
    
    # Calculate the future date
    future_date = current_date + timedelta(days=days)
    
    # Format the future date in a readable format
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    
    # Print the future date
    print(f"The date after {days} days will be: {formatted_future_date}")

# Prompt the user to enter a number of days
days = int(input("Enter the number of days: "))

# Call the function to calculate and display the future date
calculate_future_date(days)

