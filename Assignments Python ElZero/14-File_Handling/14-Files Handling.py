
# todo >>>>                                                 Assignments  65 ==> 68                                            <<<<<
# ? --------------------------------- 1  -------------------------

# import os
# print(os.getcwd())
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# files_name = fr"E:\HACKING\Python\Assignments Python ElZero\test\assigmnt.py"
# # files_name = files_name[-9:]

# print(files_name[-9:])

# file_num =1

# num = range(1, 51)

# for alls in num:

#     if alls == 25:

#         my_files = open(fr"E:\HACKING\Python\Assignments Python ElZero\test\special-text.txt","w")

#         my_files.close()

#     else:
#      my_files2 =open(fr"E:\HACKING\Python\Assignments Python ElZero\test\txt{alls}.txt","w")

#      my_files2.write(f"ElZero Web School => {alls}\n")

#      my_files2.close()

#     file_num +=1

# print(file_num)
# ! -------------------- Prof

# for mk_file in range(1,51) :

#     if mk_file == 25 :

#         my_file = open(rf"E:\HACKING\Python\Assignments Python ElZero\14-File_Handling\special-text.txt","w")

#         my_file.close()

#         continue

#     my_file = open(rf"E:\HACKING\Python\Assignments Python ElZero\14-File_Handling\txt{str(mk_file).zfill(2)}.txt","w")

#     my_file.write(f"NTFS => {mk_file}")
# # 
#     my_file.close()

# import os

# print(os.getcwd()) # E:\HACKING\Python

# print(os.path.dirname(os.path.abspath(__file__))) # e:\HACKING\Python\Assignments Python ElZero\File_Handling

# print(os.path.basename(__file__)) # 14-Files Handling.py

# print(len(os.listdir(os.path.dirname(os.path.abspath(__file__))))) # 52

# ? --------------------------------- 2  -------------------------
# my_file = open(rf"E:\HACKING\Python\Assignments Python ElZero\14-File_Handling\txt01.txt","a")

# for write_data in range(1,51):

#     my_data = f"\nAppended => Elzero Web School"

#     my_file.write(my_data)
# ! ----------------------------- Easy Way
# my_file.write("\nAppended => Elzero Web School"*50)

# my_file.close()
# ? --------------------------------- 3  -------------------------
# my_file = open(rf"E:\HACKING\Python\Assignments Python ElZero\14-File_Handling\txt01.txt","r")

# my_list = my_file.readlines()
# print(f"Number Of Lines Is => {len(my_list)}") # 51

# len_chars = len(my_file.read()) # 1522
# print(len_chars)
# ! ---------------------- prof
# my_list = my_file.readlines()
# lines_num = len(my_list)
# words_num = 0
# chars_num = 0
# char_l_num = 0

# for x in my_list:

#     o = x.split()

#     words_num += len(x)
#     print(x)

#     for i in x:

#         y = i.strip()

#         chars_num += len(y)

#         char_l_num += i.count("l")

# print(f"Number Of Lines Is => {lines_num}")
# print(f"Number Of Words Is => {words_num}")
# print(f"Number Of Chars Is => {chars_num}")
# print(f"Number Of \"l\" Char Is => {char_l_num}")

# my_file.close()
# ? --------------------------------- 4  -------------------------
# import os
# my_dirc = os.path.dirname(os.path.abspath(__file__))
# # print(os.listdir(os.path.dirname(os.path.abspath(__file__)))) # ! list my files

# for my_num in range(41,51):

#     for my_remove_file in os.listdir(os.path.dirname(os.path.abspath(__file__))):

#         first = my_remove_file[:3]

#         if my_remove_file.startswith(f"{first}{my_num}"):

#             os.remove(rf"{my_dirc}\{first}{my_num}.txt")
# ! ------------------- Easy Way
# import os
# print(os.path.dirname(os.path.abspath(__file__)))
# for i in range(41,51):
    # os.remove(fr"{os.path.dirname(os.path.abspath(__file__))}\txt{i}.txt")
