def sort_odd_even(numbers):
    odd_numbers = []
    even_numbers = []

    for num in numbers:
        if isinstance(num, int) or isinstance(num, float):
            if num % 2 == 0:
                even_numbers.append(num)
            else:
                odd_numbers.append(num)

    return odd_numbers, even_numbers

def main():
    # Ask the user to input a list of numbers
    input_list = input("Enter a list of numbers (comma-separated): ").strip().split(',')

    # Convert input values to appropriate data types
    numbers = []
    for item in input_list:
        try:
            num = float(item)
            numbers.append(num)
        except ValueError:
            print(f"Skipping invalid input: {item}")

    # Sort the numbers into odd and even lists
    odd_numbers, even_numbers = sort_odd_even(numbers)

    # Display the sorted lists
    print("Odd Numbers:", odd_numbers)
    print("Even Numbers:", even_numbers)

if __name__ == "__main__":
    main()
