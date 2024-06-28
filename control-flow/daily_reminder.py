# task_reminder.py

def main():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    reminder = f"'{task}' is a "

    match priority:
        case "high":
            reminder += "high priority task"
        case "medium":
            reminder += "medium priority task"
        case "low":
            reminder += "low priority task"
        case _:
            print("Invalid priority. Please enter high, medium, or low.")
            return

    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    elif time_bound == "no":
        reminder += "."
    else:
        print("Invalid input for time-bound. Please enter yes or no.")
        return

    print("Reminder:", reminder)

if __name__ == "__main__":
    main()

