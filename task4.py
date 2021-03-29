#q1 reverse string

x = "1234abcd"

def revstrng(y):
    return y[::-1]


print(revstrng(x))

#q2Write a function that accepts a string and prints the number of uppercase letters and lowercase letters

str = input('ENTER STRING FOR UPPER AND LOWER COUNTING')


def count(str):
    u = 0
    l = 0
    for i in str:
        if i.isupper():
            u += 1
        else:
            l += 1
    return  u,l


print(count(str))

#q3 Create a function that takes a list and returns a new list with unique elements of the first list