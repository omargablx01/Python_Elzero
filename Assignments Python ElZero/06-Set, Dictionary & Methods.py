
# t~ >>>>                                                 Assignments  26 ==> 32                                            <<<<<
# ? --------------------------------- 1  -------------------------
# my_list = [1, 2, 3, 3, 4, 5, 1]

# unique_list = list(set(my_list))

# print(unique_list) # {1, 2, 3, 4, 5}

# print(type(unique_list)) # <class 'list'>

# print(unique_list[:-1]) # [1, 2, 3, 4]

# ? --------------------------------- 2  -------------------------
# nums = {1, 2, 3}
# letters = {"A", "B", "C"}

# print(nums.union(letters)) # {1, 2, 3, 'B', 'A', 'C'}
# print(nums | letters) # {1, 2, 3, 'B', 'A', 'C'}
# nums.update(letters)
# print(nums) # {1, 2, 3, 'B', 'A', 'C'}

# ? --------------------------------- 3  -------------------------
# my_set = {1, 2, 3}
# letters = {"A", "B", "C"}

# print(my_set) # {1, 2, 3}
# my_set.clear()
# print(my_set) # set()
# my_set.update(['A','B'])
# my_set.discard("C")
# print(my_set) # {'A', 'B'}

# ? --------------------------------- 4  -------------------------
# set_one = {1, 2, 3}
# set_two = {1, 2, 3, 4, 5, 6}

# print(set_one.issubset(set_two)) # True

# ? --------------------------------- 5  -------------------------
# my_dict = {
#     1 : {"name" : "Python","progress":"90%"},
#     2 : {"name" : "Cyber","progress":"50%"},
#     3 : {"name" : "CSS","progress" : "70%"},
#     4 : {"name" : "AI","progress" : "80%"}
#     }

# my_dict[5] = {"name" : "HTML","progress" : "60%"}
# my_dict.update({6 : {"name" : "PHP","progress" : "30%"}})
# print(f"{my_dict[1]['name']} Progress Is {my_dict[1]['progress']}")
# print(f"{my_dict[2]['name']} Progress Is {my_dict[2]['progress']}")
# print(f"{my_dict[3]['name']} Progress Is {my_dict[3]['progress']}")
# print(f"{my_dict[4]['name']} Progress Is {my_dict[4]['progress']}")
# print(f"{my_dict[5]['name']} Progress Is {my_dict[5]['progress']}")
# print(f"{my_dict[6]['name']} Progress Is {my_dict[6]['progress']}")

# ! OR ----------------------------
# frameworkOne = {"name": "Vuejs","progress": "80%"}
# frameworkTwo = {"name": "ReactJs","progress": "80%"}
# frameworkThree = {"name": "Angular","progress": "80%"}
# allFramework = {"1st": frameworkOne,"2st": frameworkTwo,"3th": frameworkThree}

# allFramework["4th"] = {"name" : "HTML","progress" : "60%"}
# allFramework.update({"5th" : {"name" : "PHP","progress" : "30%"}})

# print(f"{allFramework["1st"]['name']} Progress Is {allFramework["1st"]['progress']}")
# print(f"{allFramework["2st"]['name']} Progress Is {allFramework["2st"]['progress']}")
# print(f"{allFramework["3th"]['name']} Progress Is {allFramework["3th"]['progress']}")
# print(f"{allFramework["4th"]['name']} Progress Is {allFramework["4th"]['progress']}")
# print(f"{allFramework["5th"]['name']} Progress Is {allFramework["5th"]['progress']}")

# ! OR ----------------------------
# diCover = {"prog1": "HTML",
#            "progress1": "90%",
#            "prog2": "CSS",
#            "progress2": "90%",
#            "prog3": "Python",
#            "progress3": "30%"
#            }

# diCover.update({"prog4" : "PHP","progress4" : "30%"})
# print(f"{diCover['prog1']} Progress Is {diCover['progress1']}")
# print(f"{diCover['prog2']} Progress Is {diCover['progress2']}")
# print(f"{diCover['prog3']} Progress Is {diCover['progress3']}")
# print(f"{diCover['prog4']} Progress Is {diCover['progress4']}")