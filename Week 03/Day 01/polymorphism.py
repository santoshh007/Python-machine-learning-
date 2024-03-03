class French:
    def say_hello(self):
        print("Bonjour")

class Nepali:
    def say_hello(self):
        print("Namaskar")

def greet(lang):
    lang.say_hello()

# Create instances of different language classes
french = French()
nepali = Nepali()

# Call the greet function with different language objects
print("French:")
greet(french)

print("\nNepali:")
greet(nepali)
