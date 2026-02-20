
# todo >>>>                                                 Assignments  47 ==> 50                                            <<<<<
# ? --------------------------------- 1  -------------------------
# num = int(input("Write Number : ").strip())
# ll = []

# if num > 0 :

#     while num :

#         num -=1

#         if num == 0 :

#             break

#         elif num == 6:

#             continue

#         else :

#             ll.append(num)

#             print(num)  

#     print(f"{len(ll)} Numbers Printed Successfully.")
    
# else :

#     print("Number 0 Is Not Larger Than 0")
# ? --------------------------------- 2  -------------------------
# friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]

# my_lower = []

# lens = len(friends)

# while lens > 0 :

#     lens -=1

#     if friends[lens].islower():

#         my_lower.append(friends[lens])

#         continue

#     else:

#         print(friends[lens])

# else:

#     print(f"Friends Printed And Ignored Names Count Is {len(my_lower)}")

#     my_lower.sort()

#     print(my_lower)

# ? --------------------------------- 3  -------------------------
# skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

# while skills:
#     print(skills.pop(0))
# ? --------------------------------- 4  -------------------------
# my_friends = []
# tries = 4

# while tries > 0 :
#     print("-"*40)

#     uname = input("Wrtie Your Name : ").strip()

#     print("-"*40)

#     if uname.isupper():
#         print("Invalid Name")

#         print("#"*40)

#         print(f"Names Left in List Is {tries}")

#         continue

#     elif uname.islower() :
#         tries -=1

#         my_friends.append(uname.capitalize())

#         print(f"Friend {uname} Added => 1st Letter Become Capital")

#         print("#"*40)

#         print(f"Names Left in List Is {tries}")

#     elif uname.istitle() :
#         tries -=1

#         my_friends.append(uname)

#         print(f"Friend {uname} Added")

#         print("#"*40)

#         print(f"Names Left in List Is {tries}" if tries > 0 else "All Your Friend Added")
#     else:
#         print("Invalid Name Plase Type You Name First Letter Is Capital")
# else:
#     print(f"Your List Is > {my_friends}")