
# t~ >>>>                                                 Assignments  21 ==> 23                                             <<<<<
# ? --------------------------------- 1  -------------------------
# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
# print(friends[0]) # "Osama"
# print(friends[-5]) # "Osama"
# print(friends[len(friends)-5]) # "Osama"
# print(friends.pop(0))# "Osama"
# print(friends[friends.index("Osama")])

# print(friends[len(friends)-1]) # "Mahmoud"
# print(friends[4]) # "Mahmoud"
# print(friends[-1]) # "Mahmoud"
# print(friends.pop(-1))# "Mahmoud"
# print(friends[friends.index("Mahmoud")])
# ? --------------------------------- 2  -------------------------
# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# print(friends[::2]) # "Osama", "Sayed", "Mahmoud"
# print(friends[1::2]) # "Ahmed", "Ali"
# print(friends[1:4:2])# "Ahmed", "Ali"

# ? --------------------------------- 3  -------------------------
# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# print(friends[1:4]) # 'Ahmed', 'Sayed', 'Ali'
# print(friends[-4:4])  # "Ahmed", "Sayed", "Ali"
# print(friends[friends.index("Ahmed"):friends.index("Mahmoud")]) # "Ahmed", "Sayed", "Ali"

# print(friends[-2:]) # "Ali", "Mahmoud"
# print(friends[3:])# "Ali", "Mahmoud"
# print(friends[friends.index("Ali"):]) # "Ali", "Mahmoud"

# ? --------------------------------- 4  -------------------------
# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
# friends[friends.index("Ali")] = "Elzero"
# friends[-2] = "Elzero" # OR  friends[3]="Elzero"

# friends[friends.index("Mahmoud")] = "Elzero"
# friends[-1] = "Elzero" # OR  friends[4]="Elzero"

# print(friends) # ['Osama', 'Ahmed', 'Sayed', 'Elzero', 'Elzero']

# ? --------------------------------- 5   -------------------------
# friends = ["Osama", "Ahmed", "Sayed"]
# friends.insert(0,"Nasser") # ["Nasser", "Osama", "Ahmed", "Sayed"]
# print(friends)
# friends.append("Salem") # ['Nasser', 'Osama', 'Ahmed', 'Sayed', 'Salem']
# print(friends)

# ? --------------------------------- 6  -------------------------
# friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
# friends.remove("Nasser")
# friends.remove("Osama")
# print(friends) # ["Ahmed", "Sayed", "Salem"]

# friends.pop(-1) # ! OR  friends.pop() OR friends.remove("Salem")
# print(friends) # ["Ahmed", "Sayed"]

# ? --------------------------------- 7  -------------------------
# friends = ["Ahmed", "Sayed"]
# employees = ["Samah", "Eman"]
# school = ["Ramy", "Shady"]
# friends.extend(employees)
# friends.extend(school)
# print(friends) # ['Ahmed', 'Sayed', 'Samah', 'Eman', 'Ramy', 'Shady']

# ? --------------------------------- 8  -------------------------
# friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
# friends.sort()
# print(friends) # ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']

# friends.sort(reverse=True) # OR friends.reverse()
# print(friends) # ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']

# ? --------------------------------- 9  -------------------------
# friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

# print(len(friends)) # 6

# ? --------------------------------- 10  -------------------------
# technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

# index_Django = technologies[-1].index("Django")
# print(technologies[-1][index_Django]) # Django
# print(technologies[-1][0]) # Django

# index_Web = technologies[-1].index("Web")
# print(technologies[-1][index_Web]) # Web
# print(technologies[-1][-1]) # Web
# print(technologies[-1][2])  # Web
