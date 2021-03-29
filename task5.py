#q1

try:
   i=input("Enter R: ")
   x= i**2
   print(x)

except SyntaxError as error:
    print("Syntax Error! Try again!")