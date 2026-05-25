# numbers = [10,5,7,2,1]

# print(numbers)
# print(type(numbers))


# print(numbers[0]+numbers[4])


# print(str(numbers[0])+str(numbers[4]))


# numbers = [10,5,7,2,1]
# print("first element content: ", numbers[0])
# print("second element content: ", numbers[1])
# print("third element content: ", numbers[2])
# print("fourth element content: ", numbers[3])
# print("fifth element content: ", numbers[4])


# numbers[0] = 111
# print("numbers[0]: ", numbers[0])
# print(numbers)

# numbers[1] = numbers[4]
# print(numbers)
# print(len(numbers))
# del numbers[3]
# print(numbers)
# print(len(numbers))

# print(numbers[-1])
# print(numbers[-2])
# print(numbers[-3])
# print(numbers[-4])
# print(numbers[-5]) error
# print(numbers[4]) error


# numbers = [1,2,3,4,5]
# list = len(numbers)
# print(len(numbers))
# del numbers[-1]
# x = int(input("Replace the middle number: "))
# numbers[list//2] = x
# print(numbers)


# my_list = [1,2,3,4,5,6,7,8,9,10]
# for iterator in range(len(my_list)):
#     print(my_list[iterator])


# list = []
# for iterator in range(1, 11):
#     # list.append(iterator)
#     list.insert(iterator, iterator)
#  or
# for iterator in range(10):
#     list.append(iterator+1)
# print(list)


# my_list = [10,20,30,40,50,60,70,80,90,100]
# for index in range(len(my_list)):
#     my_list[index] += 1
# print(my_list)


# my_list = [10,20,30,40,50,60,70,80,90,100]
# sum = 0
# for index in range(len(my_list)):
#     sum += my_list[index]
# print(sum)


# my_list = [10, 1 , 8, 3, 5]
# total =0

# for element in my_list:
#     total += element
# print(total)


# list_1 = [1]
# list_2 = list_1
# list_1[0] =2 
# print(list_1)
# print(list_2)


# list = [10,8,6,4,2]
# new_list = list[1:3]
# print(new_list)


# list = [10,8,6,4,2]
# new_list = list[1:-1]
# print(new_list)


# list = [10,8,6,4,2]
# new_list = list[-1:1]
# new_list = list[-5:3]
# new_list = list[:3]
# new_list = list[2:]
# print(new_list)


# list1 = [10,8,6,4,2]
# del list1[1:3]
# del list1
# del list1[:]
# print(list1)


# my_list = [0, 3, 12, 8, 2]
# print(5 in my_list)
# print(3 not in my_list)
# print(12 in my_list)


# row = []
# for i in range(8):
#     row.append("WHITE_PAWN")

# print(row)


# row = ["WHITE_PAWN" for i in range(8)]
# print(row)


# squares = [x**2 for x in range(10)]
# squares = [x**2 for x in range(1,11)]
# print(squares)


# twos = [2**index for index in range(8)]
# print(twos)


# squares = [x**2 for x in range(1,11)]
# odds = [x for x in squares if x%2 != 0]
# print(odds)


'''Two dimensional list/array'''
# board = []
# for i in range(8):
#     row = ["EMPTY" for i in range(8)]
#     board.append(row)

# # print(board)
# # for index in board:    #will print in matrix
# #     print(index)
# # print(len(board))

# # print(board[0][0])

# board [0][0] = "ROOK"
# board [0][7] = "ROOK"
# board [7][0] = "ROOK"
# board [7][7] = "ROOK"

# board [0][1] = "KNIGHT"
# board [0][6] = "KNIGHT"
# board [7][1] = "KNIGHT"
# board [7][6] = "KNIGHT"

# # print("--------------")

# for index in board:
#      print(index)


'''MULTI-DIMENSIONAL ARRAY/LIST'''
# temps = [[0.0 for h in range(24)] for d in range(31)]

# temp1 = 19
# temp2 = 32
# count = 0

# for days in temps:
#     if count ==0:
#         days[11] = temp1
#         count = 1
#     else :
#         days[11] = temp2
#         count = 0

# # for index in temps:
# #     print(index)

# total = 0.0
# for day in temps:
#     total += day[11]
# average = total/31
# print("Average temperature at noon:", average)

# highest = -100
# for days in temps:
#     for temp in days:
#         if temp > highest:
#             highest = temp

# print("The highest temperature was:", highest)


# hot_days = 0
# for day in temps:
#     if day[11] > 20.0:
#         hot_days += 1
# print(hot_days, "days were hot days in the month.")


'''Three Dimensional Array'''
# rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# # print(rooms)

# rooms[1][9][13] = True
# rooms[1][9][1]= True

# vacancy = 0
# for room_number in range(20):
#     if not rooms[1][9][room_number]:
#         vacancy += 1
# print("Vacancy in 3rd 15th floor of 3rd Building", vacancy)


