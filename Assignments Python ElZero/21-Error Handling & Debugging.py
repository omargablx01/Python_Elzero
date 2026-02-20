
# t~ >>>>                                                 Assignments  90 ==> 94                                            <<<<<
# ? --------------------------------- 1  -------------------------
# NUM = input("Add Your Number : ")

# if len(NUM) > 1 :
#     raise IndexError("Only One Character Allowed")

# elif NUM == "0" :
#     raise ValueError(f"Number Must Be Larger Than {NUM}")

# elif NUM.isupper() or NUM.islower():
#     raise Exception("Only Numbers Allowed")

# else :
#     print(f"The Number Is {NUM}")
# ! ----------- Some Way
# NUM = input("Add Your Number ")

# if len(NUM) >1:
#     raise IndexError("Only One Character Allowed")

# elif NUM.isalpha():
#     raise Exception("Only Numbers Allowed")

# elif int(NUM) == 0:
#     raise ValueError("Number Must Be Larger Than 0")

# elif NUM.isdigit():

#     print("#"*20)
#     print(f"The Number Is {NUM}")
#     print("#"*20)
# ? --------------------------------- 2  -------------------------
# LETTER = input("Add Letter From A to Z : ")

# try :

#     pass

# except:

#     pass

# else : 
#     if len(LETTER) > 1 :

#         print("You Must Write One Character Only")

#     elif LETTER.upper() != LETTER.upper():

#         print("The Letter Not In A - Z")
#     else :
#         print(f"You Typed {LETTER}")
# ! ------------- Some Way
# LETTER = input("Add Letter From A to Z : ")
# try:
#     if len(LETTER) != 1:
#         raise NameError
    
#     elif not LETTER.isupper():
#         raise IndexError
    
# except NameError:
#     print("You Must Write One Character Only")

# except IndexError:
#     print("The Letter Not In A - Z")

# else:
#     print(f"You Typed {LETTER}")
# ? --------------------------------- 3  -------------------------
# def calculate(num1, num2) -> int:
#   return num1 + num2

# print(calculate(20, 30))
