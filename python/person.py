class Person:
    def __init__(self,name):
        print("Hello,I'm {}!".format(name))
    def say_hello(self):
        print("Hello")
    def greet(self,name="Person"):
        return "Hello {}".format(name)