# class ThisIsMyFirstClass:
#     name = "Raghav" #property or attributes
#     age = 19
    
#     def getName(self): #method
#         print(self.name)

# firstObject = ThisIsMyFirstClass()
# print(firstObject)

# firstObject.getName() #calling method
# print(firstObject.name)



# class Student :
#     def __init__(self):  # __init__ is a contructor
#         self.name = ""
#         self.age = 0
#         self.gender = ""
#         self.grade = ""

# raghav = Student()
# print(raghav)

# raghav.name = "Raghav Singh Goud"
# raghav.age = 19
# raghav.gender = "Male"
# raghav.grade = "10th"

# print(raghav.name)
# print(raghav.age)
# print(raghav.gender)
# print(raghav.grade)

# print(raghav.__dict__) #creates a dictionary of object



# class Student :
#     def __init__(self, name, age, gender, grade):  # __init__ is a contructor
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.grade = grade

#     def printDetails(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Gender:",self.gender)
#         print("Grade:",self.grade)

# raghav = Student("Raghav Singh Goud", 19, "Male", "10th")
# print(raghav)

# raghav.printDetails()



'''CLASS CONTAINS  parameter method constructor
obj = Theclass() ()-> the contructor for creating the obj
implicit automatically receive
self is kis obj pr work ho rha h self obj

'''

'''class varible /static variable wrk with class not with obj'''
# class ExampleClass:
#     counter = 0
#     def __init__(self,val =1):
#         self.__first = val
#         ExampleClass.counter +=1  #class name with counter {static variable ****} 

# example_object_1  = ExampleClass()
# example_object_2  = ExampleClass(2)
# example_object_3  = ExampleClass(4)


# print(example_object_1.__dict__,example_object_1.counter)
# print(example_object_2.__dict__,example_object_2.counter)
# print(example_object_3.__dict__,example_object_3.counter)


'''we can put any logic inside our __init__ constructor rather then always intanciation'''
# class ExampleCls:
#     counter = 0
#     def __init__(self,val=1):
#         #self.__first = val
#         ExampleCls.counter += 1
#         if val % 2 != 0:
#             self.a = 1
        
#         else:
#             self.b = 1  #get an error for no attribute inside b 
# example_obj = ExampleCls(1)
# print(example_obj.a)
# print(example_obj.b)

'''exception handling try except'''
# class ExampleCls:
#     counter = 0
#     def __init__(self,val=1):
#         #self.__first = val
#         ExampleCls.counter += 1
#         if val % 2 != 0:
#             self.a = 1  #try with method
#         else:
#             self.b = 1  #get an error for no attribute inside b 
# example_obj = ExampleCls(1)
# #nested exection try catch 
# try: 
#     print("a=",example_obj.a)
# except AttributeError:
#     try:
#         print("b=",example_obj.b)
#     except AttributeError:
#        print("Error has occurs!slightly pass it") 

'''hasattr function(2 argumetn to be pas clsname,key/prop) ** checking the property exist inside the obj or not the result in form of true fales'''

# class ExampleCls:
#     counter = 0
#     def __init__(self,val=1):
#         #self.__first = val
#         ExampleCls.counter += 1
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1  #get an error for no attribute inside b 
# example_obj = ExampleCls(1)

# if hasattr(example_obj,'a'):
#     print("a=",example_obj.a)
# if hasattr(example_obj,'b'):
#     print("b=",example_obj.b)


'''passing class'''
# class ExampleCls:
#     counter = 0
#     def __init__(self,val=1):
#         #self.__first = val
#         ExampleCls.counter += 1
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1  #get an error for no attribute inside b 
# example_obj = ExampleCls(1)
# print(example_obj.a)
# print(example_obj.b)


# if hasattr(example_obj,'a'):
#     print("a=",example_obj.a)
# if hasattr(example_obj,'b'):
#     print("b=",example_obj.b)

# print(hasattr(ExampleCls,'b'))
# print(hasattr(ExampleCls,'a'))
'''__name for make is hidden'''

# class Python:
#     population = 1
#     victims = 0
#     def __init__(self):
#         self.length_ft = 3
#         self.__venomous = False

# myObj = Python()
# print("myobj.population",myObj.population)

# print("myobj.victims",myObj.victims)
# print("myobj.length_fr",myObj.length_ft)
# # print("myobj.__venomous",myObj.__venomous)
# print("myobj.venomous",myObj.venomous)

'''now accesing the hidden variable __name by using class name '''
# class Python:
#     population = 1
#     victims = 0
#     def __init__(self):
#         self.length_ft = 3
#         self.__venomous = False
# myObj = Python()

# print("myobj.population",myObj.population)
# print("myobj.victims",myObj.victims)
# print("myobj.length_fr",myObj.length_ft)
# # print("myobj.__venomous",myObj.__venomous)
# print("myobj.venomous",myObj._python.__venomous)

# class Python:
#     population = 1
#     victims = 0
#     version_2 =2
#     def __init__(self):
#         self.length_ft = 3
#         self.__venomous = False

# myObj = Python()
# print("myobj.population",myObj.population)
# print(hasattr(myObj.version_2))#***
# print("myobj.victims",myObj.victims)

'''abstraction'''
'''hidden method is also possible (hidden is abstraction)'''
'''name mangling in methods (accsesing hidden prop)'''
# class Classy:
#   def visible(self):
#     print("visible")

#   def __hidden(SELF):
#     print("hidden")

# obj =Classy()
# obj.visible()
# try:
#    obj.__hidden()
# except:
#   print("failed")
# obj._Classy__hidden()

# obj = Classy()
# print(type(obj))
# '''use to print the main class name'''
# print(type(obj).__name__)

'''is instance check whether the obj is blongs to the class or not'''
# class vehicle:
#     pass
# class LandVehicle(vehicle):
#     pass
# class trackedVechile(LandVehicle):
#     pass
# my_vehicle = vehicle()
# my_land_vehicle = LandVehicle()
# my_track_vehicle = trackedVechile()

# for obj in [my_vehicle,my_land_vehicle,my_track_vehicle]:
#     for cls in [vehicle,LandVehicle,trackedVechile]:
#         print(isinstance(obj,cls),end="\t") #*** check it belongs to the same clss the obj
#     print()

'''reference check using is'''

# class SampelClass:
#     def __init__(self,val):
#         self.val =val

# object_1 = SampelClass(0)
# object_2 = SampelClass(2)
# object_3 = object_1
# object_3.val += 1

# print(object_1 is object_2)
# print(object_2 is object_3)
# print(object_3 is object_1)
# print(object_1.val,object_2.val,object_3.val)

# string_1 = "Mary had a little "
# string_2 ="Mary had a little lamb"
# string_1 += "lamb"

# print(string_1 == string_2 , string_1 is string_2)


