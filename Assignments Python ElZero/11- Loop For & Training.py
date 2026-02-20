
# todo >>>>                                                 Assignments  51 ==> 55                                            <<<<<
# ? --------------------------------- 1  -------------------------
# my_nums = [15, 81, 5, 17, 20, 21, 13]

# lens = []

# my_nums.sort(reverse=True)

# for my_values in my_nums:

#     if my_values % 5 == 0 :

#         lens.append(my_values)

#         my_len = len(lens)

#         print(f"{my_len} - {my_values}")

# else:
#     print("All Numbers Printed")
# ! ------------------------ طريقه اخرى 
# my_numbers = [15, 81, 5, 17, 20, 21, 13]
# my_numbers.sort(reverse=True)
# a = 1

# for num in my_numbers:
#     if num % 5 == 0:
#         print(f"{a} => {num}")
#         a += 1
#     else:
#         pass

# print("All Numbers are Printed")
# ! ------------------------ طريقه اخرى 
# my_nums = [15, 81, 5, 17, 20, 21, 13]

# lens = []

# my_nums.sort(reverse=True)

# for my_values in my_nums:

#     if my_values % 5 == 0 :

#         lens.append(my_values)

#         my_len = len(lens)

#         print(f"{my_len} - {lens[my_len-1]}")

# else:
#     print("All Numbers Printed")

# ? --------------------------------- 2  -------------------------
# ! Prof Way ..
# for loops in range (1,21):
        
#         if loops in [12,8,6]:
#              continue
#         print(f"{str(loops).zfill(2)}")
# else:
#     print("All Numbers Printed")
 
# ! ------------------------ طريقه اخرى 
# for loops in range (1,21):
#     if loops in [12,8,6]:
#         continue
#     if loops < 10 :
#         print(f"{str(loops).zfill(2)}")
#     else:
#         print(f"{loops}")
# else:
#     print("All Numbers Printed")
# ? --------------------------------- 3  -------------------------
# my_ranks = {
#   'Math': 'A',
#   "Science": 'B',
#   'Drawing': 'A',
#   'Sports': 'C'
# }
# my_rank = {
#     "A":100,
#     "B":80,
#     "C":40
# }
# sums_values = []
# for my_keys,my_values in my_ranks.items():

#     for keys,val in my_rank.items():

#         if keys == my_values:

#             print(f"My Rank in {my_keys} => {keys} And This Equal {val} Points")

#             sums_values.append(val)

#             break
# ! طريقة الحصول علي الجمع من خلال While 
# index = 0
# sums = 0

# while index < len(sums_values):

#     sums+=sums_values[index]

#     index+=1

# print(f"Total Points Is {sums}")

# ! طريقة الحصول علي الجمع من خلال for
# sums_number = 0

# for num in sums_values:

#     sums_number +=num

# print(f"Total Points Is {sums_number}")
# ! --- Other Wayy ---
# my_ranks = {
#     'Math': 'A',
#     'Science': 'B',
#     'Drawing': 'A',
#     'Sports': 'C'
# }

# my_points = {
#     "A": 100,
#     "B": 80,
#     "C": 40
# }

# sums = 0

# for subject in my_ranks:

#     for points in my_points:

#         if my_ranks[subject] == points:

#             sums += my_points[points]

#             print(f"My Rank in {subject} Is '{my_ranks[subject]}' And This Equal {my_points[points]} Points.")

# print(f"Total Points Is: {sums}")
# ? --------------------------------- 4  -------------------------
# students = {
#   "Ahmed": {
#     "Math": "A",
#     "Science": "D",
#     "Draw": "B",
#     "Sports": "C",
#     "Thinking": "A"
#   },
#   "Sayed": {
#     "Math": "B",
#     "Science": "B",
#     "Draw": "B",
#     "Sports": "D",
#     "Thinking": "A"
#   },
#   "Mahmoud": {
#     "Math": "D",
#     "Science": "A",
#     "Draw": "A",
#     "Sports": "B",
#     "Thinking": "B"
#   }
# }

# grade_rank = {
#     "A":100,
#     "B":80,
#     "C":40,
#     "D":20
# }
# sums_rank_ahmed = []
# sums_rank_sayed = []
# sums_rank_mahmoud= []
# sums_numbers3 = 0
# for key_name,values_all in students.items():
#     print("-"*30)
#     print(f"-- Student Name => {key_name}")
#     print("-"*30)

#     for key_skills,vlaues_grade in values_all.items():

#         for key_rank,value_rank in grade_rank.items():

#             if vlaues_grade == key_rank and key_name == "Ahmed":
#                 print(f"- {key_skills} => {value_rank} Points")
    
#                 sums_rank_ahmed.append(value_rank)

#                 sums_numbers1 = 0

#                 for num in sums_rank_ahmed:

#                     sums_numbers1 +=num

#                     if sums_numbers1 == 340 :

#                         print(f"Total Points For {key_name} => {sums_numbers1}")

#             elif vlaues_grade == key_rank and key_name == "Sayed":
#                 print(f"- {key_skills} => {value_rank} Points")

#                 sums_rank_sayed.append(value_rank)

#                 sums_numbers2 = 0

#                 for num in sums_rank_sayed:

#                     sums_numbers2 +=num

#                     if sums_numbers2 == 360 :

#                         print(f"Total Points For {key_name} => {sums_numbers2}")

#             elif vlaues_grade == key_rank and key_name == "Mahmoud":

#                 print(f"- {key_skills} => {value_rank} Points")

#                 sums_rank_mahmoud.append(value_rank)

#                 sums_numbers3 = 0

#                 for num in sums_rank_mahmoud:

#                     sums_numbers3 +=num

#                     if sums_numbers3 == 380 :

#                         print(f"Total Points For {key_name} => {sums_numbers3}")
# ?----
# ! --- Some Way for Solving ---
# students = {
#     "Ahmed": {
#         "Math": "A",
#         "Science": "D",
#         "Draw": "B",
#         "Sports": "C",
#         "Thinking": "A"
#     },
#     "Sayed": {
#         "Math": "B",
#         "Science": "B",
#         "Draw": "B",
#         "Sports": "D",
#         "Thinking": "A"
#     },
#     "Mahmoud": {
#         "Math": "D",
#         "Science": "A",
#         "Draw": "A",
#         "Sports": "B",
#         "Thinking": "B"
#     }
# }

# my_points = {
#     "A": 100,
#     "B": 80,
#     "C": 40,
#     "D" : 20
# }

# sum1 = 0
# sum2 = 0
# sum3 = 0

# for student in students:
#     print("-" * 30)
#     print(f"Student Name => {student}")
#     print("-" * 30)

#     for subjects in students[student]:

#         for points in my_points:

#             if students[student][subjects] == points and student == "Ahmed":
#                 sum1 += my_points[points]
#                 print(f"- {subjects} => {my_points[points]} Points")
                
#             elif students[student][subjects] == points and student == "Sayed":
#                 sum2 += my_points[points]
#                 print(f"- {subjects} => {my_points[points]} Points")

#             elif students[student][subjects] == points and student == "Mahmoud":
#                 sum3 += my_points[points]

#                 print(f"- {subjects} => {my_points[points]} Points")

#     print(f"= Total Points For {student} Is: {sum1 if student == 'Ahmed' else sum2 if student == 'Sayed' else sum3}")

# ! --- With items() ---

# for key_name,value_skill in students.items():
#     print("-" * 30)
#     print(f"Student Name => {key_name}")
#     print("-" * 30)

#     for skill_name,grade in value_skill.items():
#         for key_abcd ,points in my_points.items():

#             if grade == key_abcd and key_name == "Ahmed":
#                 sum1 += points
#                 print(f"- {skill_name} => {points} Points")
                
#             elif grade == key_abcd and key_name == "Sayed":
#                 sum2 += points
#                 print(f"- {skill_name} => {points} Points")

#             elif grade == key_abcd and key_name == "Mahmoud":
#                 sum3 += points
#                 print(f"- {skill_name} => {points} Points")

#     print(f"= Total Points For {key_name} Is: {sum1 if key_name == 'Ahmed' else sum2 if key_name == 'Sayed' else sum3}")