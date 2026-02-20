
# t~ >>>>                                                 Assignments  81 ==> 85                                            <<<<<
# ? --------------------------------- 1  -------------------------
# my_string = "NTFSx00"

# def reverse_string(my_string):

#     for after_reversed in reversed(my_string):

#         yield after_reversed

# for my_reverse in reverse_string(my_string):

#         print(my_reverse)

# my_Gen = reverse_string("NTFSx00") # @@ test my function

# print(list(my_Gen))
# ! -------------- Some Way
# my_string = "NTFSx00"

# def reverse_string(my_string):

#     for x in my_string[-1::-1]:

#         yield x

# for c in reverse_string(my_string):

#     print(c)

# my_Gen = reverse_string(my_string) # @@ test my function

# print(list(my_Gen))
# ? --------------------------------- 2  -------------------------
# def my_sugar(func):
    
#     def nestedfunc():
       
#        print("Sugar Added From Decorators")

#        func()

#        print("#" * 20)
    
#     return nestedfunc

# @my_sugar
# def make_tea():

#   print("Tea Created")

# @my_sugar
# def make_coffe():

#   print("Coffe Created")

# make_tea()
# make_coffe()
