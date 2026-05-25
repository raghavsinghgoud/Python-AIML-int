'''function'''

# def message():
#     print("Enter a value: ")

# print("Step 1")
# message()   #invocation / calling a function
# a = int(input())

# print("Step 2")
# message()
# b = int(input())

# print("Step 3")
# message()
# c = int(input())


'''Defining'''

# print("We start here.")
# message() #error at defining the function
# print("We end here.")
# def message():
#     print("Enter a value: ")


# def message():
#     print("Enter a value: ")

# message = 1 \3it will remove the function and change it to this vakue

# print("We start here.")
# print(message) #it will print it's memory allocation or address
# message()
# print("We end here.")


'''making our function to return something'''


# def message():
#     print("Enter a value: ")
#     temp = int(input())
#     return temp

# print("Step 1")
# a = message()

# print("Step 2")
# b = message()

# print("Step 3")
# c = message()

# print("a:", a)
# print("b:", b)
# print("c:", c)



'''type error'''
# def hi():
#     print("hi!")

# hi(5)



'''Arguments'''

# def hello(n): #defining a function
#     print("hello,",n) # body of the function

# name = input("Enter your name: ")
# hello(name) # calling the function


'''Parameters'''

# def message(number):
#     print("Enter a number: ", number)

# number = 1234
# message(1)
# print(number)



# def message(what, number):
#     print("Enter", what, "number", number)

# message("telephone", 11)
# message("price", 5)
# message("number", "number")
# message(11, "telephone")



# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name,last_name)

# introduction("Luke", "Skywalker")
# introduction("Jesse","Quick")
# introduction("Clark", "Kent")


'''keyword argument'''

# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name,last_name)

# introduction(first_name = "Luke",last_name= "Skywalker")
# introduction(last_name="Jesse",first_name="Quick")


'''input inside the function'''

# def message(number):
#     print("Enter a number: ")
#     number = int(input())
#     return number

# number = message(1)
# print(number)


'''mixing keyword arguments'''

# def adding(a,b,c):
#     print(a,"+",b,"+",c,"=",a+b+c)

# adding(1,2,3)
# adding(a=1,b=2,c=3)
# adding(3,c=1,b=2)
# adding(3,a=1,b=2) #type error


'''protected/ default value'''

# def intro(a="James Bond", b= "Bond"):
#     print("My name is " + b +"."+ a+ ".")
# intro()


'''return without an expression'''

# def happy_new_year(wishes = True):
#     print("Three...")
#     print("Two...")
#     print("One...")
#     if not wishes:
#         return
#     print("Happy New Year!")

# happy_new_year(False)
# happy_new_year(True)


'''return with an expression'''

# def boring_function():
#     print("'Boredom Mode' ON.")
#     return 123

# print("This lesson is interesting!")
# boring_function()
# print("This lesson is boring...")


'''None keyword'''

# print(None+1) # type error


# def checkMyVar(variable):
#     if(variable == 10):
#         print("Variable is 10")
#         return
#     else:
#         print("Variable is not up to the mark")
#         #return

# print(checkMyVar(5)) # will print none after the function because the function is called inside of print function 
# # checkMyVar(5)
# # print()



'''function with list'''

# def list_sum(lst):
#     s =0

#     for elem in lst:
#         s += elem

#     return s
# # print(list_sum([5,4,3]))
# print(list_sum(2)) # int error


'''list  making function'''

# def strange_list_fun(n):
#     strange_list = []

#     for i in range(0, n):
#         strange_list.insert(0, i+1)
#         # strange_list.append(i+1)
    
#     return strange_list

# print(strange_list_fun(5))


'''scopes function'''

