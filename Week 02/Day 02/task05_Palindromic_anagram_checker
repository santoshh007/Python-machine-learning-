#task05
#palindromic anagram checkersan
def can_form_palindrome(string):
    # Remove spaces and convert to lowercase
    string = string.replace(" ", "").lower()
    
    # Count the frequency of each character
    char_count = {}
    for char in string:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    
    # Count the number of characters with odd frequency
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
    
    # If the string has more than one character with odd frequency, it cannot form a palindrome
    return odd_count <= 1

def main():
    user_input = input("Enter a string: ")
    if not user_input:
        print("Empty input. Please enter a string.")
        return
    
    if can_form_palindrome(user_input):
        print("The given string can be rearranged to form a palindrome.")
    else:
        print("The given string cannot be rearranged to form a palindrome.")

if __name__ == "__main__":
    main()
