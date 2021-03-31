def myDecorator(functionCall):
    def innerFunc():
        print("Decorationn")
        functionCall()
        print("MORE decoration")  
    return innerFunc()
 
@myDecorator 
def myfunction():
    print("I am from the original Function")
