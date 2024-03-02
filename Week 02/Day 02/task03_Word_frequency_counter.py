#task 03
#word frequency counter
import string

def count_word_frequency(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenize the text into words
    words = text.split()
    
    # Initialize a dictionary to store word frequencies
    word_freq = {}
    
    # Count the frequency of each word
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    return word_freq

def display_word_frequency(word_freq):
    # Sort the word frequencies alphabetically by keys
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[0])
    
    # Display the word frequencies
    print("Word Frequency:")
    for word, freq in sorted_word_freq:
        print(f"{word}: {freq}")

def main():
    text = input("Enter a paragraph or sentence: ").strip()
    
    if not text:
        print("No input provided.")
        return
    
    word_freq = count_word_frequency(text)
    display_word_frequency(word_freq)

if __name__ == "__main__":
    main()
