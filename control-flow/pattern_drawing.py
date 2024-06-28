# pattern_drawing.py

def draw_square_pattern(size):
    row = 0
    while row < size:
        for _ in range(size):
            print("*", end="")
        print()
        row += 1

def main():
    try:
        size = int(input("Enter the size of the pattern: "))
        if size <= 0:
            print("Please enter a positive integer.")
        else:
            draw_square_pattern(size)
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()

