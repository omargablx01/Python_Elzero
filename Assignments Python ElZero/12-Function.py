
# todo >>>>                                                 Assignments  56 ==> 59                                            <<<<<
# ? --------------------------------- 1  -------------------------
# def calculate(number1,number2,operation = "add"):
#     operation = operation.lower()

#     if operation in ['add',"a","+"]:

#         print(f"{number1} + {number2} = {number1 + number2}")
    
#     elif operation in ['subtract',"s","-"]:

#         print(f"{number1} - {number2} = {number1 - number2}")
    
#     elif operation in ['multiply',"m","*"]:

#         print(f"{number1} * {number2} = {number1 * number2}")
    
#     else:
#         print(f"This {operation} Worng .. try again")

# calculate(10, 20) # 30
# calculate(10, 20, "AdD") # 30
# calculate(10, 20, "a") # 30
# calculate(10, 20, "A") # 30
# calculate(10, 20, "+") # 30

# calculate(10, 20, "S") # -10
# calculate(10, 20, "subTRACT") # -10
# calculate(100, 15, "-") # 85

# calculate(10, 20, "Multiply") # 200
# calculate(10, 20, "m") # 200
# calculate(10, 10, "*") # 100

# calculate(10, 10,"bad") # This bad Worng .. try again
# ? --------------------------------- 2  -------------------------
# def addition(*parameters):

#     add = 0

#     for num in parameters:
#         if num == 10 :
#             continue

#         elif num == 5:
#             add -= num

#         else:
#             add+=num

#     return add
    
# print(addition(10, 20, 30, 10, 15)) # 65
# print(addition(10, 20, 30, 10, 15, 5, 100)) # 160
# ? --------------------------------- 3  -------------------------
# def show_skills(name,*skills):
#     if len(skills) > 0 :

#         print(f"Hello {name} Your Skills Is: ")

#         for skill in skills :

#             print(f"- {skill}")
#     else:
#         print(f"Hello {name} You Have No Skills To Show ")


# show_skills("0ag_ntfsx00", "HTML", "CSS", "JS", "Python")
# show_skills("0ag_ntfsx00", "Python")
# show_skills("0ag_ntfsx00")
# ? --------------------------------- 4  -------------------------
# def say_hello(name="Unknown",age="Unknown",country="Unknown"):

#     return f"Hello {name} Your {age} Is 38 And You Live In {country}"

# print(say_hello("0ag_ntfsx00", 38, "Egypt"))

# print(say_hello())