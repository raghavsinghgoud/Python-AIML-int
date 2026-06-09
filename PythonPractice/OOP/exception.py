'''Exception with else'''

# def reciprocal(n):
#     try:
#         n= 1/n
#     except ZeroDivisionError:
#         print("Division Failed")
#         return None
#     else:
#         print("Everything went Fine")
#         return n

# print("-------------")
# print("reciprocal(2): ", reciprocal(2))
# print("-------------")
# print("reciprocal(0): ", reciprocal(0))
# print("-------------")

    
'''finally'''    

# def reciprocal(n):
#     try:
#         n= 1/n
#     except ZeroDivisionError:
#         print("Division Failed")
#         n = None
#     else:
#         print("Everything went Fine")
#     finally:
#         print("It's time to say goodbye")
#     return n


# print(reciprocal(2))
# print(reciprocal(0))



'''Exception as class'''

# try:
#     i = int("Hello!")
# except Exception as e:
#     print(e)
#     print(e.__str__())


'''Exception Tree'''

# def print_exception_tree(thisclass, nest = 0):
#     if nest > 1:
#         print("   |" * (nest - 1), end="")
#     if nest > 0:
#         print("   +---", end="")
#     print(thisclass.__name__)
#     for subclass in thisclass.__subclasses__():
#         print_exception_tree(subclass, nest + 1)
# print_exception_tree(BaseException)


'''Creating your own Exception'''

# class MyZeroDivisionError(ZeroDivisionError):
#     pass

# def do_the_division(mine):
#     if mine:
#         raise MyZeroDivisionError("some worse news")
#     else:
#         raise ZeroDivisionError("some bad news")
    
# do_the_division(False)

# 