
# t~ >>>>                                                 Assignments  60 ==> 64                                            <<<<<
# ? --------------------------------- 1  -------------------------
# def get_score(**all):

#     for score_key,score_value in all.items():

#         print(f"{score_key} => {score_value}")

# get_score(Math=90, Science=80, Language=70)
# print("-" * 45)
# get_score(Logic=70, Problems=60)
# ? --------------------------------- 2  -------------------------
# def get_people_scores(*names,**skills):

#     for name in names :

#         if len(skills) >= 1 : 

#             print(f"Hello {name} This Is Your Score Table:")

#         else:

#             print(f"Hello {name} You Have No Scores To Show")

#     for skill_key,skill_value in skills.items():

#         print(f"{skill_key} => {skill_value}")

# get_people_scores("Osama", Math=90, Science=80, Language=70)
# get_people_scores("Mahmoud", Logic=70, Problems=60)
# get_people_scores(Logic=70, Problems=60)
# get_people_scores("Ahmed")
# ! ------------------------- Prof
#  def get_people_scores(*name, **scores):
#     for names in name:

#         if len(names) > 0 and len(scores) > 0:

#             print(f"Hello {names} This Is Your Score Table : ")

#         if len(scores) == 0:

#             print(f"Hello {names} You Have No Scores To Show")

#     for get_key, get_value in scores.items():

#         print(f"{ get_key} => {get_value}")

# get_people_scores("Osama", Math=90, Science=80, Language=70)
# get_people_scores("Mahmoud", Logic=70, Problems=60)
# get_people_scores(Logic=70, Problems=60)
# get_people_scores("Ahmed")
# ! ------------------------- Prof
# def get_pepole_scores2(namee="", **scoress):

#     if len(scoress) > 0:

#         if bool(namee):

#             print(f"Hello {namee} This is Your Score Table: ")

#         for key, value in scoress.items():

#             print(f"- {key} => {value}")
#     else:

#         print(f"Hello {namee} You Have No Scores To Show")

# get_pepole_scores2("Osama", Math=90, Science=80, Language=70)
# get_pepole_scores2("Mahmoud", Logic=70, Problems=60)
# get_pepole_scores2(Logic=70, Problems=60)
# get_pepole_scores2("Ahmed")
# ? --------------------------------- 3  -------------------------
# student_score = {
#     "Math" : 90,
#     "Science" : 80,
#     "Language" : 70
# }
# def get_the_scores(name = "", **scores_list):

#     if name == "" :
#         pass

#     elif name != "" and scores_list != {}:
#         print(f"Hello {name}, This Is Your Score Table:")

#     if scores_list == {} and name != "":
#         print(f"Hello {name} You Have No Scores To Show.")

#     else:
#         for subject_key,subject_value in scores_list.items():
#             print(f"- {subject_key} => {subject_value}")


# get_the_scores("NTFSx00", **student_score)

# print('=' * 40)

# get_the_scores("NTFSx00")

# print('=' * 40)

# get_the_scores(**student_score)

# ! ------------------------- Prof
# scores_list = {
#     "Math": 90,
#     "Science": 80,
#     "Language": 70,
# }
# def get_the_scores(name="", **scoress):

#     if len(scoress) > 0:

#         if bool(name):

#             print(f"Hello {name} This is Your Score Table: ")

#         for key, value in scoress.items():

#             print(f"- {key} => {value}")
#     else:
#         print(f"Hello {name} You Have No Scores To Show")

# get_the_scores("NTFSx00", **scores_list)

# print('=' * 40)

# get_the_scores("NTFSx00")

# print('=' * 40)

# get_the_scores(**scores_list)