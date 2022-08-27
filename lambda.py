# A lambda functionis a small anonymous function.
# A lambda function can take any number of arguments,but can only have one expression.
# x = lambda a : a + 10
# print(x(5))
# x = lambda a,b : a * b
# print(x(5,6))
from binascii import a2b_base64


print((lambda a, b, c : a - b - c)(1,2,3))

def myfunc(n):
    return lambda a : a * n
#function expression.
# mydoubler = myfunc(2)
# another_doubler = myfunc(5)
# print(mydoubler(11))
# print(another_doubler(2))
#it's simpler and can be used to execute a program with just a line.

my_list = [2,5,8,67,44,21,90,506,33,31]
# my_even = []
# for e in my_list:
#     if e%2==0:
#         my_even.append(e)
# print(my_even)
# def my_even(x):
#     return x % 2 == 0
#higher order function (filter)
#filter(function, iterable)
# print(list(filter(lambda a: a%2==0, my_list)))
# print(list(filter(lambda a: a%2==1, my_list)))
#map returns an object which is an iterator of the result.
print(list(map(lambda x: pow(x,3), my_list)))


