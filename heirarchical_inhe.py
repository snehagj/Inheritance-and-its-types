class Parent:
    def fun1(self):
        print("Parent method")
class Child1(Parent):
    def fun2(self):
        print("Child 1 method")
class Child2(Parent):
    def fun3(self):
        print("Child 2 method")

ob = Child1()
ob.fun1()
ob.fun2()

ob = Child2()
ob.fun1()
ob.fun3()
