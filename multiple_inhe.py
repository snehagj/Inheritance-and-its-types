class Parent1:
    def fun1(self):
        print("Parent1 method")

class Parent2:
    def fun2(self):
        print("Parent2 method")

class Child(Parent1, Parent2):
    def fun3(self):
        print("Child method")

ob = Child()

ob.fun1()
ob.fun2()
ob.fun3()