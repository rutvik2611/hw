
#q1
mylist= [1,2,'apple','dog',1j,3j,5.7,3.0,10,'fish']
#q2
myList = [1, 2, 3, 4, 5]
print(myList[1:3])
print(myList[1:5:2])
print(myList[::-1])

#q3
a = [1, 2, 3, 4, 5]
def sumMyList(k):
    add = 0
    for i in a:
        add += i
    return add


def multiplyMyList(k1):
    mul = 1
    for i in a:
        mul *= i
    return mul


print("Sum of list is: ", sumMyList(a))
print("Multiply of list is: ", multiplyMyList(a))

#q4

a = [1, 2, 3, 4, 5, 4, 10, 100, 20003, 200, 12, -9, -100, -124, 90]


def Large(a):
    large = a[0]
    for i in a:
        if i > large:
            large = i
    return large


print("Largest element in list is: ", Large(a))


def Small(a):
    small = a[0]
    for i in a:
        if i < small:
            small = i
    return small


print("Smallest element in list is: ", Small(a))

#q5

a = [1, 2, 3, 4, 5, 4, 10, 100, 20003, 200, 12, -9, -100, -124, 90]


def Large(a):
    large = a[0]
    for i in a:
        if i > large:
            large = i
    return large


print("Largest element in list is: ", Large(a))


def Small(a):
    small = a[0]
    for i in a:
        if i < small:
            small = i
    return small


print("Smallest element in list is: ", Small(a))

#q5

mylist = [4, 5, 3, 9, 1, 2]

result = []
for x in mylist:
    if x % 2 != 0:
        result.append(x)

print(result)

#q6

mylist = []
for x in range(1, 31):
    if x < 6 or x > 25:
        mylist.append(x ** 2)

print(mylist)

#q7

num1 = [1, 3, 5, 7, 9, 10]
num2 = [2, 4, 6, 8]
num1[-1:] = num2
print(num1)

#q9
n = int(input("Please enter number: "))
d = {}

for x in range(1, n + 1):
    d[x] = x * x

print(d)