#list comprehension offers a shorter syntax when you want to create a new list based on the values of existing list.
# fruits = ["apple","banana","cherry","kiwi","mango"]
# newlist = [x for x in fruits if "e" in x]
# print(newlist)

# new = []

# for x in fruits:
#     if 'e' in x:
#         new.append(x)
# print(new)

nums = [1,2,4,5,7,8]
new_num = [x**2 for x in nums]
print(new_num)