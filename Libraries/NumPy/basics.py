# import numpy as np # here np is a variable that is changeble or mutable

# arr1d = np.array([1,2,3,4,5])
# arr2d = np.array([[85,90,78],[72,88,95],[91,76,83]])

# print(arr2d.shape)  #(3,3)
# print(arr2d.dtype)  #int64
# print(arr2d.ndim)  #2 dimensional n=2

# zeros = np.zeros((3,4))   # (row , column)
# print(zeros)
# ones = np.ones((2,5))
# print(ones)
# ring = np.arange(0,50,5)
# print(ring)

# lin = np.linspace(0,1,11)
# print(lin)


# random = np.random.randint(40,100,(5,3))
# print(random)


'''array functions'''

# arr = np.array([10,20,30,40,50])

# print(arr*2)
# print(arr+5)
# print(arr**2)  # the output will have " "/spaces in place of ","


'''Statistics Operation'''

# marks_2d = np.array([[85,90,78],[72,88,95],[91,76,83]])

# print(np.mean(marks_2d))    # overall mean

# print(np.mean(marks_2d, axis=1))    # mean per student (row)

# print(np.mean(marks_2d, axis=0))    # mean per subject (column)

# print(np.max(marks_2d))     # Highest mark

# print(np.std(marks_2d))    #standard deviation


'''Boolean Indexing'''

# arr = np.array([56,82,43,91,67,78,35,88])

# print(arr[arr> 70])     # [82 91 78 88] - only greater than 70

