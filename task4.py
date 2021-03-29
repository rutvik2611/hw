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

#q6

def sum(a, b):
    a1 = int(a)
    a2 = int(b)
    total = a1 + a2
    print(total)
j,z=input("no1"),input("no2")
print(sum(j,z))

#q7

str1=input("string1")
str2=input("string2")

def longer(s1,s2):
    l1,l2=len(s1),len(s2)
    if l1>l2:
        return(s1)
    elif l1==l2:
        return(s1 + "/n" + s2)
    else:
        return(s2)

print(longer(str1,str2))

#q8 tuples

def tu():
    a1 = range(1, 21)
    k = []
    for i in a1:
        a = i * i
        k.append(a)
    return tuple(k)


print(tu())

#q9 show num

def showNumbers(userNum):
    x7 = range(0,  userNum + 1)
    for i in x7:
        if i % 2 == 0:
            print(i, "EVEN")
        else:
            print(i, "ODD ")


Maxnumber = int(input("enter number for odd even : "))
showNumbers(Maxnumber)

#q10fiter

x8 = range(1, 21)
odd = filter(lambda x: x % 2 != 0, x8) 
print("Odd", list(odd))


even = filter(lambda x: x % 2 == 0, x9) 
print("Even",list(even))

#q11

x=filter(lambda y:y%2==0,range(1,11))
y=list(x)

square=map(lambda z:z**2, y )
print(list(square))

#q12

def fun():
    n=int(input("Enter the value of Divident: "))
    y=int(input("Enter the value of Divisor: "))
    try:
        x=n/y
        return x
    except:
        print("Error dividing by zero")


print(fun())

