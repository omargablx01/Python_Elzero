
# t~ >>>>                                                 Assignments  86 ==> 89                                            <<<<<
# ? --------------------------------- 1  -------------------------
# my_list = ["E", "Z", "R", 1, 2, 3]
# my_tuple = ("L", "E", "O")
# my_data = []

# for data in zip(my_list, my_tuple):

#     for my_string in data:

#         my_data.append(my_string)

# final_string = "".join(my_data).capitalize()

# print(final_string) # Elzero

# ! ----------- Prof Way
# my_list = ["E", "Z", "R", 1, 2, 3]
# my_tuple = ("L", "E", "O")
# my_data = []

# for data in zip(my_list,my_tuple):

#     my_data.extend(data)

# final_string="".join(my_data).capitalize()

# print(final_string)
# ? --------------------------------- 2  -------------------------
# my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
# my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
# my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
# my_data = []

# for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):

#     if type(item1) == int:

#         continue

#     my_data.append(item1)

# final_string="".join(my_data).capitalize()

# print(final_string)

# ! ------------ Some Way
# my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
# my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
# my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
# my_data = []

# for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):

#     my_data.append(item1)

#     if len(my_data) == len("Elzero"):

#         final_string=("".join(my_data)).capitalize()

# print(final_string)
# ? --------------------------------- 3  -------------------------
# from PIL import Image

# my_image = Image.open(r"E:\HACKING\Python\Assignments Python ElZero\elzero-pillow.png")

# # my_image.show()
# # @@      left,   upper,  right,  lower
# my_crop = (400,0,800,400)

# new_crop = my_image.crop(my_crop)

# change_color = new_crop.convert("L")

# change_color.show()

# change_color.save(r"E:\HACKING\Python\Assignments Python ElZero\change_color.png")

# ! Two Task ....

# from PIL import Image

# my_image = Image.open(r"E:\HACKING\Python\Assignments Python ElZero\elzero-pillow.png")

# my_crop = (0,400,1200,800)

# new_crop = my_image.crop(my_crop)

# rotate = new_crop.transpose(Image.Transpose.ROTATE_180)

# change_color = rotate.convert("L")

# change_color.show()

# change_color.save(r"E:\HACKING\Python\Assignments Python ElZero\change_color_rotate.png")
# ! ----------- Some Way
# from PIL import Image

# my_image = Image.open(r"E:\HACKING\Python\Assignments Python ElZero\elzero-pillow.png")

# my_Box2 = (0, 400, 1200, 800)

# myNewImage2 = my_image.crop(my_Box2)

# myConverted2 = myNewImage2.convert("L")

# myrotate= myConverted2.rotate(180)

# myrotate.show()

# myrotate.save(r"E:\HACKING\Python\Assignments Python ElZero\change_color_rotate2.png")
# ? --------------------------------- 4  -------------------------
# def say_hello_to(name):
#     """parameter(someone) => Person Name
#     Function To Say Hello To Anyone"""

#     return f"Hello {name}"

# print(say_hello_to.__doc__)

# help(say_hello_to)

# print(say_hello_to("NTFSx00"))
# ? --------------------------------- 5  -------------------------
# '''This For List Name Pepole'''
# my_friends = ["Ahmed","Osama","Sayed"]
# """MAke Function To Type names for List"""
# def say_hello(some_peoples) -> list:
#     '''Function To Type List Names'''
#     for some_one in some_peoples:
#         print(f"Hello {some_one}")
# say_hello(my_friends)
# @@ pylint.exe "E:\HACKING\Python\Assignments Python ElZero\pylint.py"
# ! Doneee >>>>  Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
