#User Defined function

def greet():
    print("Good Morning Anurag!")

greet()
greet()
greet()
greet()
greet()

def call(name):
    print("Hi",name)

call("Anurag")
call("Amrit")

def bf(Name,dish = "goo"):      #by default goo khila rhe hn
    print("Hi",Name,"kaise ho ?")
    print(dish,"kha lo")

bf("Anurag","Chicken")
bf("Amrit")

def sum(a , b):
    return a+b

print(sum(3,4))

