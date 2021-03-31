string = "Consultadd Training"
def gen(string):
    s1 = " "
    for i in string:
        s1 = i + s1
        yield s1

reversedLetter = gen(string)
for i in range(len(string)):
    print(next(reversedLetter))