k = int(input("Enter 4 digit number: "))
convert = str(k)
l = len(convert)

while l != 4:
    try:
        k = input("TOO LONG OR SHORT , Try AGAIN ")
        l = len(k)
    except ValueError:
        print("Value Error")