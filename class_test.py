class Foo:
    def func1():
        print("function1")
    def func2(self):
        print(id(self))
        print("function2")
f3 = Foo()
print(id(f3))
Foo.func2(f3)
