
# t~ >>>>                                                 Assignments  128 ==> 132                                            <<<<<
# ? --------------------------------- 1  -------------------------
# import unittest

# class MytestCase(unittest.TestCase):
#     def test_case_one(self):
#         self.assertIn(10,[5, 7, 8, 10],"10 Is Found In This List [5, 7, 8, 10]")

#     def test_case_two(self):
#         self.assertIsInstance(10,int,"The Type Of 10 Is Int")

#     def test_case_three(self):
#         self.assertTrue(100,"Number 100 Return True")

#     def test_case_four(self):
#         self.assertTrue([],"Empty List [] Return False")

#     def test_case_five(self):
#         self.assertGreaterEqual(100 , 90 ,"100 Is Larger Than Or Equal 90")

# if __name__ == "__main__":
#     unittest.main()
# ? --------------------------------- 2  -------------------------
# from string import * 
# import random

# def random_serial(count=14):
#     all_data = ascii_lowercase + digits
#     lens = len(all_data)
#     my_list = []

#     while count > 0 :
#             my_rand = random.randint(0,lens-1)
#             my_new_data = all_data[my_rand]
#             my_list.append(my_new_data)
#             count -=1

#     print(f"{"".join(my_list[:4]):.4}-{"".join(my_list[4:9]):.4}-{"".join(my_list[8:]):.6}")

# random_serial()
# ! --------------- Other Way 
# import string
# import random

# s1 = list(string.ascii_lowercase)
# s2 = list(string.digits)

# # shuffle lists
# random.shuffle(s1)
# random.shuffle(s2)

# result = []

# for x in range(7):
#     result.append(s1[x])
#     result.append(s2[x])

# random.shuffle(result)

# result.insert(4, "-")
# result.insert(9, "-")

# output = "".join(result)

# print(output)

# !  >>>>>>>>>>>>>>>>>>>>>>>>            END In 2/2/2026          <<<<<<<<<<<<<<<<<<<<<<<<