
# todo >>>>                                                 Assignments  24 ==> 25                                            <<<<<
# ? --------------------------------- 1  -------------------------
# type_name = "0ag_ntfsx00",

# print(type_name)
# print(type_name[0])
# print(type(type_name))

# ? --------------------------------- 2  -------------------------
# ! هذا الحل ينفع ولكن يجعل ال tuple عباره عن STring 
# friends = ("Osama", "Ahmed", "Sayed")

# print(f"{friends}".replace("Osama", "Elzero"))  # ("Elzero", "Ahmed", "Sayed")
# replace_first = f"{friends}".replace("Osama", "Elzero")
# print(replace_first)  # ("Elzero", "Ahmed", "Sayed")
# print(type(friends)) # <class 'tuple'>
# print(len(friends)) # 3

# ! ---- OR ----
# ? هذا هو الحل الصحيح لان نوع البيانات بهذا الشكل عباره عن tuple
# friends = ("Osama", "Ahmed", "Sayed")
# new_list = list(friends)
# new_list[0] = "Elzero"
# new_tuple = tuple(new_list)

# print(new_tuple) # ('Elzero', 'Ahmed', 'Sayed')
# print(type(new_tuple)) # <class 'tuple'>
# print(len(new_tuple)) # 3
# # ? --------------------------------- 3  -------------------------
# nums = (1, 2, 3)
# letters = ("A", "B", "C")
# nums_and_letters_one = nums+letters
# print(nums_and_letters_one) # (1, 2, 3, 'A', 'B', 'C')
# print(len(nums_and_letters_one)) # 6
# ? --------------------------------- 4  -------------------------
# my_tuple = (1, 2, 3, 4)
# a,b,_,d = my_tuple

# print(a)
# print(b)
# print(d)