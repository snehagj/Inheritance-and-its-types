class Animal:
    def sound(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("The dog barks.")

class GoldenRetriever(Dog):
    def sound(self):
        super().sound()
        print("The Golden Retriever is friendly in nature.")

my_dog = GoldenRetriever()
my_dog.sound()