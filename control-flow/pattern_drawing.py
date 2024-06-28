# pattern_drawing.py

def main():
    try:
        size = int(input("Enter the size of the pattern: "))
        if size > 0:
            for _ in range(size):
                print("*" * size)
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()

