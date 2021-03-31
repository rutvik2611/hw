string = "Consultadd Training"
def gen(string):
    s1 = " "
    for c in string:
        s1 = c + s1
        yield s1

reversedLetter = gen(string)
for i in range(len(string)):
    print(next(reversedLetter))