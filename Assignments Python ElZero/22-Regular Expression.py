
# t~ >>>>                                                 Assignments  95 ==> 102                                            <<<<<
# ? --------------------------------- 1  -------------------------
# import re
# string1 = '"eeeeE llllLl lllzzZzzzz eroe operationr pollo "'
# print(re.findall(r"\w ",string1))
# print(re.findall(r"\w\s",string1))
# ? --------------------------------- 2  -------------------------
# string2 = '"EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111"'

# print(re.findall(r"L[A-z]+",string2)) # ['LElzero']
# print(re.findall(r"L\w[a-z](Elzero)*",string2)) # ['LElzero']
# print(re.findall(r"[G-L](Elzero)",string2)) # ['Elzero']

# ? --------------------------------- 3  -------------------------
# string3 = """
# +(0100) 600-1234
# +(0100) 60-1234
# (0100) 6000-1234
# 01006001234
# 0100 600 1234
# (0100) 600-1
# (0100) 600-12"""

# print(re.findall(r"\+?\(\d+\) \d+-\d{4}",string3,re.MULTILINE))
# print(re.findall(r"(\+?\(\d{4}\) \d+-\d{4})",string3,re.MULTILINE))
# ? --------------------------------- 4  -------------------------
# string4 = """
# http://www.elzero.org:8888/link.php
# https://elzero.org:8888/link.php
# http://www.elzero.com/link.py
# https://elzero.com/link.py
# http://www.elzero.net
# https://elzero.net"""
# print(re.findall(r"^(https?://)(www\.)?(\w+\.)(\w+)(\:\d+)?/(.+)$",string4,re.MULTILINE))
# print(re.findall(r"((https?://)(www\.)?(\w+)(.com|.org)(:\d+)?(.+))",string4,re.MULTILINE))
# ? --------------------------------- 5  -------------------------
# string5 = """
# http
# https
# abcd
# abcd"""

# print(re.findall(r"https?",string5)) # ['http', 'https']
# print(re.findall(r"(https|http)",string5)) # ['http', 'https']
# print(re.findall(r"HTTPS?",string5,re.IGNORECASE)) # ['http', 'https']
# print(re.findall(r"[h-z]{4,5}",string5)) # ['http', 'https']
# print(re.findall(r"[h-t]+",string5)) # ['http', 'https']
# print(re.findall(r"(http\w?)",string5)) # ['http', 'https']
# print(re.findall(r"h(.)+",string5))
