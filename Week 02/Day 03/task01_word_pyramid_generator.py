def generate_word_pyramid(word, direction='up'):
    word_length = len(word)
    if direction == 'down':
        start = word_length
        step = -1
    else:
        start = 1
        step = 1

    for i in range(start, start + word_length, step):
        spaces = ' ' * (word_length - i)  # Add spaces for centering
        if direction == 'down':
            print(spaces + word[:i])
        else:
            print(spaces + word[:i].center(word_length))

def main():
    # Ask user for input word
    word = input("Enter a word: ").strip()

    # Validate input word
    if not word.isalpha():
        print("Invalid input. Please enter a valid word.")
        return

    # Ask user for direction
    direction = input("Enter direction (up/down): ").strip().lower()
    if direction not in ['up', 'down']:
        print("Invalid direction. Please enter 'up' or 'down'.")
        return

    # Generate and print word pyramid
    print("\nWord Pyramid:")
    generate_word_pyramid(word.upper(), direction)

if __name__ == "__main__":
    main()
