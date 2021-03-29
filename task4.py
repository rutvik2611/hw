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

      
def unique(lst):
    x = []
    for i in lst:
        if i not in x:
            x.append(i)
    return x
print(unique([1,2,3,4,43,2,11,3,3,2,3,4,2,4,5,6,7,7,8,6,78,8,8,88,99,]))


#q4 Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically

word = input("Enter word you want to be seprated by hyphen")
sortt = word.split("-")
sortt.sort()
print("-".join(sortt))

#q5 captilization

x3 = input("Word to be captalized:")
print(x3.upper())