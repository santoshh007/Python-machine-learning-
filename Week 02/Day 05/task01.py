class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def set_info(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def walk(self):
        print(f"{self.name} is walking.")

if __name__ == "__main__":
    cat = Animal(name="cat", species="Cat Family")
    cat.walk()
    cat.set_info(name="Tom", species="Felidae", age=3)
    print(f"Name: {cat.name}, Species: {cat.species}, Age: {cat.age}")
