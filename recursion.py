#a recursive function is a function defined in terms of itself via self-refriential expressions.
#this means that the function will continue to call itself and repeat its behaviour until some condition is met to return a result.



def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
 
x = factorial(5)
print(x)


def tri_recursion(k):
    if(k>0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
# print(f"Recursion Example Results")
# tri_recursion(8)
