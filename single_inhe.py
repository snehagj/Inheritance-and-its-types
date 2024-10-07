class Parent:
    def display(self):
        print("Parent class.")
class Child(Parent):                                 #single inheritance
    def display1(self):
        print("Child class")
ob = Child()
ob.display()
ob.display1()