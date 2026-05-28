# school_class = {}

# while True:
#     name = input("Enter the student's name: ")
#     if name == "":
#         break

#     score = int(input(f"Enter ${name}'s score (0 - 10):")) # f-string used
#     if score not in range(1, 11):
#         break

#     if name in school_class:
#         school_class[name] += (score, )
#     else:
#         school_class[name] = (score, )


# for name , mark in school_class.items():
#     sum = 0
#     for m in mark:
#         # print(m)
#         sum += m
#     print(name, "->", sum/len(mark))
# print(school_class)


# for name in sorted(school_class.keys()):
#     marks = 0
#     number = 0
#     for score in school_class[name]:
#         marks += score
#         number += 1
#     print(name, ":", marks/number)


