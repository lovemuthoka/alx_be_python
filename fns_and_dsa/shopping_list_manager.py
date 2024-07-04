# shopping_list_manager.py

def display_menu():
    print("\nShopping List Manager")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the list")
    print("4. Exit")

def add_item(shopping_list):
    apple = input("Enter the item to add: ").strip()
    shopping_list.append(apple)
    print(f"'{apple}' has been added to the shopping list.")

def remove_item(shopping_list):
    ring = input("Enter the item to remove: ").strip()
    if ring in shopping_list:
        shopping_list.remove(ring)
        print(f"'{ring}' has been removed from the shopping list.")
    else:
        print(f"'{ring}' is not in the shopping list.")

def view_list(shopping_list):
    if shopping_list:
        print("\nCurrent Shopping List:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("\nThe shopping list is empty.")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
    
            print("Exiting the shopping list manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
