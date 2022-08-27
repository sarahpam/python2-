#closures are these inner funtions that are enclosed within the outer function.
#closures can access variables present in the outer function scope.
#works with nested funtion i.e function within a function.
def outer(name):
#this is the enclosing function
    def inner():
    #this is the enclosed function,the inner function accessing
        print(name)
    return inner
#call the enclosing function 
myfunction = outer('sarah')
myfunction ()