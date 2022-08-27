# def square(num):
#     return num*num
# print(square(8))

# #building a better calculator
# num1 = float(input("enter first number:"))
# op = input("enter operator:")
# num2 = float(input("enter second number:"))

# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print (num1 * num2)
# else:
#    print("Invalid operator")

#Dictionaries are a special  structure in python that allows us to store information and key valued pair.
monthconversions = {"Jan": "January", "Feb": "February", "Mar": "March", }
print(monthconversions["Mar"])
print(monthconversions.get("Jan"))
#exponent function
print(2**3)
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(raise_to_power(3, 2))
#2D lists & Nested Loops
number_grid = [ 
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for x in number_grid:
    print(x)
    for y in x:
        print(y)


# print(number_grid[2][1])
# for row in number_grid:
#     print(row)
#     for col in row:
#         print(col) 

#translator
#Try except
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input")
#Reading files

