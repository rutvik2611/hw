
from platform import python_version

from pip._vendor.distlib.compat import raw_input

a, b, c = 1, 2.01, 'string'
print(type(a), type(b), type(c))


p = 1 + 2j
q = 25
p, q = q, p
print(p)
print(q)


x = 6
y = 7

temp = x
x = y
y = temp

print(x)
print(y)



name = input("Please Enter Your Name HERE: ")
print(name, python_version())

name = raw_input("Enter your Name Here: ")
print(name)



num1, num2 = input("Enter any two numbers between 1 to 10: ").split(" ")
z = int(num1) + int(num2)
result = 30 + z
print("Final output:", result)



x = input("Enter any variable: ")
print(type(x))



# Upper CamelCase
NewVariable = 5

# Lower camelcase
newVariable = 7

# snake case
new_variable = 9


a = 5
print(a)

a = "string"
print(a)
