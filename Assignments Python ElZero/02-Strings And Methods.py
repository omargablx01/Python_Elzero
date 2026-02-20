
# t~ >>>>                                                 Assignments  11 ==> 18                                             <<<<<
# ? --------------------------------- 1  -------------------------

# name = "0ag_NTFSx01"
# age = 22
# country = "EGYPT"

# print("\"Hello '%s', How You Doing \\ \"\"\" Your Age Is \"%d\"\" + And Your Country Is: ' %s ' "%(name,age,country))

# print("\"Hello '{0}', How You Doing \\ \"\"\" Your Age Is \"{1}\"\" + And Your Country Is: ' {2} ' ".format(name,age,country))

# print(f"\"Hello '{name}', How You Doing \\ \"\"\" Your Age Is \"{age}\"\" + And Your Country Is: ' {country} ' ")

# "\"Hello \'{0:s}\', How You Doing \\ \"\"\" Your Age Is \"{1:d}\"\" + And Your Country Is : {2:s}".format(name, age, Country))

# print("\"Hello \'{n:s}\', How You Doing \\ \"\"\" Your Age Is \"{a:d}\"\" + And Your Country Is : {Country:s}".format(name="Omar", age=22, Country="Egypt"))

# print("\"Hello \'{0:s}\', How You Doing \n\ \"\"\" Your Age Is \"{1:d}\"\" + \nAnd Your Country Is : {2:s}".format(name, age, country))
# ? ---------------------------------  2  -------------------------
# name = "0ag_NTFSx01"
# age = 22
# country = "EGYPT"

# old_format = "\"Hello '%s', How You Doing \\ \n \"\"\" Your Age Is \"%d\"\" + \n And Your Country Is: ' %s ' "%(name,age,country)

# print("\"Hello '%s', How You Doing \\ \n \"\"\" Your Age Is \"%d\"\" + \n And Your Country Is: ' %s ' "%(name,age,country))
# print(old_format)
# print("_"*50)

# mid_format = "\"Hello '{0}', How You Doing \\ \n \"\"\" Your Age Is \"{1}\"\" + \n And Your Country Is: ' {2} ' ".format(name,age,country)
# print("\"Hello '{0}', How You Doing \\ \n \"\"\" Your Age Is \"{1}\"\" + \n And Your Country Is: ' {2} ' ".format(name,age,country))
# print(mid_format)

# print("_"*50)
# new_format = f"\"Hello '{name}', How You Doing \\ \n \"\"\" Your Age Is \"{age}\"\" + \n And Your Country Is: ' {country} ' "
# print(f"\"Hello '{name}', How You Doing \\ \n \"\"\" Your Age Is \"{age}\"\" + \n And Your Country Is: ' {country} ' ")
# print(new_format)

# ? ---------------------------------  3  -------------------------
# name = "Elzero"

# print(name[1]) # l
# print(name[2]) # z
# print(name[-1]) # o

# ? ---------------------------------  4  -------------------------
# name = "Elzero"

# print(name[1:4]) # lze
# print(name[::2]) # Ezr
# print(name[4::-2]) # rzE

# ? ---------------------------------  5  -------------------------
# name = "#@#@Elzero#@#@"
# print(name.strip("#@")) # Elzero
# ? ---------------------------------  6  -------------------------
# num1 ,num2,num3,num4,num5="9","15","130","950","1500"
# num2 ="15"
# num3 ="130"
# num4 ="950"
# num5 ="1500"
# print(num1.zfill(4)) # 0015
# print(num2.zfill(4)) # 0130
# print(num3.zfill(4)) # 0950
# print(num4.zfill(4)) # 1500

# ? ---------------------------------  7  -------------------------
# name_one = "Osama"
# name_two = "Osama_Elzero"
# print(name_one.rjust(20,"@")) # @@@@@@@@@@@@@@@Osama
# print(name_two.rjust(20,"@")) # @@@@@@@@Osama_Elzero
# ? ---------------------------------  8  -------------------------
# name_one = "OSamA"
# name_two = "osaMA"
# print(name_one.swapcase())
# print(name_two.swapcase())
# ? ---------------------------------  9  -------------------------
# msg = "I Love Python And Although Love Elzero Web School"
# print(msg.count("Love"))
# ? ---------------------------------  10  -------------------------
# msg = "Elzero"
# print(msg.index("z"))
# ? ---------------------------------  11  -------------------------
# msg = "I <3 Python And Although <3 Elzero Web School"
# print(msg.replace("<3","Love",1))
# ? ---------------------------------  12  -------------------------
# msg = "I <3 Python And Although <3 Elzero Web School"
# print(msg.replace("<3","Love"))
# ? ---------------------------------  13  -------------------------
# name = "NTFSx00"
# age = 29
# country = "China"
# print(f"My Name Is {name}, And My {age} Is 38, And My Country Is {country}")