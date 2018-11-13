#############################################################################################################

# 5.1.8

# Write a class called "Burrito". A Burrito should have the
# following attributes (instance variables):
#
# - meat
# - to_go
# - rice
# - beans
# - extra_meat (default: False)
# - guacamole (default: False)
# - cheese (default: False)
# - pico (default: False)
# - corn (default: False)
#
# The constructor should let any of these attributes be
# changed when the object is instantiated. The attributes
# with a default value should be optional. Both positional
# and keyword attributes should be in the order shown above
#(for the autograder to work).


# Write your code here!

##############################################

# un-Comment From here

# class Burrito(object):
#     """docstring for Burrito"""

#     def __init__(self, meat, to_go, rice, beans, extra_meat=False, guacamole=False, cheese=False, pico=False, Corn=False):
#         self.meat = meat
#         self.to_go = to_go
#         self.rice = rice
#         self.beans = beans
#         self.extra_meat = extra_meat
#         self.guacamole = guacamole
#         self.cheese = cheese
#         self.pico = pico
#         self.corn = Corn


# # The code below will test your class. If it is written
# # correctly, this will print True, then False. Note,
# # though, that we'll test your code against more complex
# # test cases when you submit.
# newBurrito = Burrito("Tofu", True, True, True)
# print(newBurrito.to_go)
# print(newBurrito.guacamole)

# un-Comment to here

###################################################

#################################################################################################################################

# 5.19

# Copy your Burrito class from the last exercise. Now,
# write a getter and a setter method for each attribute.
# Each setter should accept a value as an argument. If the
# value is a valid value, it should set the corresponding
# attribute to the given value. Otherwise, it should set the
# attribute to False.
#
# Edit the constructor to use these new setters and getters.
# In other words, if we were to call:
#
# new_burrito = Burrito("spaghetti", True, True, False)
#
# new_burrito.meat would be False because "spaghetti" is not
# one of the valid options. Note that you should NOT try to
# check if the new value is valid in both the constructor and
# the setter: instead, just call the setter from the
# constructor using something like self.set_meat(meat).
#
# Valid values for each setter are as follows:
#
# - set_meat: "chicken", "pork", "steak", "tofu", False
# - set_to_go: True, False
# - set_rice: "brown", "white", False
# - set_beans: "black", "pinto", False
# - set_extra_meat: True, False
# - set_guacamole: True, False
# - set_cheese: True, False
# - set_pico: True, False
# - set_corn: True, False
#
# Make sure you name each setter with the format:
#"set_some_attribute" and "get_some_attribute"
#
# For example, the getter for meat would be get_meat. The
# getter for to_go would be get_to_go.
#
# Hint: Your code is going to end up *very* long. This
# will be the longest program you've written so far, but
# it isn't the most complex. Complexity and length are
# often very different!
#
# Hint 2: Checking for valid values will be much easier
# if you make a list of valid values for each attribute
# and check the new value against that.


# Write your code here!
##############################################
# Uncomment from Here

# class Burrito(object):
#     """docstring for Burrito"""

#     def __init__(self, meat, to_go, rice, beans, extra_meat=False, guacamole=False, cheese=False, pico=False, Corn=False):
#         self.set_meat(meat)
#         self.set_to_go(to_go)
#         self.set_rice(rice)
#         self.set_beans(beans)
#         self.set_extra_meat(extra_meat)
#         self.set_guacamole(guacamole)
#         self.set_cheese(cheese)
#         self.set_pico(pico)
#         self.set_corn(Corn)

#     def set_meat(self, meat):
#         if meat in ["chicken", "pork", "steak", "tofu"]:
#             self.meat = meat
#         else:
#             self.meat = False

#     def set_to_go(self, to_go):
#         if type(to_go) == bool:
#             self.to_go = to_go
#         else:
#             self.to_go = False

#     def set_rice(self, rice):
#         if rice in ["brown", "white"]:
#             self.rice = rice

#     def set_beans(self, beans):
#         if beans in ["black", "pinto"]:
#             self.beans = beans

#     def set_extra_meat(self, extra_meat):
#         if type(extra_meat) == bool:
#             self.extra_meat = extra_meat
#         else:
#             self.extra_meat = False

#     def set_guacamole(self, guacamole):
#         if type(guacamole) == bool:
#             self.guacamole = guacamole
#         else:
#             self.guacamole = guacamole

#     def set_cheese(self, cheese):
#         if type(cheese) == bool:
#             self.cheese = cheese

#     def set_pico(self, pico):
#         if type(pico) == bool:
#             self.pico = pico

#     def set_corn(self, corn):
#         if type(corn) == bool:
#             self.corn = corn
#         else:
#             self.corn = False

#     def get_meat(self):
#         return (self.meat)

#     def get_to_go(self):
#         return (self.to_go)

#     def get_rice(self):
#         return (self.rice)

#     def get_beans(self):
#         return (self.beans)

#     def get_extra_meat(self):
#         return(self.extra_meat)

#     def get_guacamole(self):
#         return(self.guacamole)

#     def get_cheese(self):
#         return(self.cheese)

#     def get_pico(self):
#         return (self.pico)

#     def get_corn(self):
#         return (self.corn)
#         # Feel free to add code below to test out the class that
#         # you've written. It won't be used for grading.

#     def get_cost(self):
#         base_cost = 5.0
#         if self.get_meat() in ["chicken", "pork", "tofu"]:
#             base_cost += 1.0
#         elif self.get_meat() == "steak":
#             base_cost += 1.5
#         if self.get_extra_meat() == True:
#             base_cost += 1.0
#         if self.get_guacamole() == True:
#             base_cost += 0.76
#         return (base_cost)


# # print: 7.75
# a_burrito = Burrito("pork", False, "white", "black", extra_meat=True, guacamole=True)
# print(a_burrito.get_cost())

# Un-Comment to here
#########################################

################################################################################################################


# 5.1.11


# Copy your Burrito class from the last exercise. Below,
# We've given you three additional classes named "Meat",
#"Rice" and "Beans." We've gone ahead and built getters
# and setters in these classes to check if the incoming
# values are valid, so you'll be able to remove those
# from your original code.
#
# First, edit the constructor of your Burrito class.
# Instead of calling setters to set the values of the
# attributes self.meat, self.rice, and self.beans, it
# should instead create new instances of Meat, Rice, and
# Beans. The arguments to these new instances should be
# the same as the arguments you were sending to the
# setters previously (e.g. self.rice = Rice("brown")
# instead of set_rice("brown")).
#
# Second, modify your getters and setters from your
# original code so that they still return the same value
# as before. get_rice(), for example, should still
# return "brown" for brown rice, False for no rice, etc.
# instead of returning the instance of Rice.
#
# Third, make sure that your get_cost function still
# works when you're done changing your code.
#
# Hint: When you're done, creating a new instance of
# Burrito with Burrito("pork", True, "brown", "pinto")
# should still work to create a new Burrito. The only
# thing changing is the internal reasoning of the
# Burrito class.
#
# Hint 2: Notice that the classes Meat, Beans, and Rice
# already contain the code to validate whether input is
# valid. So, your setters in the Burrito class no
# longer need to worry about that -- they can just pass
# their input to the set_value() methods for those
# classes.
#
# Hint 3: This exercise requires very little actual
# coding: you'll only write nine lines of new code, and
# those nine lines all replace existing lines of code
# in the constructor, getters, and setters of Burrito.
#
# You should not need to modify the code below.

# un-Comment from here

class Meat:
    def __init__(self, value=False):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value in ["chicken", "pork", "steak", "tofu"]:
            self.value = value
        else:
            self.value = False


class Rice:
    def __init__(self, value=False):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value in ["brown", "white"]:
            self.value = value
        else:
            self.value = False


class Beans:
    def __init__(self, value=False):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value in ["black", "pinto"]:
            self.value = value
        else:
            self.value = False


# Add and modify your code here!

class Burrito(object):
    """docstring for Burrito"""

    def __init__(self, meat, to_go, rice, beans, extra_meat=False, guacamole=False, cheese=False, pico=False, Corn=False):
        self.set_meat(meat)
        self.set_to_go(to_go)
        self.set_rice(rice)
        self.set_beans(beans)
        self.set_extra_meat(extra_meat)
        self.set_guacamole(guacamole)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(Corn)

    def set_meat(self, meat):
        # if meat in ["chicken", "pork", "steak", "tofu"]:
        #     self.meat = meat
        # else:
        #     self.meat = False
        meat_inst = Meat(meat)

    def set_to_go(self, to_go):
        if type(to_go) == bool:
            self.to_go = to_go
        else:
            self.to_go = False

    def set_rice(self, rice):
        # if rice in ["brown", "white"]:
        #     self.rice = rice
        rice_inst = Rice(rice)

    def set_beans(self, beans):
        # if beans in ["black", "pinto"]:
        #     self.beans = beans
        beans_inst = Beans()
        beans_inst.set_value(beans)

# 5.1.8

# Write a class called "Burrito". A Burrito should have the
# following attributes (instance variables):
#
# - meat
# - to_go
# - rice
# - beans
# - extra_meat (default: False)
# - guacamole (default: False)
# - cheese (default: False)
# - pico (default: False)
# - corn (default: False)
#
# The constructor should let any of these attributes be
# changed when the object is instantiated. The attributes
# with a default value should be optional. Both positional
# and keyword attributes should be in the order shown above
#(for the autograder to work).


# Write your code here!

##############################################

# un-Comment From here

# class Burrito(object):
#     """docstring for Burrito"""

#     def __init__(self, meat, to_go, rice, beans, extra_meat=False, guacamole=False, cheese=False, pico=False, Corn=False):
#         self.meat = meat
#         self.to_go = to_go
#         self.rice = rice
#         self.beans = beans
#         self.extra_meat = extra_meat
#         self.guacamole = guacamole
#         self.cheese = cheese
#         self.pico = pico
#         self.corn = Corn


# # The code below will test your class. If it is written
# # correctly, this will print True, then False. Note,
# # though, that we'll test your code against more complex
# # test cases when you submit.
# newBurrito = Burrito("Tofu", True, True, True)
# print(newBurrito.to_go)
# print(newBurrito.guacamole)

# un-Comment to here

###################################################

#################################################################################################################################

# 5.19

# Copy your Burrito class from the last exercise. Now,
# write a getter and a setter method for each attribute.
# Each setter should accept a value as an argument. If the
# value is a valid value, it should set the corresponding
# attribute to the given value. Otherwise, it should set the
# attribute to False.
#
# Edit the constructor to use these new setters and getters.
# In other words, if we were to call:
#
# new_burrito = Burrito("spaghetti", True, True, False)
#
# new_burrito.meat would be False because "spaghetti" is not
# one of the valid options. Note that you should NOT try to
# check if the new value is valid in both the constructor and
# the setter: instead, just call the setter from the
# constructor using something like self.set_meat(meat).
#
# Valid values for each setter are as follows:
#
# - set_meat: "chicken", "pork", "steak", "tofu", False
# - set_to_go: True, False
# - set_rice: "brown", "white", False
# - set_beans: "black", "pinto", False
# - set_extra_meat: True, False
# - set_guacamole: True, False
# - set_cheese: True, False
# - set_pico: True, False
# - set_corn: True, False
#
# Make sure you name each setter with the format:
#"set_some_attribute" and "get_some_attribute"
#
# For example, the getter for meat would be get_meat. The
# getter for to_go would be get_to_go.
#
# Hint: Your code is going to end up *very* long. This
# will be the longest program you've written so far, but
# it isn't the most complex. Complexity and length are
# often very different!
#
# Hint 2: Checking for valid values will be much easier
# if you make a list of valid values for each attribute
# and check the new value against that.


# Write your code here!
##############################################
# Uncomment from Here

# class Burrito(object):
#     """docstring for Burrito"""

#     def __init__(self, meat, to_go, rice, beans, extra_meat=False, guacamole=False, cheese=False, pico=False, Corn=False):
#         self.set_meat(meat)
#         self.set_to_go(to_go)
#         self.set_rice(rice)
#         self.set_beans(beans)
#         self.set_extra_meat(extra_meat)
#         self.set_guacamole(guacamole)
#         self.set_cheese(cheese)
#         self.set_pico(pico)
#         self.set_corn(Corn)

#     def set_meat(self, meat):
#         if meat in ["chicken", "pork", "steak", "tofu"]:
#             self.meat = meat
#         else:
#             self.meat = False

#     def set_to_go(self, to_go):
#         if type(to_go) == bool:
#             self.to_go = to_go
#         else:
#             self.to_go = False

#     def set_rice(self, rice):
#         if rice in ["brown", "white"]:
#             self.rice = rice

#     def set_beans(self, beans):
#         if beans in ["black", "pinto"]:
#             self.beans = beans

#     def set_extra_meat(self, extra_meat):
#         if type(extra_meat) == bool:
#             self.extra_meat = extra_meat
#         else:
#             self.extra_meat = False

#     def set_guacamole(self, guacamole):
#         if type(guacamole) == bool:
#             self.guacamole = guacamole
#         else:
#             self.guacamole = guacamole

#     def set_cheese(self, cheese):
#         if type(cheese) == bool:
#             self.cheese = cheese

#     def set_pico(self, pico):
#         if type(pico) == bool:
#             self.pico = pico

#     def set_corn(self, corn):
#         if type(corn) == bool:
#             self.corn = corn
#         else:
#             self.corn = False

#     def get_meat(self):
#         return (self.meat)

#     def get_to_go(self):
#         return (self.to_go)

#     def get_rice(self):
#         return (self.rice)

#     def get_beans(self):
#         return (self.beans)

#     def get_extra_meat(self):
#         return(self.extra_meat)

#     def get_guacamole(self):
#         return(self.guacamole)

#     def get_cheese(self):
#         return(self.cheese)

#     def get_pico(self):
#         return (self.pico)

#     def get_corn(self):
#         return (self.corn)
#         # Feel free to add code below to test out the class that
#         # you've written. It won't be used for grading.

#     def get_cost(self):
#         base_cost = 5.0
#         if self.get_meat() in ["chicken", "pork", "tofu"]:
#             base_cost += 1.0
#         elif self.get_meat() == "steak":
#             base_cost += 1.5
#         if self.get_extra_meat() == True:
#             base_cost += 1.0
#         if self.get_guacamole() == True:
#             base_cost += 0.76
#         return (base_cost)


# # print: 7.75
# a_burrito = Burrito("pork", False, "white", "black", extra_meat=True, guacamole=True)
# print(a_burrito.get_cost())

# Un-Comment to here
#########################################

################################################################################################################


# 5.1.11


# Copy your Burrito class from the last exercise. Below,
# We've given you three additional classes named "Meat",
#"Rice" and "Beans." We've gone ahead and built getters
# and setters in these classes to check if the incoming
# values are valid, so you'll be able to remove those
# from your original code.
#
# First, edit the constructor of your Burrito class.
# Instead of calling setters to set the values of the
# attributes self.meat, self.rice, and self.beans, it
# should instead create new instances of Meat, Rice, and
# Beans. The arguments to these new instances should be
# the same as the arguments you were sending to the
# setters previously (e.g. self.rice = Rice("brown")
# instead of set_rice("brown")).
#
# Second, modify your getters and setters from your
# original code so that they still return the same value
# as before. get_rice(), for example, should still
# return "brown" for brown rice, False for no rice, etc.
# instead of returning the instance of Rice.
#
# Third, make sure that your get_cost function still
# works when you're done changing your code.
#
# Hint: When you're done, creating a new instance of
# Burrito with Burrito("pork", True, "brown", "pinto")
# should still work to create a new Burrito. The only
# thing changing is the internal reasoning of the
# Burrito class.
#
# Hint 2: Notice that the classes Meat, Beans, and Rice
# already contain the code to validate whether input is
# valid. So, your setters in the Burrito class no
# longer need to worry about that -- they can just pass
# their input to the set_value() methods for those
# classes.
#
# Hint 3: This exercise requires very little actual
# coding: you'll only write nine lines of new code, and
# those nine lines all replace existing lines of code
# in the constructor, getters, and setters of Burrito.
#
# You should not need to modify the code below.

# un-Comment from here

class Meat:
    def __init__(self, value=False):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value in ["chicken", "pork", "steak", "tofu"]:
            self.value = value
        else:
            self.value = False


class Rice:
    def __init__(self, value=False):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value in ["brown", "white"]:
            self.value = value
        else:
            self.value = False


class Beans:
    def __init__(self, value=False):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value in ["black", "pinto"]:
            self.value = value
        else:
            self.value = False


# Add and modify your code here!

class Burrito(object):
    """docstring for Burrito"""

    def __init__(self, meat, to_go, rice, beans, extra_meat=False, guacamole=False, cheese=False, pico=False, Corn=False):
        self.meat = Meat(meat)
        self.set_to_go(to_go)
        self.rice = Rice(rice)
        self.beans = Beans(beans)
        self.set_extra_meat(extra_meat)
        self.set_guacamole(guacamole)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(Corn)

    # def set_meat(self, meat):
    #     # if meat in ["chicken", "pork", "steak", "tofu"]:
    #     #     self.meat = meat
    #     # else:
    #     #     self.meat = False
    #     meat_inst = Meat(meat)

    def set_to_go(self, to_go):
        if type(to_go) == bool:
            self.to_go = to_go
        else:
            self.to_go = False

    # def set_rice(self, rice):
    #     # if rice in ["brown", "white"]:
    #     #     self.rice = rice
    #     rice_inst = Rice(rice)

    # def set_beans(self, beans):
    #     # if beans in ["black", "pinto"]:
    #     #     self.beans = beans
    #     beans_inst = Beans(beans)

    def set_extra_meat(self, extra_meat):
        if type(extra_meat) == bool:
            self.extra_meat = extra_meat
        else:
            self.extra_meat = False

    def set_guacamole(self, guacamole):
        if type(guacamole) == bool:
            self.guacamole = guacamole
        else:
            self.guacamole = guacamole

    def set_cheese(self, cheese):
        if type(cheese) == bool:
            self.cheese = cheese

    def set_pico(self, pico):
        if type(pico) == bool:
            self.pico = pico

    def set_corn(self, corn):
        if type(corn) == bool:
            self.corn = corn
        else:
            self.corn = False

    def get_meat(self):
        # meat_inst.get_value()
        return (self.meat.get_value())

    def get_to_go(self):
        return (self.to_go)

    def get_rice(self):
        return (self.rice.get_value())

    def get_beans(self):
        return (self.beans.get_value())

    def get_extra_meat(self):
        return(self.extra_meat)

    def get_guacamole(self):
        return(self.guacamole)

    def get_cheese(self):
        return(self.cheese)

    def get_pico(self):
        return (self.pico)

    def get_corn(self):
        return (self.corn)
        # Feel free to add code below to test out the class that
        # you've written. It won't be used for grading.

    def get_cost(self):
        base_cost = 5.0
        if self.get_meat() in ["chicken", "pork", "tofu"]:
            base_cost += 1.0
        elif self.get_meat() == "steak":
            base_cost += 1.5
        if self.get_extra_meat() == True:
            base_cost += 1.0
        if self.get_guacamole() == True:
            base_cost += 0.75
        return (base_cost)



# Below are some lines of code that will test your class.
# You can change the value of the variable(s) to test your
# class with different inputs. Remember though, the results
# of this code should be the same as the previous problem:
# what should be different is how it works behind the scenes.
#
# If your function works correctly, this will originally
# print: 7.75
a_burrito = Burrito("pork", False, "white", "black", extra_meat=True, guacamole=True)
print(a_burrito.get_cost())


# In this exercise, you won't edit any of your code from the
# Burrito class. Instead, you're just going to write a
# function to use instances of the Burrito class. You don't
# actually have to copy/paste your previous code here if you
# don't want to, although you'll need to if you want to write
# some test code at the bottom.
#
# Write a function called total_cost. total_cost should take
# as input a list of instances of Burrito, and return the
# total cost of all those burritos together as a float.
#
# Hint: Don't reinvent the wheel. Use the work that you've
# already done. The function can be written in only five
# lines, including the function declaration.
#
# Hint 2: The exercise here is to write a function, not a
# method. That means this function should *not* be part of
# the Burrito class.


# If you'd like to use the test code, paste your previous
# code here.


# Write your new function here.
def total_cost(multiple_burritos=[]):
    Final_Cost = 0
    for every_burrito in multiple_burritos:
        Final_Cost += every_burrito.get_cost()
    return(Final_Cost)


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs. Note that these lines
# will ONLY work if you copy/paste your Burrito, Meat,
# Beans, and Rice classes in.
#
# If your function works correctly, this will originally
# print: 27.0
burrito_1 = Burrito("tofu", True, "white", "black")
burrito_2 = Burrito("steak", True, "white", "pinto", extra_meat=True)
burrito_3 = Burrito("pork", True, "brown", "black", guacamole=True)
burrito_4 = Burrito("chicken", True, "brown", "pinto", extra_meat=True, guacamole=True)
burrito_list = [burrito_1, burrito_2, burrito_3, burrito_4]
print(total_cost(burrito_list))
