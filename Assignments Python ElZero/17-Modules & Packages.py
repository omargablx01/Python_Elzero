
# t~ >>>>                                                 Assignments  76 ==> 78                                            <<<<<
# ? --------------------------------- 1  -------------------------
# import random

# print(f"Random Number Between 10 And 50 => {random.randint(10,50)}")

# print(f"Random Even Number Between 2 And 10 => {random.randrange(2,10,2)}")

# print(f"Random Odd Number Between 1 And 9 => {random.randrange(1,9,2)}")

# print(dir(random))

# ? --------------------------------- 2  -------------------------
#! solving in folder >> 17-python
# import sys,os
# sys.path.append(os.path.dirname(__file__)) # @@ هنا عملنا اضافه للمكان الي احنا في علشان نقدر نستدعي المكتبه الي معانا في نفس المكان
# print(sys.path)


# t~ ------
# import my_mod

# print(my_mod.say_hello("NTFS"))
# print(my_mod.say_welcome("NTFS"))

# ? --------------------------------- 3  -------------------------
# from my_mod import say_welcome

# print(say_welcome("NTFS"))

# ? --------------------------------- 4  -------------------------
# from my_mod import say_welcome as new_welcome

# print(new_welcome("NTFS"))