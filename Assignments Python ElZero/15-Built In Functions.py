
# t~ >>>>                                                 Assignments  69 ==> 71                                            <<<<<
# ? --------------------------------- 1  -------------------------
# values = (0, 1, 2)

# if any(values): #True
    
#     my_var = 0

# my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

# if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

#     print("Good") #! Good Because all(my_list[:4]) == True

# else:

#   print("Bad")

# ? --------------------------------- 2  -------------------------
# v = 40

# my_range = list(range(v))

# print(sum(my_range,40)) # start Sum From 40

# print(sum(my_range, v) + pow(v, v, v))  # 820

# ? --------------------------------- 3  -------------------------
# n = 21

# l = list(range(n))

# print(round(sum(l) / n)) # 10

# if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

#   print("Good") # @@ Output => Good

# ? --------------------------------- 4  -------------------------
# ! اختبار مخترع من دماغي
# def my_sum(numbers):

#     my_sum = 0
    
#     for number in numbers:

#         my_sum+=number

#     return my_sum

# print(my_sum((1, 2, 3,9,155))) # 170
# ! ------------------------ 1 
# def my_all (items):

#     for item in items:

#         if bool(item) == False:

#             return False

#     else:

#         return True
    
# print(my_all([1, 2, 3])) # True
# print(my_all([1, 2, 3, []])) # False
# @@ ----- Another Way
# def my_all(done):
    
#     d = 0

#     for r in done:

#         if bool(r):

#             d += 1

#     if d == len(done):

#         return True
    
#     else:

#         return False

# print(my_all([1, 2, 3]))  # True
# print(my_all([1, 2, 3, []]))  # False
# ! ------------------------ 2
# def my_any (items):

#     for item in items:

#         if bool(item) == True:

#             return True

#     else:

#         return False
# @@ ----- Another Way
# def my_any(items):

#     for item in items:

#         if item:

#             return True

#     return False
    
# print(my_any([0, 1, [], False])) # True
# print(my_any([(), 0, False])) # False
# @@ ----- Another Way
# def my_any(done):

#     d = 0

#     for r in done:

#         if bool(r):

#             d += 1

#     if d >= 1:

#         return True

#     else:

#         return False


# print(my_any([0, 1, [], False]))  # True
# print(my_any([(), 0, False]))  # False
# ! ------------------------ 3 min
# def my_min(items):

#     free_list = []

#     for item in items:

#         free_list.append(item)

#         free_list.sort()

#     return free_list.pop(0)

# print(my_min([10, 100, -20, -100, 50])) # -100
# print(my_min((10, 100, -20, -100, 50))) # -100
# @@ ----- Another Way
# def my_min(items):

#     my_list = list(items)

#     my_list.sort()

#     return my_list [0]

# print(my_min([10, 100, -20, -100, 50])) # -100
# print(my_min((10, 100, -20, -100, 50))) # -100
# @@ ----- Another Way
# def my_min(allos):

#     k = allos[0]

#     for i in allos:

#         if i < k:

#             k = i

#     return k

# print(my_min([10, 100, -20, -100, 50]))  # -100
# print(my_min((10, 100, -20, -100, 50)))  # -100
# ! ------------------------ 4 max
# def my_max(items):

#     free_list = []

#     for item in items:

#         free_list.append(item)

#         free_list.sort()

#     return free_list.pop(-1)

# print(my_max([10, 100, -20, -100, 50, 700])) # 700
# print(my_max((10, 100, -20, -100, 50, 700))) # 700
# @@ ----- Another Way
# def my_max(items):

#     my_list = list(items)

#     my_list.sort()

#     return my_list [-1]

# print(my_max([10, 100, -20, -100, 50, 700])) # 700
# print(my_max((10, 100, -20, -100, 50, 700))) # 700
# @@ ----- Another Way
# def my_max(allos):

#     k = allos[0]
    
#     for i in allos:
        
#         if i > k:
            
#             k = i
            
#     return k
    

# print(my_max([10, 100, -20, -100, 50, 700]))  # 700
# print(my_max((10, 100, -20, -100, 50, 700)))  # 700