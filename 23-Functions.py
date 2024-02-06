# # Python functions

# 1. Built-in
# 2. Modules
# 3. User-defined


##Built in functions 
# int() / float() / eval()
# input()
# min() / max()
# abs()
# type()
# len()
# round()
# range()

num_str = "123"
num_int = int(num_str)
print(num_int)  # Output: 123

num_str = "3.14"
num_float = float(num_str)
print(num_float)  # Output: 3.14

expression = "3 + 5"
result = eval(expression)
print(result)  # Output: 8

name = input("Enter your name: ")
print("Hello, " + name + "!")

numbers = [2, 7, 1, 9, 5]
min_value = min(numbers)
max_value = max(numbers)
print("Min:", min_value)  # Output: 1
print("Max:", max_value)  # Output: 9

num = -10
absolute_value = abs(num)
print(absolute_value)  # Output: 10

value = 42
print(type(value))  # Output: <class 'int'>

text = "Hello, World!"
length = len(text)
print(length)  # Output: 13

num = 3.75
rounded_num = round(num)
print(rounded_num)  # Output: 4

numbers = list(range(1, 6))
print(numbers)  # Output: [1, 2, 3, 4, 5]

