#q1
num=eval(input("Enter a number: "))
if num%3==0 and num%5==0:
    print("Consultadd - Python Training")

elif num%5==0:
    print("Python Training")

elif num%3==0:
    print("Consultadd")

#q2

print("Note: At a time user can only perform one action")
print("Enter your choice: ")
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")
print("5: Average")

choice=eval(input("Enter your choice: "))
num1=eval(input("Enter the first number: "))
num2=eval(input("Enter the second number: "))


while True:
    if choice==1:
        ans= num1+num2
        print("ans:", + ans)
        if ans<0:
            print("Negative")
        break
    
    elif choice==2:
        ans= num1-num2
        print("ans:",+ ans)
        if ans<0:
            print("Negative")
        break

    elif choice==3:
        ans= num1*num2
        print("ans:", + ans)
        if ans<0:
            print("Negative")
        break

    elif choice==4:
        ans= num1/num2
        print("ans:", + ans)
        if ans<0:
            print("Negative")
        break

    elif choice==5:
        num3=eval(input("Enter the third number: "))
        num4=eval(input("Enter the fourth number: "))
        ans= (num1+num2+num3+num4)/4
        print("ans:", + ans)
        if ans<0:
            print("Negative")
        break
    
    else:
        print("Enter the correct option")
        break

#q3

a=10
b=20
c=30
avg=(a+b+c)/3
print("avg=", avg)
if avg>a and avg>b and avg>c:
    print("avg is higher than a,b,c")
elif avg>a and avg>b:
    print("avg is higher than a,b")
elif avg>a and avg>c:
    print("avg is higher than a,c")
elif avg>b and avg>c:
    print("avg is higher than b,c")
elif avg>a:
    print("avg is just higher than a")
elif avg>b:
    print("avg is just higher than b")
elif avg>c:
    print("avg is just higher than c")

#q4

while True:
    n=int(input("Enter a number: "))
    if n<0:
        print("It's Over")
        break
    else:
        print("Good Going")
        continue
    
#q5


x=int(2000)
y=int(3200)
for i in range(x-1,y+1):
    if i%7==0 and i%5!=0:
        print(i)

#q6

x=[1,2,3]
for i in x:
    print(i)


i=0
while i<5:
    print(i)
    i+=1
    if i==3:
        break
    else:
        print("error")

count=0
while True:
    print(count)
    count+=1
    if count>=5:
        break


for i in range(0,6):
    if i==3 or i==6:
        continue
    print(i) 

#q8

str= input("Enter the string: ")
letter=0
digit=0
for i in str:
    if i.isalpha():
        letter+=1
    elif i.isdigit():
        digit+=1
print("Number of digits: ", digit)
print("Number of letters: ",letter)

#q9

Lucky_number=7
#number=int(input("Guess the lucky number: "))
while True:
    number=int(input("Guess the lucky number: "))
    if number==Lucky_number:
        print("Guess is correct!")
        break
    else:
        print("Your guess is wrong!")
    answer=input("Do you want to guess again: " )
    if answer=="no":
        break
    elif answer=="yes":
        continue

#q10


Lucky_number=7
counter=0
while counter<=5:
    number=int(input("Guess the lucky number: "))
    if number==Lucky_number:
        print("Good guess!")
    else:
        print("Try again!")
    counter=counter+1
    if counter==5:
        print("Game over!")
        break
