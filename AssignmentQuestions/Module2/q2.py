'''Write a program to print a series like this:
1, 2, 3, 4, 5….50
1, t, 3, t, 5, t, 7, t, 9……50
1, 2, t, 4, 5, t, 7, 8, t…..50
1, 2, fiz, 4, buz, fiz, 7, 8, fiz, buz, 11, fiz, 13, 14, fizbuz, 16……50'''

# for iterator in range(1, 51):
#     if iterator == 50:
#         print(iterator)
#     else:
#         print(iterator, end=", ")

# for iterator in range(1, 51):
#     if iterator == 50:
#         print(iterator)  
#     elif iterator % 2 == 0:
#         print("t", end=", ")
#     else:
#         print(iterator, end=", ")

# for iterator in range(1,51):
#     if iterator == 50:
#         print(iterator)
#     elif iterator %3 == 0:
#         print("t", end=", ")
#     else:
#         print(iterator,end=", ")

# for iterator in range(1,51):
#     if iterator == 50:
#         print(iterator)
#     elif iterator % 3== 0 and iterator % 5==0:
#         print("fizbuz", end=", ")
#     elif iterator% 3==0:
#         print("fiz" , end= ", ")
#     elif iterator%5 == 0:
#         print("buz",end=", ")
#     else:
#         print(iterator,end=", ")

