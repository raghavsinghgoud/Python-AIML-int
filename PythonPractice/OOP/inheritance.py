# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy

# sun = Star("Sun", "Milky Way")
# print(sun)


'''__str__'''
# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy

#     def __str__(self):
#         return self.name + " in " + self.galaxy

# sun = Star("Sun", "Milky Way")
# print(sun)


'''Two Level Inheritance'''

# class Vehicle:
#     pass

# class LandVehicle(Vehicle):
#     pass

# class TrackedVehicle(LandVehicle):
#     pass


'''issubClass()'''

# for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
#     for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(issubclass(cls2,cls1), end="\t") # "\t" for next tab
#     print()


# class Super:
#     supVar = 1

# class Sub(Super):
#     subVar = 2

# obj = Sub()
# print(obj.subVar)
# print(obj.supVar)


'''with __init__'''


# class Super:
#     def __init__(self):  
#         self.supVar = 11

# class Sub(Super):
#     def __init__(self):
#        super().__init__()
#        self.subVar = 12

# obj = Sub()
# print(obj.subVar)
# print(obj.supVar)


'''Multi(Three)-Level Inheritance'''

# class Level1:
#     variable_1 = 100
#     def __init__(self):
#         self.var_1 = 101
#     def fun_1(self):
#         return 102
    

# class Level2(Level1):
#     variable_2 = 200
#     def __init__(self):
#         super().__init__()
#         self.var_2 = 201
#     def fun_2(self):
#         return 202
    

# class Level3(Level2):
#     variable_3 = 300
#     def __init__(self):
#         super().__init__()
#         self.var_3 = 301
#     def fun_3(self):
#         return 302
    
# obj = Level3()
# print(obj.variable_1, obj.var_1, obj.fun_1())
# print(obj.variable_2, obj.var_2, obj.fun_2())
# print(obj.variable_3, obj.var_3, obj.fun_3())


'''__str__ method'''

# class Super:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return "My name is "+ self.name+ "."

# class Sub(Super):
#     def __init__(self, name):
#         Super.__init__(self, name)
#         super().__init__(name) # super() method

# obj = Sub("Andy")
# print(obj)



'''Multiple Inheritance'''

# class SuperA:
#     var_a = 10
#     def fun_a(self):
#         return 11
    
# class SuperB:
#     var_b = 20
#     def fun_b(self):
#         return 21
    
# class Sub(SuperA, SuperB):
#     pass

# obj = Sub()
# print(obj.var_a, obj.fun_a())
# print(obj.var_b, obj.fun_b())


'''Method Overriding'''

# class Level1:
#     var = 100
#     def fun(self):
#         return 101
    
# class Level2(Level1):
#     var = 200
#     def fun(self):
#         return 201
    
# class Level3(Level2):
#     pass

# obj = Level3()
# print(obj.var, obj.fun())  # Level2's fun() method will override the Level1's 
                             # fun() method


'''Multiple Inheritance conflict on same level entity'''

# class Left:
#     var = "L"
#     var_left = "LL"
#     def fun(self):
#         return "Left"

# class Right:
#     var = "R"
#     var_right = "RR"
#     def fun(self):
#         return "Right"

# class Sub(Left, Right):
#     pass

# obj = Sub()
# print(obj.var, obj.var_left, obj.var_right, obj.fun())
#  When multiple superclasses have same entity, left-to-right order determines precedence


