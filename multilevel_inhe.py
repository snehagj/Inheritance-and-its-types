class Parent1:
    def fun1(self):
        print("Parent1 method")
class Parent2(Parent1):
    def fun2(self):
        print("Parent2 method")
class Child(Parent2):                                           #multilevel inheritance
    def fun3(self):
        print("Child method")

ob=Child()
ob.fun1()
ob.fun2()
ob.fun3()