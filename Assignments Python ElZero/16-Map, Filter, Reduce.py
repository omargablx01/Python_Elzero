
# t~ >>>>                                                 Assignments  72 ==> 75                                            <<<<<
# ? --------------------------------- 1  -------------------------
# def remove_chars(names):

#     return names[1:-1]

# friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

# cleaned_list  = map(remove_chars,friends_map)

# for name in cleaned_list:
#     print(name)

#! ----- lambda

# friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

# for name in map(lambda names : names[1:-1] ,friends_map ):

#     print(name)

# ? --------------------------------- 2  -------------------------
# def get_names(name):

#     return name.endswith("m")

# friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

# names = filter(get_names,friends_filter)

# for res in names:

#     print(res)

#! ----- lambda
# friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

# for res in filter(lambda name : name.endswith("m") ,friends_filter):

#     print(res)
# ? --------------------------------- 3  -------------------------
# from functools import reduce

# def my_reduce(num1,num2):

#     return num1 * num2

# nums = [2, 4, 6, 2]

# my_sum = reduce(my_reduce,nums)

# print(my_sum)

#! ----- lambda

# nums = [2, 4, 6, 2]

# my_sum = reduce((lambda num1 , num2 : num1 * num2),nums)

# print(my_sum)
# ? --------------------------------- 4  -------------------------
# skills = reversed(("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript"))

# for counts , values in enumerate(skills,50):

#     if type(values) == int:

#         continue
    
#     print(f"{counts} - {values}")
# ? ------------ Another Way
# skills = reversed(("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript"))

# skills = list(enumerate(skills, 50))

# def cleaner(name):

#     if type(name[1])==int:

#      pass

#     else:

#         return name

# cleaned = filter(cleaner,skills)

# for i,s in cleaned:

#     print(f"{i} - {s}")

# cleaner(skills)