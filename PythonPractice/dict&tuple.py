# school_class = {}

# while True:
#     name = input("Enter the student's name: ")
#     if name == "":
#         break

#     score = int(input("Enter the student's score (0 - 10):"))
#     if score not in range(0, 11):
#         break

#     if name in school_class:
#         school_class[name] += (score, )
#     else:
#         school_class[name] = (score, )

# for name in sorted(school_class):
#     marks = 0
#     number = 0
#     for score in school_class[name]:
#         marks += score
#         number += 1
#     print(name, ":", marks/number)

