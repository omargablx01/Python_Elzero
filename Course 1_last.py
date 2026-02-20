

# ? -------------------------------------- 005 + 006 ------------------------------------------------------
# str1 = "str"
# int1 = 123
# float1 = 12.8
# bool1 = True
# set1 = {1}
# list1 = [1, 2]
# tuple1 = (1, 1)
# dict1 = {"ONE": 1, "TWO": 2, "three": 3}
# print(type(str1)) # <class 'str'>
# print(type(int1)) # <class 'int'>
# print(type(float1)) # <class 'float'>
# print(type(bool1)) # <class 'bool'>
# print(type(set1)) # <class 'set'>
# print(type(list1))  # <class 'list'>
# print(type(tuple1))  # <class 'tuple'>
# print(type(dict1)) # <class 'dict'>
# --------------------------------------------------------
# a,b,c = 10,15,20 # Make 3 Var in one Line
# print(f"Value For a IS : {a}")
# print(f"Value For b IS : {b}")
# print(f"Value For c IS : {c}")
# ? -------------------------------------- 009 ------------------------------------------------------
# print("Remove\b last Latter")
# print("This\
#  in One\
#  Line")
# print("New\nLine")
# print("Test Back Slash \\")
# print('Escape Single Quotes \'Single\'')
# print('Escape Double Quotes \"Double\"')
# print("Can We Make\rPyt")
# print("Make\ttab")
# print("\x45\x4C \x44\x45\x45\x50")
# ? -------------------------------------- 010 ------------------------------------------------------
# msg = "I Love"
# lang = "Python"
# print(msg + " " + lang)
# print(msg + " - " + lang)

# full = msg + " " + lang
# print(full)

# a = "First \
# Second \
# Third"

# b = "A \
# B \
# C"
# print(a + "\n" + b)
# --------------------------------------------------------
# Name = "ELDEEP"
# Age = 22
# Country = "ELMARG"
# outt = "Hello, My Name Is Osama And Iam 38 Years Old and I Live in Egypt."
# print(Name)
# print(outt)
# print(Age)
# print(Country)

# print(type(Name))
# print(type(Country))
# print(type(outt))
# ? -------------------------------------- 011 ------------------------------------------------------
# myStringOne = 'This is Single Quote'
# myStringTwo = "This is Double Quotes"
# print(myStringOne)
# print(myStringTwo)

# myStringThree = 'This is Single Quote "Test"'
# myStringFour = "This is Double Quotes 'Test'"
# print(myStringThree)
# print(myStringFour)

# myStringFive = '''First
# Second 'Test' "Test"
# Third'''  # لكتابه اكتر من سطر نستخدم 3 سنجل كوت في الاول والاخر
# print(myStringFive)

# myStringSix = """First
# Second "Test" \\\ 'Test'
# Third"""  # لكتابه اكتر من سطر نستخدم 3 دابل كوت في الاول والاخر
# print(myStringFive)
# print(myStringSix)
# ? -------------------------------------- 012 ------------------------------------------------------
# myString = "I Love Python"

# print(myString[0])  # Index 0 => (I)
# print(myString[9])  # Index 9 => (t)

# print(myString[-1])  # Index -1 => First Character From End (n)
# print(myString[-6])  # Index -6 => 6th Character From End (p)
# ---------------------------------
# Slicing ( Access Multiple Sequence Items )
# [Start:End] End Not Included
# t~ Name_Slicing[Start:End:Steps]

# print(myString[8:11])  # yth
# print(myString[3:5])  # ov

# print(myString[:10])  # If Start Is Not Here Will Start From 0 (I Love Pyt)
# print(myString[5:])  # If End Is Not Here Will Go To The End (e Python)

# print(myString[:])  # Full Data
# print(myString)  # Full Data

# print(myString[0::1])  # Full Data
# print(myString[::1])  # Full Data

# print(myString[::2]) # بيفوت واحد ويطبع واحد (ILv yhn)
# print(myString[::3]) # (Io tn) بيفوت 2 ويطبع ال3
# ? -------------------------------------- 013 ------------------------------------------------------
# ---------------------
# -- Strings Methods --
# ---------------------
#! len(a) تستخدم لمعرفه عدد العناصر الموجود عدد الحروف او الارقام
#! strip() تستخدم لازاله المسافات من كل الجوانب
#! rstrip() تستخدم لازاله المسافات من اللمين
#! lstrip() تستخدم لازاله المسافات من الشمال

# a = "     I Love Python Py   "
# print(len(a))
# print(a.strip())
# print(a.rstrip())
# print(a.lstrip())

# a = "###I Love Python##"  # ? اذا تم اعطاءه كلمه او حرف او اي شي وهو موجود سوف يتم حذفه ولكن لازم نبداء من اليمين او الشمال 
# print(a.strip("#")) # (I Love Python)
# print(a.rstrip("#")) # (###I Love Python)
# print(a.lstrip("#")) # (I Love Python##)

# a = "@#@#@#I Love Python@#@#@#"
# print(a.strip("@#")) # (I Love Python)
# print(a.rstrip("@#")) # (@#@#@#I Love Python)
# print(a.lstrip("@#")) # (I Love Python@#@#@#)

# a = "%$%$PYTHON !!!:`!@#$%^&*:;;;"

# print(a) # (%$%$PYTHON !!!:`!@#$%^&*:;;;)
# print(a.strip("`!@#$%^&*;:")) # (PYTHON)

# title() # ? يجعل اول حرف ف كل كلمه كابتل واي حرف قبله رقم يحوله كابتل ايضا

# b = "I Love 2d Graphics and 3g Technology and python"
# print(b.title()) # (I Love 2D Graphics And 3G Technology And Python)

# ? خاصية capitalize() تقوم بتحويل أول حرف Capital من ال String واذا كان ال String يحتوي على جملة فيها الكثير من الكلمات فانه يقوم بتحويل اول حرف Capital من أول كلمة فقط وباقي الكلمات كل حروفها تكون Small Letter

# b = "I Love d Graphics and 3g Technology and Python"
# print(b.capitalize()) # (I love d graphics and 3g technology and python)

#! lower() يحول كل النص الي صغير 
# print(b.lower()) # (i love d graphics and 3g technology and python)

#! upper() يحول كل النص الي كبير 

# print(b.upper()) # (I LOVE D GRAPHICS AND 3G TECHNOLOGY AND PYTHON)

# c, d, e, f = "1", "11", "111", "1111"

# print(c) # (1)
# print(d) # (11)
# print(e) # (111)
# print(f) # (1111)

# ! يضيف عدد اصفار معينه علي حسب كام انت وضعت بداخل الاقواس وهذا يكون الافضل

# print(c.zfill(4)) # (0001)
# print(d.zfill(4)) # (0011)
# print(e.zfill(4)) # (0111)
# print(f.zfill(4)) # (1111)

# cap = "jOny FONU 2Hony 4ony---"
# zfill_string= "12"
# strips = "@#@#@#I Love Python@#@#@#"

# print(len(cap)) # (23)
# cap2=cap.strip("-")
# print(len(cap2)) # (20)

# print(cap.strip("-")) # (jOny FONU 2Hony 4ony)
# print(strips.lstrip("@#")) # (I Love Python@#@#@#)
# print(strips.rstrip("@#")) # (@#@#@#I Love Python)

# print(cap2.title()) #(Jony Fonu 2Hony 4Ony)
# print(cap2.capitalize()) # (Jony fonu 2hony 4ony)
# print(zfill_string.zfill(4)) # (0012)
# print(cap2.upper()) # (JONY FONU 2HONY 4ONY)
# print(cap2.lower()) # (jony fonu 2hony 4ony)
# ? -------------------------------------- 014 ------------------------------------------------------
# ? split() + rsplit() الطبيعي بتعها تقطيع المسطره الي بين الكلام 

# a = "I Love Python and PHP and MySQL"
# print(a.split()) #? قطعنا المسطره 

# b = "I-Love-Python-and-PHP-and-MySQL"
# print(b.split("-")) #? قطعنا ال - ['I', 'Love', 'Python', 'and', 'PHP', 'and', 'MySQL']

# print(b.split("-",2)) # ? قطعنا ال - وحددنا عدد التقطيع كام مره ['I', 'Love', 'Python-and-PHP-and-MySQL']

# c = "I- Love-Python-and-PHP- and- MySQL"
# print(c.rsplit("-",3)) # ? يعمل تقطيع من الشمال مع تديد العدد 

# ? center(العدد ,"") تستخدم لاضافه حروف قبل وبعد المتغير الذي سوف تستخدمه ويتم العد من بعد عدد الحروف الذي لديك

# e = "Osama"
# print(e.center(9))  # Spaces
# print(e.center(9, "#"))  # Hashes
# print(e.center(15, "@"))  # @
# print(e.center(100,"^"))

# ? count("string",Start,End) تستخدم للبحث عن عدد وجود الحرف او الكلمه الذي سوف تستخدمها
# f = "I Love Python and PHP Because PHP PHP is Easy I I "
# print(f.count("PHP"))  # 3 PHP Words
# print(f.count("I",5)) # كدا هيبحث من اول 5 الي النهاية 
# print(f.count("PHP", 20, 34))  # ? تستخدم بهذا الشكل للبحث من اول كذا الي كذا 

# ? swapcase() تجعل الحرف بدل ما يكون صغير تجعله كبير والعكس
# g = "I Love Python"
# h = "i lOVE pYTHON"

# print(g.swapcase())
# print(h.swapcase())
# ? startswith() تستخدم لمعرفه المتغير يبداء بشي معين الذي سوف تضعه ام لا
# B~  startswith("String",Start,End)

# i = "I Love Python JavaScript"
# print(i.startswith("I"))
# print(i.startswith("J", 14))
# print(i.startswith("P", 7, 12))  # ويمكننا وضع بدايه ونهايه

# B~  endswith("String",Start,End)

# j = "I Love Python JS"
# print(j.endswith("S"))
# print(j.endswith("n", 7, 13))
# print(j.endswith("e", 2, 6))
# ? -------------------------------------- 015 ------------------------------------------------------
# ? index(SubString, Start, End) تستخدم للبحث عن كلمه او حرف معين ويمكن وضع نهايه وبدايه
#! print(a.index("P", 0, 5))  # Through Error اذا لم يجد الشي الذي تبحث عنه سوف يعمل Error

# a = "I Love Python"
# print(a.index("P"))  # Index Number 7
# print(a.index("Love"))  # Index Number 2
# print(a.index("n")) # Index Number 12
# print(a.index("P", 0, 10))  # Index Number 7

# ? find(SubString, Start, End)  تستخدم للبحث عن كلمه او حرف معين ويمكن وضع نهايه وبدايه
#? print(b.find("P", 0, 5))  # -1 اذا لم يجد الذي تبحث عنه سوف يطبع لك
# b = "I Love Python"
# print(b.find("o"))  # Index Number 3
# print(b.find("P", 0, 10))  # Index Number 7
# print(b.find("2"))

#! rjust(Width, Fill Char) نضع كلمه او حرف معين علي حسب ما تكتب انت من جها اللمين
#! ljust(Width, Fill Char) نضع كلمه او حرف معين علي حسب ما تكتب انت من جها الشمال

# c = "Osama"
# print(c.rjust(10))
# print(c.rjust(10, "#"))
# print(c.rjust(15,"*"))

# c = "Osama"
# print(c.ljust(10))
# print(c.ljust(10, "#"))
# print(c.ljust(15,"*"))

#! splitlines() تستخدم لكي تسترجع لك list اذا كانت العناصر ليست علي سطر واحد
# e = """First Line
# Second Line
# Third Line
# 1
# """
# print(e.splitlines()) # ['First Line', 'Second Line', 'Third Line', '1']

# ? expandtabs() تجعلك تتحكم في عدد ال TAB

# g = "Hello\tWorld\tI\tLove\tPython"
# print(g.expandtabs(10))

# ? istitle() تستخدم لمعرفه هل اول حرف فقط في كل جمله يبداء بحرف كبير ام لا لو اي حرف في نفس الكلمه كبير هتطلع False 
# a = "Hell And WEsda Snao My Wndy"
# b = "Hello"
# c = "22 Names"
# d = "This Is %'!?"

# print(a.istitle()) # False لان يجود اكثر من حرف كابتيل في نفس الكلمه 
# print(b.istitle())
# print(c.istitle())
# print(d.istitle())

# ? isspace() تستخدم لمعرفه هل الشي المستخدم Space ام لا مسطره
# txt = "    "
# print(txt.isspace())

# ? islower() تستخدم لمعرفه هل جميع الحروف صغيره ام لا
# five = 'i love python'
# six = 'I Love Python'
# print(five.islower())
# print(six.islower())

# ? isupper() تستخدم لمعرفه هل جميع الحروف كبيره
# a = "Hello World!"
# b = "hello 123"
# c = "MY NAME IS PETER"
# print(a.isupper()) # (False)
# print(b.isupper()) # (False)
# print(c.isupper()) # (True)

# ? isidentifier() لمعرفه هل هذا الاسم يمكن استخدمه لعمل متغير ام لا

# seven = "osama_elzero"
# eight = "OsamaElzero100"
# nine = "1OsamaElzero100"

# print(seven.isidentifier()) # True
# print(eight.isidentifier()) # True
# print(nine.isidentifier()) # False

# ? isalpha() تستخدم لمعرفه هل كل الحروف الموجوده من (a-z,A-Z)
# x = "AaaaaBbbbbb"
# y = "AaaaaBbbbbb111"
# print(x.isalpha()) # True
# print(y.isalpha()) # False

# ? isalnum() تستخدم لكي تعرف هل كل الموجود ارقام وحروف
# u = "AaaaaBbbbbb"
# z = "AaaaaBbbbbb111"
# x = "21314sadASD####"
# print(u.isalnum()) # True
# print(z.isalnum()) # True
# print(x.isalnum()) # False

# ? isnumeric() (0-9) تستخدم لمعرفه هل المتغر او الشي المستخدم ارقام
# a = "\u0030"  # unicode for 0
# b = "\u00B2"  # unicode for &sup2;
# c = "omar254"
# d = "1"
# e = "15"

# print(a.isnumeric()) # True
# print(b.isnumeric()) # True
# print(c.isnumeric()) # False
# print(d.isnumeric()) # True
# print(e.isnumeric()) # True

# ? -------------------------------------- 016 ------------------------------------------------------
# ? replace(Old Value, New Value, Count) تستخدم لتبديل شي معين بشي اخر وعلي حسب كام مره تحتاج ان تبدله

# a = "Hello One Two Three One One Hello"
# print(a.replace("One", "1")) # Hello 1 Two Three 1 1 Hello
# print(a.replace("One", "1", 1)) # Hello 1 Two Three One One Hello
# print(a.replace("One", "1", 2)) # Hello 1 Two Three 1 One Hello
# print(a.replace("Hello","Welcome",1)) # Welcome One Two Three One One Hello

# ? join(Iterable) تستخدم لادخال شي معين داخل ال string

# myList = ["Osama", "Mohamed", "Elsayed"]
# print("-".join(myList)) # Osama-Mohamed-Elsayed
# print(" & ".join(myList)) # Osama & Mohamed & Elsayed
# print(", ".join(myList)) # Osama, Mohamed, Elsayed
# print(type(", ".join(myList))) # <class 'str'>
# kano = "KANO"
# print("-".join(kano)) # K-A-N-O
# ? -------------------------------------- 017 ------------------------------------------------------
# ------------------------
# ? -- Strings Formatting -- هذا الشكل القديم لل
# ------------------------
# name = "Omar"
# age = 22
# rank = 1

#! %s => Omar > String عند استخدام هذا تعني ان اول متغير سوف تستخدمه هو
#! %d => 22 > Number عند استخدام هذا تعني ان اول متغير سوف تستخدمه هو
#! %f => 1.000000 > Float عند استخدام هذا تعني ان اول متغير سوف تستخدمه هو
# ! لتحديد عدد الحروف الارقام نستخمد هذه الطريقه 
# ? %.3s - %.3f

# print("My Name is: " + name) # My Name is: Omar
# print("My Name is:" , name) # My Name is: Omar
# print("My Name is: " + name + " and My Age is :" , age) # My Name is: Omar and My Age is : 22
# print("My Name is:" , name , "and My Age is :" , age) # My Name is: Omar and My Age is : 22
# print("My Name is: " + name + " and My Age is: " + age)  # Type Error

# print("My Name is: %s" % "Omar")
# print("My Name is: %s" % name)
# print("My Name is: %s and My Age is: %d" % (name, age))
# print("My Name is: %s and My Age is: %d and My Rank is: %f" % (name, age, rank))

# n = "Omar"
# lg = "JavaScript"
# m = 2
# print("My Name Is %s And Learn Programing in %d MOnth My Lang Learing Is %s" % (n, m, lg))
# print("Name : %.2s"%(n)) # Name : Om 
# myNumber = 10
# print("My Number is: %d" % myNumber) # My Number is: 10
# print("My Number is: %f" % myNumber) # My Number is: 10.000000
# print("My Number is: %.3f" % myNumber) # My Number is: 10.000

# myLongString = "Hello Peoples I Love You All"
# print("Message is %s" % myLongString) # Message is Hello Peoples I Love You All
# print("Message is %.13s" % myLongString) # Message is Hello Peoples

# ? -------------------------------------- 018 ------------------------------------------------------
# ---------------------------------
# -- Strings Formatting New Ways --
# ---------------------------------
# name = "Omar"
# age = 22
# rank = 20

# print("My Name is: {}".format("AHMED")) # My Name is: AHMED
# print("My Name is: {}".format(name)) # My Name is: Omar
# print("My Name is: {} My Age: {}".format(name, age)) # My Name is: Omar My Age: 22
# print("My Name Is: {:s} Age = {:d} & Rank Is: {:f}".format(name, age, rank))

# n = "Omar"
# l = "Python"
# y = 6

# print("My Name is {:s} Iam {:s} Developer With {:d} Years Exp".format(n, l, y))

# ? {:.3f} Control Floating Point Number للتحكم في عدد الاصفار الذي تاتي بعد العلامه العشريه باستخدام ال
# myNumber = 10
# print("My Number is: {:d}".format(myNumber))
# print("My Number is: {:f}".format(myNumber))
# print("My Number is: {:.3f}".format(myNumber))

# ? {:.5s} Truncate String تستخدم للتحكم في عدد الحروف الذي تريد عرضها ف ال
# myLongString = "Hello Peoples I Love You All"
# print("Message is {}".format(myLongString)) # Message is Hello Peoples I Love You All
# print("Message is {:.20}".format(myLongString)) # Message is Hello Peoples I Love
# print("Message is {:.13s}".format(myLongString)) # Message is Hello Peoples

# ? {:_d} Format Money بعض العلامات تستخدم لكي تضعها بين كل 3 ارقام

# myMoney = 500162350198

# print("My Money in Bank Is: {:d}".format(myMoney)) # My Money in Bank Is: 500162350198
# print("My Money in Bank Is: {:_d}".format(myMoney)) # My Money in Bank Is: 500_162_350_198
# print("My Money in Bank Is: {:,d}".format(myMoney)) # My Money in Bank Is: 500,162,350,198

# B~ ReArrange Items
# ? التحكم من خلال index المتغير 

# a, b, c = "One", "Two", "Three"
# print("Hello {} {} {}".format(a, b, c))  # Hello One Two Three
# print("Hello {1} {2} {0}".format(a, b, c))  # Hello Two Three One
# print("Hello {2} {0} {1}".format(a, b, c))  # Hello Three One Two
# print("Plus {1} + {0} == {2}".format(a,b,c)) # Plus Two + One == Three

#? احدث طريقه لل format هي دي 

# x, y, z = 10, 20, 30
# print("Hello {} {} {}".format(x, y, z)) # Hello 10 20 30
# print("Hello {1:d} {2:d} {0:d}".format(x, y, z)) # Hello 20 30 10
# print("Hello {2:f} {0:f} {1:f}".format(x, y, z)) # Hello 30.000000 10.000000 20.000000
# print("Equal {2:d} = {1:d} + {0:d}".format(x,y,z)) # Equal 30 = 20 + 10
# print("Hello {2:.2f} {0:.3f} {1:.3f}".format(x, y, z)) # Hello 30.00 10.000 20.000

# print(f"Hello {z:.2f} {x:.3f} {y:.3f}") # Hello 30.00 10.000 20.000
# print(f"Hello {z:.2f} AND {x:.1f}") # Hello 30.00 AND 10.0

# ! Get This From Searching ( pyformat.info ) Website

# discount = 30  # %
# price = 499.99
# new_price = price * (1-discount/100)

# # B~ 3.10.3. Old school (%)

# print("SALE: Get %d%% off the new PS5 and pay $%.0f instead of $%.2f." %
#       (discount, new_price, price))

# # B~ 3.10.4. Format method (.format())

# print("SALE: Get {:d}% off the new PS5 and pay ${:.0f} instead of ${:.2f}."
#       .format(discount, new_price, price))

# # b~ 3.10.5. F-string (f"")

# print(
#     f"SALE: Get {discount:d}% off the new PS5 and pay ${new_price:.0f} instead of ${price:.2f}.")

# B~ 3.10.6. String formatting with loop

# month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
# balance = [-10.45,  50.99,  0.99,  -5.76,  100.57, -78.22]

# print("{:-^30}".format('Monthly Balance'))
# for mo, bal in zip(month, balance):
#     print(f'We have ${bal:.2f} left in {mo}.')

# print('{:-<15.9}'.format('xylophone'))
# print('{:^10}'.format('test'))
# print('{:03d}'.format(50))
# print('{:->10}'.format('test'))
# print('{:-<10}'.format('test'))
# print('{:-<10.9}'.format('xylophone'))
# print('{:05.1f}'.format(3.141592653589793))
# print('{:$>5.1f}'.format(3.141592653589793))
# print('{:0<5.1f}'.format(3.141592653589793))
# print('{: d}'.format((23)))
# print('{: 10d}'.format((23)))

# data = {'first': 'Hodor?', 'last': 'Hodor!'}
# print('{first} {last}'.format(**data))

# person = {'first': 'Jean-Luc', 'last': 'Picard'}
# print('{p[first]} {p[last]}'.format(p=person))

# data = [4, 8, 15, 16, 23, 42]
# print('{v[3]} {v[5]}'.format(v=data))

# class Plant(object):
#     type = 'Test Jango'

# print('{p.type}'.format(p=Plant()))

# class Plant(object):
#     type = 'tree'
#     kinds = [{'name': 'oak'}, {'name': 'maple'}]

# print('{p.type}: {p.kinds[1][name]}'.format(p=Plant()))

# print('{:.{prec}} = {:.{prec}f}'.format('Gibberish', 2.7182, prec=5))

# print('{:5.2f}'.format(2.7182))
# print('{:{width}.{prec}f}'.format(2.7182, width=5, prec=2))

# print('{:.3} = {:.3}'.format('Gibberish', 2.7182))
# print('{:{prec}} = {:{prec}}'.format('Gibberish', 2.7182, prec='.3'))

# print('{:{}{}{}.{}}'.format(2.7182818284, '>', '+', 10, 3))
# ? -------------------------------------- 019 ------------------------------------------------------
# -------------
# -- Numbers --
# -------------
# ? Integer هذا نوع الذي يكون رقم لسه به اي كسور
# print(type(1))
# print(type(100))
# print(type(10))
# print(type(-10))
# print(type(-110))
# -------------
# ? Float هذا نوع يكون بجانبه كسور
# print(type(1.500))
# print(type(100.99))
# print(type(-10.99))
# print(type(0.99))
# print(type(-0.99))
# -------------
# Complex
# -------------
# [1] You Can Convert From Int To Float or Complex -- يمكنك تحويل نوع float الي complex
# [2] You Can Convert From Float To Int or Complex -- يمكنك تحويا نوع int الي complex
# [3] You Cannot Convert Complex To Any Type -- لا يمكن تحويل نوع complex الي اي شي اخري

# myComplexNumber = 5+7j

# print(type(myComplexNumber))
# للحصول علي الرقم الاول نستخدم real 
# print(f"Real Part Is: {myComplexNumber.real}")
# للحصول علي الرقم الثاني نستخدم imag 
# print(f"Imaginary Part Is: {myComplexNumber.imag}")

# print(float(10+95j)); print(int(10+9j)) # ERROR
# ? -------------------------------------- 020 ------------------------------------------------------
# --------------------------
# -- Arithmetic Operators --
# --------------------------
# ? [+] Addition الجمع
# ? [-] Subtraction الطرح
# ? [*] Multiplication الضرب
# ? [/] Division القسمه  ( float Number )
# ? [%] Modulus باقي القسمه
# ? [**] Exponent الاوس
# ? [//] Floor Division  ( int Number )
# --------------------------
# Addition جمع 

# print(10 + 30)  # 40
# print(-10 + 20)  # 10
# print(1 + 2.66)  # 3.66
# print(1.2 + 1.2)  # 2.4

# Subtraction طرح 

# print(60 - 30)  # 30
# print(-30 - 20)  # -50
# print(-30 - -20)  # -10
# print(5.66 - 3.44)  # 2.22

# Multiplication

# print(10 * 3)  # 30
# print(5 + 10 * 100)  # 1005 هنا ضرب الاول 
# print((5 + 10) * 100)  # 1500 هنا جمع الاول لان استخدمنا الاقواس () 

# Division

# print(100 / 20)  # 5.0
# print(int(100 / 20))  # 5

# ? Modulus باقي القسمه لو الرقم المقسوم عليه هيساوي عدد صحيح يبقي تساوي صفر غير كده يبقي تقربه لاقرب رقم وسوف تظهر النتيجه
# print(8 % 2)  # 0
# print(9 % 2)  # 1
# print(20 % 5)  # 0
# print(24 % 5)  # 4

# Exponent الاوس 

# print(2 ** 5)  # 32
# print(2 * 2 * 2 * 2 * 2)  # 32
# print(5 ** 4)  # 625
# print(5 * 5 * 5 * 5)  # 625
# print(5**4) # 625

# ? Floor Division تستخدم لمعرفه اقرب رقم يقبل القسمه علي الرقم المقابل له
# print(100 // 20)  # 5
# print(119 // 20)  # 5
# print(120 // 20)  # 6
# print(140 // 20)  # 7
# print(142 // 20)  # 7
# ? -------------------------------------- 021 ------------------------------------------------------
# -----------------------------
# t~ -- Lists  = []  -- هذا ليس نوع Array
# -----------
#! [1] List Items Are Enclosed in Square Brackets   هذا النوع متتالي
#! [2] List Are Ordered, To Use Index To Access Item  تستخدم بعدد الانديكس يبدا من الصفر
#! [3] List Are Mutable => Add, Delete, Edit   يمكننا التعديل فيها او الحذف منها
#! [4] List Items Is Not Unique   يتم كتابه العناصر وبعدها , كومه
#! [5] List Can Have Different Data Types  يمكن وضع اكثر من نوع في نفس ال list
# -----------------------------
# myAwesomeList = ["One", "Two", "One", 1, 100.5, True]

# print(myAwesomeList)  # Whole List
# print(myAwesomeList[1])  # "Two"
# print(myAwesomeList[-1])  # True
# print(myAwesomeList[-3])  # 1

# print(myAwesomeList[1:4])  # ['Two', 'One', 1]
# print(myAwesomeList[:4])  # ['One', 'Two', 'One', 1]
# print(myAwesomeList[1:])  # ['Two', 'One', 1, 100.5, True]

# print(myAwesomeList[::1])  # ['One', 'Two', 'One', 1, 100.5, True]
# print(myAwesomeList[::2])  # ['One', 'One', 100.5] كل خطوه ب 2 

# print(myAwesomeList)
# myAwesomeList[1] = 2 #تعديل علي الانديكس واحد
# myAwesomeList[-1] = False #تعديل علي الانديكس سالب واحد
# myAwesomeList[0:3] = ["A"]# تعديل من اول الانديكس صفر الي 2
# myAwesomeList[0:3] = [1, 2, 3, 4, 5, 6] # تغير قيمه من index 0 ل 2 
# print(myAwesomeList)
# ? -------------------------------------- 022 ------------------------------------------------------
# -------------------
# -- Lists Methods --
# -------------------

# t~ append() تستخدم لاضافه عنصر جديد الي ال list ولكن يتم اضافته ف الاخر

# myFriends = ["Osama", "Ahmed", "Sayed"]
# myOldFriends = ["Haytham", "Samah", "Ali"]

# myFriends.append("Alaa")
# myFriends.append(100)
# myFriends.append(150.200)
# myFriends.append(True)
# myFriends.append(myOldFriends)

# print(myFriends)
# print(myFriends[2])
# print(myFriends[6])
# print(myFriends[7])
# print(myFriends[-1])
# print(myFriends[7][2])

# t~ extend() تستخدم لادخال كذا list مع بعض بشكل طبيعي ولكن يتم اضافته ف الاخر
# a = [1, 2, 3, 4]
# b = ["A", "B", "C"]
# c = ["One", "Two"]

# a.extend(b)
# a.extend(c)

# print(a)

# t~ remove() تستخدم لحذف عنصر معين بداخل ال list ولكن اذا كان العنصر متكرر سوف تحذف اول عنصر فقط

# x = [1, 2, 3, 4, 5, "Osama", True, "Osama", "Osama"]
# print(x)
# x.remove("Osama")
# print(x)
# t~ sort() تستخدم لترتيب الارقام والحروف بترتيب الابجدي والحروف من الصغير للكبير وترتب نوع واحد من البيانات لبس كذا نوع

# ? sort(reverse=True) تستخدم لعكس الترتيب
# y = [1, 2, 100, 120, -10, 17, 29]
# y = ["A", "Z", "B"]
# y.sort()
# print(y)
# y.sort(reverse=True) # عكس الترتيب تستخدم هكذا 
# print(y)

# t~ reverse() تستخدم لعكس مكان العناصر بدل ما هو في الشمال يروح يمين وهكذا
# z = [10, 1, 9, 80, 50, "Osama", 100]
# z.reverse()
# print(z)

# ? -------------------------------------- 023 ------------------------------------------------------
# -------------------
# -- Lists Methods --
# -------------------
# t~ clear() تستخدم لحذف جميع عناصر ال list
# a = [1, 2, 3, 4]
# a.clear()
# print(a)

# t~ copy() تستخدم لعمل نسخ من list الي list اخري
# b = [1, 2, 3, 4]
# c = b.copy()
# print(b)  # Main List
# print(c)  # Copied List
# b.append(5)  #? عند اضافه عنصر اخر لا يظهر في ال copy
# print(b)  # Main List
# print(c)  # Copied List

# t~ count() تستخدم لعد عنصر معين موجود كام مره
# d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
# print(d.count(1))

# t~ index() تستخدم للبحث عن رقم الانديكس بتاع العنصر الذي سوف تعطيه له يبحث في اول انديكس
#? index(value,start,stop)

# e = ["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
# print(e.index("Ahmed")) # 1
# print(e.index("Ahmed",2)) # 4
# print(e.index("Ahmed",1,3)) # 1

# t~  insert() تستخدم لوضع عنصر معين قبل الانديكس الذي سوف تضعه
# f = [1, 2, 3, 4, 5, "A", "B"]
# f.insert(0, "Test")
# f.insert(-1, True)
# print(f)

# t~ pop() تستخدم ايضا لحذف اخر عنصر اذا لم تعطيها index
# t~ pop() تستخدم لوضع الانديكس ويرجع لك بقيمه هذا الانديكس ويحذفه من ال list
# g = [1, "Omar", 3, 4, 5, "A", "B"]
# print(g.pop())
# print(g.pop(3))

# ? -------------------------------------- 024 ------------------------------------------------------
# -----------------------------
# t~ -- Tuple = () --
# -----------
# [1] Tuple Items Are Enclosed in Parentheses = ()
# ? [2] You Can Remove The Parentheses If You Want يمكن ازاله الكوس بشكل عادي بدون اي مشاكل
# ~ [3] Tuple Are Ordered, To Use Index To Access Item تكون عناصر مرتبه ونستخدم الانديكس لنصل الي العنصر
# ? [4] Tuple Are Immutable => You Cant Add or Delete لايمكن التعديل بها والحذف منها عكس ال list
# [5] Tuple Items Is Not Unique
# ? [6] Tuple Can Have Different Data Types يمكن وضع اي نوع بيانات وتكررها بشكل عادي
# _ [7] Operators Used in Strings and Lists Available In Tuples -- ال operators الذب تم استخدمها في الاسترينج و ال list تستخدم هنا بشكل عادي
# -----------------------------

# ? Tuple Syntax & Type Test نوع كتابه شكل ال Tuple

# myAwesomeTuple1 = ("Osama", "Ahmed")
# myAwesomeTuple2 = "Osama", "Ahmed"

# print(myAwesomeTuple1)
# print(myAwesomeTuple2)

# print(type(myAwesomeTuple1))
# print(type(myAwesomeTuple2))

# ? Tuple Indexing نستخدم الانديكس بشكل عادي لنصل للعنصر

# myAwesomeTupleThree = (1, 2, 3, 4, 5)
# print(myAwesomeTupleThree[0])
# print(myAwesomeTupleThree[-1])
# print(myAwesomeTupleThree[-3])

#! Tuple Assign Values مش بنعرف نعدل علي الفيم الذي بداخلها 

# myAwesomeTupleFour = (1, 2, 3, 4, 5)
# myAwesomeTupleFour[2] = "Three"
# print(myAwesomeTupleFour)  # 'tuple' object does not support item assignment

# Tuple Data

# myAwesomeTupleFive = ("Osama", "Osama", 1, 2, 3, 100.5, True)
# print(myAwesomeTupleFive[0])
# print(myAwesomeTupleFive[-1])

# ? -------------------------------------- 025 ------------------------------------------------------
# -----------
# -- Tuple --
# print(f"{friends}".replace("Osama", "Elzero")) لتغير عنصر او التلاعب ب اي عنصر من عناصر ال tuple
# -----------
# Tuple With One Element

# myTuple1 = ("Osama",)  # ? لجعل نوع المتغير tuple نضع , اذا كان عنصر واحد
# myTuple2 = "Osama",

# print(myTuple1)
# print(myTuple2)

# print(type(myTuple1))
# print(type(myTuple2))

# print(len(myTuple1))
# print(len(myTuple2))

# ? Tuple Concatenation طريقه دمج البيانات بهذا الشكل
#! لا تقبل دمج مع اي نوع بيانات اخر 

# a = (1, 2, 3, 4)
# b = (5, 6)

# c = a + b
# d = a + ("A", "B", True) + b
# print(c)
# print(d)

# t~ Tuple, List, String Repeat (*) اتكرار نوع البيانات نستخدم علامه الضرب

# myString = "Osama"
# myList = [1, 2]
# myTuple = ("A", "B")

# print(myString * 3)
# print(myList * 3)
# print(myTuple * 3)

# ? Methods => count() لمعرفه عدد وجود شي معين

# a = (1, 3, 7, 8, 2, 6, 5, 8)
# print(a.count(8))

# ? index()

# b = (1, 3, 7, 8, 2, 6, 5)
# print("Index Is: {:d}".format(b.index(7))) # Index Is: 2
# print("Index Is: {:.5f}".format(b[5])) # Index Is: 6.00000
# print(f"Testing SOme Programing: {b[1]}") # Testing SOme Programing: 3
# print(f"The Position of Index Is: {b.index(6)}") # The Position of Index Is: 5
# print(f"INdex Num 6 Is : {b.index(6)}") # INdex Num 6 Is : 5
# # print("The Position of Index Is: " + b.index(7))  # ! Error

# ? Tuple Destruct _, تستخدم لتجاهل عنصر علي حسب مكان وقعه

# a = ("A", "B", 4, "C")

# x, y, _, z = a
# s , n ,_ ,e = 1,True,"SS",False
# print(x) # A
# print(y) # B
# print(z) # C

# print(s) # 1
# print(n) # True
# print(_) # SS
# print(e) # False

# ? -------------------------------------- 026 ------------------------------------------------------
# -----------------------------
# J$ -- Set => {} --
# ---------
# [1] Set Items Are Enclosed in Curly Braces => {}
# ^^ [2] Set Items Are Not Ordered And Not Indexed العناصر تكون ليست مرتبه
# ^^ [3] Set Indexing and Slicing Cant Be Done لا يستخدم الانديكس
# ^^ [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not يتم وضع نوع بيانات معينه ماعدا
# ^^ [5] Set Items Is Unique العناصر لا تكرر بداخلها
# -----------------------------
# Not Ordered And Not Indexed

# mySetOne = {10, "Ahmed", 100,(15,18,"SS")}
# print(mySetOne)
# print(mySetOne[0]) # ! ERROR لايمكن تحديد العناصر زي ال LIST

# * Slicing Can't Be Done لايمكن تحديد العناصر زي ال LIST

# mySetTwo = {1, 2, 3, 4, 5, 6}
# print(mySetTwo[0:3]) # ! ERROR

# * Has Only Immutable Data Types تقبل (Numbers, Strings, Tuples) فقط

# mySetThree = {"Osama", 100, 100.5, True, [1, 2, 3]} # ! unhashable type:'list' ERROR
# mySetThree = {"Osama", 100, 100.5, True, (1, 2, 3)}

# print(mySetThree)

# * Items Is Unique العنصر لا يتكرر لو اتكتب اكثر من مره بيظهر اكنه مره واحده 

# mySetFour = {1, 2, "Osama", "One", "Osama", 1}
# print(mySetFour)

# ? -------------------------------------- 027 ------------------------------------------------------
# -----------------
# -- Set Methods --
# -----------------
# t~ clear() لحذف العناصر

# a = {1, 2, 3}
# a.clear()
# print(a)

# t~ union() تستخدم لاتحاد او جمع بين اكثر من set

# b = {"One", "Two", "Three"}
# c = {"1", "2", "3"}
# x = {"Zero", "Cool"}

# print(b | c | x) # الطريقه الاوله لعمل اتحاد هذه
# print(b.union(c, x)) # الطريقة الثانيه والطبيعية استخدام داله union

# t~ add() تستخدم لاضافه عنصر بداخل ال set
# V_ عند اضافه اكثر من عنصر نكرر الكود ونغير العنصر

# d = {1, 2, 3, 4}
# d.add(5)
# d.add(6)
# d.add("Test")
# print(d)

# t~ copy() نسخ المحتوي الي متغير ثاني

# e = {1, 2, 3, 4}
# e.add(5) # ? كدا القيمه الذي تم اضافتها سوف تنسخ في المتغير المنسوخ
# f = e.copy() # ! Var Coped
# print(f"This Main Var : {e}")
# print(f"This Coped Var : {f}")
# e.add(6) # ! عند اضافه عنصر بهذا الشكل لايتم نسخه في ال copy لازم يكون قبل النسخ كما في الاعلي
# print(e)
# print(f)

# t~ remove() تستخدم لحذف شي معين وعند عدم وجود العنصر الذي تريد حذفه سوف يطبع ERROR

# g = {1, 2, 3, 4}
# g.remove(1)
# g.remove(7) # ! عند حذف ليس موجود سوف يطبع لك ERRoR
# print(g)

# t~ discard() تستخدم لحذف شي معين وحين عدم وجود العنصر الذي تريد حذفه لم يطبع ERROR

# h = {1, 2, 3, 4}
# h.discard(1)
# h.discard(7) # NO ERROR
# print(h)

# t~  pop() عند استخدام يطبع لك عنصر عشوائي

# i = {"A", True, 1, 2, 3, 4, 5,False}
# print(i.pop())

# t~ update() يعمل تحديث لل set من متغير ثاني

# j = {1, 2, 3}
# k = {1, "A", "B", 2}
# s = {"KILLER","MILLER"}
# j.update(['Html', "Css"])
# j.update(k)
# print(j)
# j.update([1.55,"TSA"])
# j.update(s)
# print(j)

# ? -------------------------------------- 028 ------------------------------------------------------
# -----------------
# -- Set Methods --
# -----------------
# t~ difference() تستخدم لمعرفه الاختلاف بين اي 2 set

# a = {1, 2, 3, 4}
# b = {1, 2, 3, "Osama", "Ahmed"}
# print(a)
# print(a.difference(b))  # => a - b  < {4}
# print(b.difference(a))  # => b - a  < {'Osama', 'Ahmed'}
# print(a)

# t~ difference_update() تستخدم لمعرفه الاختلاف بين اي 2 set وعمل تحديث لها 
# c = {1, 2, 3, 4}
# d = {1, 2, "Osama", "Ahmed"}
# print(c)
# c.difference_update(d)  #
# print(c)

# t~ intersection() تستخدم لمعرفه الاشياء المتكرره في المغير الاول و التاني

# e = {1, 2, 3, 4, "X"}
# f = {"Osama", "X", 2}
# print(e)
# print(f)
# print(f"intersction e & f > : {e.intersection(f)}")  # => e & f 
# print(e&f)

# t~ intersection_update() تستخدم لمعرفه الاشياء المتكرره في المغير الاول و التاني وتعمل تحديث للبيانات ويتم وضعهم في المتغير الاصلي

# g = {1, 2, 3, 4, "X", "Osama"}
# h = {"Osama", "X", 2}
# print(g)
# g.intersection_update(h)  #
# print(g)

# t~ symmetric_difference() تستخدم لمعرفه العنصر الي مش موجود في المتغير الاول و الثاني بمعني ان الي موجود في الاول وليس موجود في الثاني

# i = {1, 2, 3, 4, 5, "X",7}
# j = {"Osama", "Zero", 1, 2, 4, "X",9}
# print(i)
# print(f"symmertic_difference i ^ j > {i.symmetric_difference(j)}")  # i ^ j
# print(i^j)
# print(i)

# t~ symmetric_difference_update() تستخدم لمعرفه العنصر الي مش موجود في المتغير الاول و الثاني بمعني ان الي موجود في الاول ولبس موجود في الثاني وتعمل تحديث للمتغير الاصلي

# k = {1, 2, 3, 4, 5, "X"}
# l = {"Osama", "Zero", 1, 2, 4, "X"}
# print(k)
# k.symmetric_difference_update(l)  # k ^ l
# print(k)

# ? -------------------------------------- 029 ------------------------------------------------------
# -----------------
# -- Set Methods --
# -----------------
# t~ issuperset() لمعرفة هل عنصر ال set الاول نفس عناصر set الثاني ام لا ويرجع ب ( True _ False )

# a = {1, 2, 3, 4}
# b = {1, 2, 3}
# c = {1, 2, 3, 4, 5}
# print(a.issuperset(b))
# print(a.issuperset(c))

# t~ issubset() تستخدم لمعرفه هل ال set الاساسيه تساوي نفس عناصر ال set الثانيه

# d = {1, 2, 3, 4}
# e = {1, 2, 3}
# f = {1, 2, 3, 4, 5}
# print(d.issubset(e))  # False
# print(d.issubset(f))  # True

# t~ isdisjoint() تستخدم لمعرفه هل كل العناصر مختتلفه عن بعض

# g = {1, 2, 3, 4}
# h = {1, 2, 3}
# i = {10, 11, 12}
# print(g.isdisjoint(h))  # False
# print(g.isdisjoint(i))  # True

# ? -------------------------------------- 030 ------------------------------------------------------
# ---------------------------
# -- Dictionary --
# ----------------
# [1] Dict Items Are Enclosed in Curly Braces => {}
# [2] Dict Items Are Contains Key : Value => {"Key":"Value","Key":"Value"}
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed يستخدم جميع انواع البيانات معادا list
# [4] Dict Value Can Have Any Data Types الادخال يمكنك استخدام جميع انواع البيانات
# [5] Dict Key Need To Be Unique لا يستحب تكرار البيانات
# [6] Dict Is Not Ordered You Access Its Element With Key
# ----------------------------

# user = {
#     "name": "Osama",
#     "age": 36,
#     "country": "Egypt",
#     "skills": ["Html", "Css", "JS"],
#     "rating": 10.5
# }

# print(type(user))

# ? use dict طريقه اخري لعمل المتغيرات داخل ال Dict

# users = dict(name = "admin",age=27)
# print(users)
# print(users["name"])

# print(type(users))

# B~ get() تستخدم للمناده علي ال key

# print(user)
# print(user["skills"][2])
# print(user["skills"][1:3])
# print(user.get("skills")[1])
# print(user['country'])
# print(user.get("rating"))

# print(user.keys()) # تستخدم لطباعه كل ال keys
# print(user.values()) # تستخدم لطباعه كل ال values

# ? Two-Dimensional Dictionary عمل 2 Dict بداخل بعض 

# languages = {
#     "One": {
#         "name": "Html",
#         "progress": "80%"
#     },
#     "Two": {
#         "name": "Css",
#         "progress": "90%"
#     },
#     "Three": {
#         "name": "Js",
#         "progress": ["50%", "90%"]
#     }
# }

# print(languages['One']) # {'name': 'Html', 'progress': '80%'}
# print(languages['Three']['name']) # Js
# print(languages['Three']['progress'][1]) # 90%

# ? Dictionary Length

# print(len(languages))
# print(len(languages["Two"]))

# ? Create Dictionary From Variables

# frameworkOne = {
#     "name": "Vuejs",
#     "progress": "80%"
# }

# frameworkTwo = {
#     "name": "ReactJs",
#     "progress": "80%"
# }

# frameworkThree = {
#     "name": "Angular",
#     "progress": "80%"
# }

# allFramework = {
#     "1st": frameworkOne,
#     "2st": frameworkTwo,
#     "3th": frameworkThree
# }

# print(allFramework)
# print(allFramework["1st"]) # {'name': 'Vuejs', 'progress': '80%'}
# print(allFramework["1st"]['name']) # Vuejs

# ? -------------------------------------- 031 ------------------------------------------------------
# ------------------------
# -- Dictionary Methods --
# ------------------------

# clear()

# user = {
#     "name": "Osama"
# }
# print(user)
# user.clear()
# print(user)

# ? varname["age"] = 36 # طريقه اضافه عنصر واحد فقط
# ? update() طريقه اضافه عنصر ولكن يمكننا ان نضيف اكثر من عنصر مع بعض

# member = {
#     "name": "Osama"
# }
# print(member)
# member["age"] = 36 # طريقه اضافه عنصر
# print(member)
# member.update({"country": "Egypt","python":"80%"}) 
# print(member)

# ? copy() نسخ العناصر ولا تنسخ ال update اذا كان بعد النسخ

# main = {
#     "name": "Osama"
# }
# b = main.copy()
# print(b)
# main.update({"skills": "Fighting"})
# print(main)
# print(b)

# ? keys() طباعه المتغيرات
# ? values() طباعه القيم

# print(main.keys())
# print(main.values())

# ? -------------------------------------- 032 ------------------------------------------------------
# ------------------------
# -- Dictionary Methods --
# ------------------------

# ? setdefault() تستخدم لكي يبحث عن ال keys و value الذي سوف يتم وضعهم ان وجدهم سوف يرجع بيهم وان لم يلاقيهم سوف يعمل key جديده بال valuse الجديده

# user = {
#     "name": "Osama"
# }
# print(user)
# print(user.setdefault("age")) # value > None
# print(user)
# print(user.setdefault("name", 'Omar'))
# print(user)
# print(user.setdefault("newNa", 'Omar'))
# print(user)

# ? popitem() تستخدم لمعرفه اخر عنصر في المتغير

# member = {
#     "skill": "PS4",
#     "name": "Osama",
# }
# print(member)
# member.update({"age": 36})
# print(member.popitem())

# ? items() تستخدم لعرض ال keys , valuses حتي لو بعد اضافه عنصر جديد

# view = {
#   "name": "Osama",
#   "skill": "XBox"
# }

# allItems = view.items()
# print(view)
# view["age"] = 36
# view.update({"NOsa":50})
# print(allItems) # dict_items([('name', 'Osama'), ('skill', 'XBox'), ('age', 36), ('NOsa', 50)])

# ? fromkeys( var_value , var_keys) يتم عمل Dictionary من خلالها ونستخدم قبلها .dict

# a = ('MyKeyOne', 'MyKeyTwo', 'MyKeyThree')
# b = "X","g"
# print(dict.fromkeys(a,b)) # {'MyKeyOne': ('X', 'g'), 'MyKeyTwo': ('X', 'g'), 'MyKeyThree': ('X', 'g')}

# ? -------------------------------------- 033 ------------------------------------------------------
# -------------
# -- Boolean --
# -------------
# [1] In Programming You Need to Known Your If Your Code Output is True Or False
# [2] Boolean Values Are The Two Constant Objects False + True.
# ---------------------------------------------------------------
# True > صح
# False > خطا

# name = " "
# print(name.isspace()) # True

# print(100 > 200) # False
# print(100 > 100) # False
# print(100 > 90) # True

# ? True Values

# print(bool("Osama")) # True
# print(bool(100)) # True
# print(bool(100.95)) # True
# print(bool(True)) # True
# print(bool([1, 2, 3, 4, 5])) # True

# ? False Values

# print(bool(0)) # False
# print(bool("")) # False
# print(bool('')) # False
# print(bool([])) # False
# print(bool(False)) # False
# print(bool(())) # False
# print(bool({})) # False
# print(bool(None)) # False
# ? -------------------------------------- 034 ------------------------------------------------------
# -----------------------
# -- Boolean Operators --
# -----------------------
# and و
# or او
# not لا تستخدم لعكس من True الي False والعكس
# not >> reverse from True To False ( Reverse Logic )
# نفي النفي اثبات 
# -----------------------
# age = 36
# country = "Egypt"
# rank = 10

# ! هنا لازم كل الشروط تتحقق علشان يرجع ب True
# print(age > 16 and country == "Egypt" and rank > 0)  # True
# print(age > 16 and country == "KSA" and rank > 0)  # False

# ! اي شرط هيتحقق هريجع ب True 
# print(age > 40 or country == "KSA" or rank > 20)  # False
# print(age > 40 or country == "Egypt" or rank > 20)  # True

# ! Reverse From True To False . OR . Reverse From False To True
# print(not age > 40)  # True
# print(not age > 22)  # Not True = False

# ? -------------------------------------- 035 ------------------------------------------------------
# --------------------------
# -- Assignment Operators --
# --------------------------
# = Equal
# += Plus Equal
# -=
# *=
# /=
# **=
# %=
# //=
# --------------------------
# x = 200  # Var One
# y = 3  # Var Two

# x += y # ! x = x + y
# print(x) # 203
# x -= y # ! x = x - y
# print(x) # 200
# x *= y # ! x = x * y
# print(x) # 600
# x /= y # ! x = x / y
# print(x) # 200.0
# x **= y # ! x = x ** y
# print(x) # 8000000.0
# x %= y # ! x = x % y
# print(x) # 2.0
# x //= y # ! x = x // y
# print(x) # 0.0
# ? -------------------------------------- 036 ------------------------------------------------------
# --------------------------
# -- Comparison Operators --
# --------------------------
# [ == ] Equal تساوي
# [ != ] Not Equal لا تساوي
# [ > ] Greater Than اكبر من
# [ < ] Less Than اصغر من
# [ >= ] Greater Than Or Equal اكبر او يساوي
# [ <= ] Less Than Or Equal اصغر او يساوي
# --------------------------
# ? Equal + Not Equal

# print(100 == 100) # True
# print(100 == 200) # False
# print(100 == 100.00) # True

# print(100 != 100) # False
# print(100 != 200) # True
# print(100 != 100.00) # False

# ? Greater Than + Less Than

# print(100 > 100) # False
# print(100 > 200) # False
# print(100 > 100.00) # False
# print(100 > 40) # True

# print(100 < 100) # False
# print(100 < 200) # True
# print(100 < 100.00) # False
# print(100 < 40) # False

# ? Greater Than Or Equal + Less Than Or Equal

# print(100 >= 100) # True
# print(100 >= 200) # False
# print(100 >= 100.00) # True
# print(100 >= 40) # True

# print(100 <= 100) # True
# print(100 <= 200) # True
# print(100 <= 100.00) # True
# print(100 <= 40) # False
# ? -------------------------------------- 037 ------------------------------------------------------
# ---------------------
# -- Type Conversion --
# ! تحويل البيانات من نوع الي نوع اخري
# ----------------------
# ? str()

# a = 10
# print(type(a)) # <class 'int'>
# print(type(str(a))) # <class 'str'>

# ? tuple()
# c = "Osama"  # String
# d = [1, 2, 3, 4, 5]  # List
# e = {"A", "B", "C"}  # Set
# f = {"A": 1, "B": 2}  # Dictionary
# print(tuple(c)) # ('O', 's', 'a', 'm', 'a')
# print(tuple(d)) # (1, 2, 3, 4, 5)
# print(tuple(e)) # ('C', 'A', 'B')
# print(tuple(f)) # ('A', 'B')

# ? list()
# c = "Osama"  # String
# d = (1, 2, 3, 4, 5)  # Tuple
# e = {"A", "B", "C"}  # Set
# f = {"A": 1, "B": 2}  # Dictionary
# print(list(c))
# print(list(d))
# print(list(e))
# print(list(f))

# ? set()
# c = "Osama"  # String
# d = (1, 2, 3, 4, 5)  # Tuple
# e = ["A", "B", "C"]  # List
# f = {"A": 1, "B": 2}  # Dictionary
# print(set(c))
# print(set(d))
# print(set(e))
# print(set(f))

# ? dict() تطبق ع ال tuple + list فقط اذا كانو بهذا المنظر

# d = (("A", 1), ("B", 2), ("C", 3))  # Tuple
# e = [["One", 1], ["Two", 2], ["Three", 3]]  # List
# print(dict(d))
# print(dict(e))
# ? -------------------------------------- 038 ------------------------------------------------------
# ----------------
# -- User Input --
# ----------------
# fName = input('What\'s Is Your First Name? > ').strip().capitalize()
# mName = input('What\'s Is Your Middle Name? > ').strip().capitalize()
# lName = input('What\'s Is Your Last Name? > ').strip().capitalize()

# print(f"Hello {fName} {mName} {lName} Happy To See You.")
# print(f"Hello {fName} .{mName:.1s} {lName} Happy To See You.")

# ? -------------------------------------- 039 ------------------------------------------------------
# ---------------------------
# -- Practical Slice Email --
# ---------------------------
# theName = input('What\'s Your Name ? : ').strip().capitalize()
# theEmail = input('What\'s Your Email ? : ').strip()

# theUsername = theEmail[:theEmail.index("@")]
# theWebsite = theEmail[theEmail.index("@") +1:]

# print(f"Hello {theName} Your Email Is {theEmail}")
# print(f"Your Username Is {theUsername} \nYour Website Is {theWebsite}")

# email = "tryhackme@hotmail.org"
# print(email[:email.index("@")]) # tryhackme
# print(email[email.index("@") +1 :email.index(".")]) # hotmail
# print(email[email.index(".") +1 :]) # org
# ? -------------------------------------- 040 ------------------------------------------------------
# -------------------------------------
# -- Practical Your Age Full Details --
# -------------------------------------
# Input Age
# age = int(input('What\'s Your Age ? ').strip())

# Get Age in All Time Units

# months = age * 12
# weeks = months * 4
# days = age * 365
# hours = days * 24
# minutes = hours * 60
# seconds = minutes * 60
# print('You Lived For:')
# print(f"{months} Months.")
# ! استخدام ال :, لوضع علامه , بعد كل 3 ارقام
# print(f"{weeks:,} Weeks.")
# print(f"{days:,} Days.")
# print(f"{hours:,} Hours.")
# print(f"{minutes:,} Minutes.")
# print(f"{seconds:,} Seconds.")

# ? -------------------------------------- 041 ------------------------------------------------------
# --------------------
# --  Control Flow  --
# -- If, لو
# Elif, او لو
#  Else, غير ذالك
# -- Make Decisions --
# --------------------
# uName = "NTFSx00"
# uCountry = "Egypt"
# cName = "Python"
# cPrice = 100

# if uCountry == "Egypt":  # تستخدم لعمل شرط
#     print(f"Hello {uName} Because You Are From {uCountry}")
#     print(f"The Course '{cName}' Price Is: ${cPrice - 80}")

# elif uCountry == "KSA":  # تستخدم لعمل شرط اخر غير الاول
#     print(f"Hello {uName} Because You Are From {uCountry}")
#     print(f"The Course '{cName}' Price Is: ${cPrice - 60}")

# elif uCountry == "Kuwait":  # تستخدم لعمل شرط اخر غير الاول و الثاني
#     print(f"Hello {uName} Because You Are From {uCountry}")
#     print(f"The Course '{cName}' Price Is: ${cPrice - 50}")

# else:  # تستخدم حين عدم تحقيق اي شرط من السابقين
#     print(f"Hello {uName} Because You Are From {uCountry}")
#     print(f"The Course '{cName}' Price Is: ${cPrice - 30}")
# ? -------------------------------------- 042 ------------------------------------------------------
# ---------------
# -- Nested If -- واحده بداخل واحده
# ---------------
# uName = "Shark"
# isStudent = "Yes"
# uCountry = "KSA"
# cName = "Python Course"
# cPrice = 100

# if uCountry == "Egypt" or uCountry == "KSA" or uCountry == "Qatar":
#     if isStudent == "Yes":
#         print(f"Hi {uName} Because UR From {uCountry} And Student")

#         print(f"The \"{cName}\" Price Is: ${cPrice - 90}")
#     else:
#         print(f"Hi {uName} Because UR From {uCountry}")

#         print(f"The \"{cName}\" Price Is: ${cPrice - 60}")

# elif uCountry == "Kuwait" or uCountry == "Bahrain":
#     if isStudent == "Yes":
#         print(f"Hi {uName} Because UR From {uCountry} And Student")

#         print(f"The \"{cName}\" Price Is: ${cPrice - 50}")
#     else:
#         print(f"Hi {uName} Because UR From {uCountry}")

#         print(f"The \"{cName}\" Price Is: ${cPrice - 40}")
# else:
#     print(f"Hi {uName} Because UR From {uCountry}")
#     print(f"The \"{cName}\" Price Is: ${cPrice - 30}")
# ? -------------------------------------- 043 ------------------------------------------------------
# ----------------------------------
# -- Ternary Conditional Operator -- اختصرتها
# ----------------------------------
# country = "Egypt"
# movieRate = 17
# age = 18
# print("Movie S Not Good 4U" if age < movieRate else "Movie S Good 4U And Happy Watching")
# //______________________________________________
# name = "NTFSx00"
# age = 17
# merg = f"Welcome {name} Your Age Is : {age} You'r Is Big Man ." if age >= 18 else f"Welcome {name} Your Age Is : {age} You'r Is Small Man Sorry :(( ..!"
# print(merg)

# t~ Condition If True | If Condition | Else | Condition If False
# !___________________________________________
# score = 51
# result = "Pass" if score > 50 else "Fail" # لو ال score اكبر من 50 اطبع Pass غير كدا اطبع Fail
# print(result)
# !___________________________________________
# is_debug_mode = True
# print("Debugging ON" if is_debug_mode else "Debugging OFF") # Debugging ON
# !___________________________________________
# is_admin = True # Using a tuple (discouraged)
# access_level = ("User Access", "Admin Access")[is_admin] # True evaluates to 1, False to 0, which are used as indices
# print(access_level) # Admin Access
# !___________________________________________
# n = 0
# res = "Positive" if n > 0 else "Negative" if n < 0 else "Zero"
# print(res) # Zero
# !___________________________________________
# x = 4
# result = "P and Even" if x > 0 and x % 2 == 0 else "P and Odd" if x > 0 else "Negative or Zero"
# print(result) # P and Even
# !___________________________________________
# v1 , v2 = 100 ,200
# ! لو v1 اصغر من v2 اطبع قيمه ال v1 
# min_no = v1 if v1 < v2 else v2

# ! لو v1 اكبر من v2 اطبع قيمه ال v2 
# max_no = v1 if v1 > v2 else v2
# print(min_no) # 100
# print(max_no) # 200
# ? -------------------------------------- 044 ------------------------------------------------------
# -------------------------------------------------
# -- Calculate Age Advanced Version and Training --
# -------------------------------------------------
# Write A Very Beautiful Note
# print("-" * 80)
# # print(" You Can Write The First Letter Or Full Name of The Time Unit ".center(80, '-'))
# print("-" * 80)

# ? Collect Age Data
# age = int(input("Please Write Your Age : ").strip())

# ? Collect Time Unit Data
# unit = input("Please Choose Time Unit: Months, Weeks, Days : ").strip().lower()

# ? Get Time Units
# months = age * 12
# weeks = months * 4
# days = age * 365

# if unit == "months" or unit == "m":
    
#     print("You Choosed The Unit Months")
#     print(f"You Lived For {months:,} Months.")

# elif unit == "weeks" or unit == "w":

#     print("You Choosed The Unit Weeks")
#     print(f"You Lived For {weeks:,} Weeks.")

# elif unit == "days" or unit == "d":

#     print("You Choosed The Unit Days")
#     print(f"You Lived For {days:,} Days.")
# ? -------------------------------------- 045 ------------------------------------------------------
# --------------------------
# -- Membership Operators --
# --------------------------
# in هل العنصر موجود بداخل
# not in هل العنصر ليس موجود
# --------------------------
# ! String

# name = "Osama"
# print("s" in name)
# print("a" in name)
# print("A" in name)

# print("#" * 50)

# ! List

# friends = ["Ahmed", "Sayed", "Mahmoud"]
# print("Osama" in friends)
# print("Sayed" in friends)
# print("Mahmoud" not in friends)  # هل محمود ليس موجود

# ! Using In and Not In With Condition

# countriesOne = ["Egypt", "KSA", "Kuwait", "Bahrain", "Syria"]
# countriesOneDiscount = 80

# countriesTwo = ["Italy", "USA"]
# countriesTwoDiscount = 50

# myCountry = "KSA"

# if myCountry in countriesOne:
#     print(f"Hello You Have A Discount Equal To ${countriesOneDiscount}")
# elif myCountry in countriesTwo :
#     print(f"Hello You Have A Discount Equal => ${countriesTwoDiscount}")
# else :
#     print("You Don't Have Discount")

# @@ --------------------------------------------- تم استخدام الشكل الذي فوق بدل الي تحت اختصار

# if myCountry == "Egypt" or "KSA" or "Kuwait" or "Bahrain" or "Syria":

#     print(f"Hello You Have A Discount Equal To ${countriesOneDiscount}")

# elif myCountry == "Italy" or "USA":

#     print(f"Hello You Have A Discount Equal => ${countriesTwoDiscount}")

# else:

#     print("You Don't Have Discount")
# ? -------------------------------------- 046 ------------------------------------------------------
# ----------------------------------
# -- Practical Membership Control --
# ----------------------------------
# ? List Contains Admins
# admins = ["Ahmed", "Osama", "Sameh", "Manal", "Rahma", "Mahmoud", "Enas"]

# ? Login
# name = input('Type Your UserName : ').strip().capitalize()

# ? If Name is In Admin
# if name in admins :
#     print(f"Hello {name} Welcome Back You'r Admin User ..")
#     option = input('Type You Option > Delete or Update : ').strip().capitalize()

# ? Update Option
    # if option == "Update" or option == "U":
    #     theNewName = input("Type Your Name Update To : ").strip().capitalize()
    #     admins[admins.index(name)] = theNewName
    #     print("Name Updated.")
    #     print(admins)

# ! Delete Option
    # elif option == "Delete" or option == "D":
    #     admins.remove(name)
    #     print("Admin Deleted ..!")
    #     print(admins)

# ? Wrong Option
#     else:
#         print("Wrong Option Choosed")
# else:
#     status = input("Not Admin, Add You Y, N ? ").strip().capitalize()
#     if status == "Yes" or status == "Y":
#         print("You Have Been Added")
#         admins.append(name)
        # admins.insert(0,name) or add in index 0
    #     print(admins)
    # else:
    #     print(f"Hello {name} You'r Not Added ..")

# ? -------------------------------------- 047 ------------------------------------------------------
# -------------------
# -- Loop => While -- تستخدم لعمل تكرار علي البيانات
# -------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------
# a = 0 
# while a <= 15 :

#     print(a)

#     a += 1

# else: # ! اول ما ال True تتحول الي False نفذ الكود دا 
#     print("Loop is Done")  # True Become False
# ? -------------------------------------- 048 ------------------------------------------------------
# ----------------------------
# -- Loop => While Training --
# ----------------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------
# myF = ["Os", "Ah", "Ga", "Al", "Ra", "Sa", "Ta", "Ma", "Mo", "Wa"]

# a = 0 
# while a < len(myF):
#     print(f"#{str(a+1).zfill(2)} {myF[a]}")
#     a += 1
# else:
#     print("Loop Done")
# ? -------------------------------------- 049 ------------------------------------------------------
# ----------------------------
# -- Loop => While Training --
# -- Simple Bookmark Manage --
# ----------------------------
# # Empty List To Fill Later
# myFavouriteWebs = []

# # # Maximum Allowed Websites
# maximumWebs = 5

# while maximumWebs > 0 :
  
#     # Input The New Website
#     web = input("Website Name Without https:// ").strip().lower()
# #   # Add The New Website To The List
#     myFavouriteWebs.append(f"https://{web}")

# #   # Decrease One Number From Allowed Websites
#     maximumWebs -= 1  # maximumWebs = maximumWebs - 1

# #   # Print The Add Message
#     print(f"Website Added, {maximumWebs} Places Left")

#     #   # Print The List
#     print(myFavouriteWebs)
# else:

#   print("Bookmark Is Full, You Cant Add More")

# # # Check If List Is Not Empty
# if len(myFavouriteWebs) > 0:

# #   # Sort The List
#     myFavouriteWebs.sort()

#     index = 0

#     print("#"*60)
#     print(" Printing The List Of Websites in Your Bookmark ".center(60,"#"))
#     print("#"*60)

# while index < len(myFavouriteWebs):

#     print(f"#{str(index+1).zfill(2)} : {myFavouriteWebs[index]}")

#     index += 1  # index = index + 1
# ? -------------------------------------- 050 ------------------------------------------------------
# ----------------------------
# -- Loop => While Training --
# -- Simple Password Guess --
# ----------------------------
# tries = 4

# mainPassword = "Osama@123"

# inputPassword = input("Write Your Password: ")

# while inputPassword != mainPassword:  # True

#     tries -= 1  # tries = tries - 1

#     print(f"Wrong Password, { 'Last' if tries == 0 else tries } Chance Left")

#     inputPassword = input("Write Your Password: ")

#     if tries == 0:

#         print("All Tries Is Finished.")

#         break

# else:

#     print("Correct Password")

# ! ---- تمرين بسيط علي ال While
# my_list = []

# for x in range(1,21):

#     my_list.append(x)


# # print(my_list)

# loop = 0
# continue_num = [10,11,12,13,14,15,16,17,19]
# while loop < len(my_list):

#     my_loop = my_list[loop]

#     loop +=1

#     if my_loop in continue_num:
#         continue

#     print(my_loop)

# print(f'You Continue list Is {continue_num}')
# ----
# ? -------------------------------------- 051 ------------------------------------------------------
# -----------------
# -- Loop => For --
# -----------------
# ? for item in iterable_object :
#   Do Something With Item
# استخدمها سهل يعتمعد علي اسم لل Loop ثم المتغير الذي تعمل عليه Loop
# -----------------------------
# item Is A Vairable You Create and Call Whenever You Want
# item refer to the current position and will run and visit all items to the end
# iterable_object => Sequence [ list, tuples, set, dict, string of charcaters, etc ... ] تاخذ جميع انواع البيانات
# ---------------------------------------------------------------
# myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for number in myNumbers :

#     if number % 2 == 0:  # Even

#         print("~" * 17)

#         print(f"The Number {number} Is Even.")

#         print("~" * 17)

#     else:

#         print(f"The Number {number} Is Odd.")
# else:

#     print("The Loop Is Finished")

# myName = "Osama"

# for letter in myName:

#     print(f" [ {letter.lower()} ] ")
# ? -------------------------------------- 052 ------------------------------------------------------
# -----------------
# -- Loop => For --
# --  Trainings  --
# -----------------
# Range()
# range(start, stop, step)

# myRange = range(0, 101, 5)

# for number in myRange:

#     print(number)

# mySkills = {
#     "Html": "98%",
#     "Css": "93%",
#     "PHP": "70%",
#     "JS": "94%",
#     "Python": "49%",
#     "MySQL": "30%",
#     "R": "70%",
#     "SQLite": "54%"
# }

# print(mySkills['JS'])
# print(mySkills.get("Python"))

# for skill in mySkills:
#     print(f"My Progress in Lang : > {skill} < Value : {mySkills[skill]}")
    # # ! OR طريقه اخرى لطباعه ال Vlaue نستخدم اداه get()
    # print(f"My Progress in Lang : > {skill} < Value : {mySkills.get(skill)}")
# ? -------------------------------------- 053 ------------------------------------------------------
# -----------------
# -- Loop => For --
# -- Nested Loop --
# -----------------
# peoples = ["Osama", "Ahmed", "Sayed", "Ali"]

# skills = ['Html', 'Css', 'Js']

# for name in peoples:  # Outer Loop
# # ! هذه الطريقه ليست سليمه لعرض محتوي بداخله محتوي اخر سوف نستخدم ال Dictionary
#     print(f"{name} Skills Is: ")

#     for skill in skills:  # Inner Loop

#         print(f"- {skill}")
# Dictionary

# peoples = {
#     "Osama": {
#         "Html": "70%",
#         "Css": "80%",
#         "Js": "70%"
#     },
#     "Ahmed": {
#         "Html": "90%",
#         "Css": "80%",
#         "Js": "90%"
#     },
#     "Sayed": {
#         "Html": "70%",
#         "Css": "60%",
#         "Js": "90%",
#         "SQL": "30%"
#     }
# }

# for name in peoples:

#     print(f"{name} Skills Is: ")

#     for skill in peoples[name]:

#         print(f"{skill.upper()} => {peoples[name][skill]}")

# ? -------------------------------------- 054 ------------------------------------------------------
# > ------------------------
# -- Break, Continue, Pass --
# t~ Continue تستخدم لتفادي شي معين او عنصر معين
# t~ Break تستخدم للتوقف عند عنصر معين سوف توقف ال Loop
# t~ Pass تستخدم لعبور او تفادي loop معين
# > ------------------------
# myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Continue

# for nums in myNumbers:
#     if nums == 8:
#         continue
#     print(nums)

#  Break

# for nums in myNumbers:
#     # # ? print(nums) #J$ تفرق بين ان تطبع قبل ال break ام لا
#     if nums == 8:
#         break
#     print(nums) #V_ تفرق بين ان تطبع قبل ال break ام لا

# Pass

# for number in myNumbers:
#     if number == 13:
#         pass
#     print(number)
# ? -------------------------------------- 055 ------------------------------------------------------
# ------------------------------
# -- Advanced Dictionary Loop --
# ------------------------------
# mySkills = {
#   "HTML": "80%",
#   "CSS": "90%",
#   "JS": "70%",
#   "PHP": "80%"
# }
# print(mySkills.items())
# #######################
# for skill in mySkills:
#   print(f"{skill} => {mySkills[skill]}")
# ! ####################### هذه طريقه متقدمه لعمل loop داخل ال Dictionary
# for skill_key, skill_progress in mySkills.items():
#   print(f"{skill_key} => {skill_progress}")

# myUltimateSkills = {
#   "HTML": {
#     "Main": "80%",
#     "Pugjs": "80%"
#   },
#   "CSS": {
#     "Main": "90%",
#     "Sass": "70%",
#     "SQL": "70%"
#   },
#   "PHP": {
#     "Main": "90%",
#     "Sass": "70%",
#     "SQL": "70%"
#   }
# }
# for main_key, main_value in myUltimateSkills.items():

#   print(f"{main_key} Progress Is: ")

#   for child_key, child_value in main_value.items():

#     print(f"- {child_key} => {child_value}")
# ? -------------------------------------- 056 ------------------------------------------------------
# -------------------------
# -- Function And Return --
# -------------------------
# [1] A Function is A Reusable Block Of Code Do A Task
# [2] A Function Run When You Call It
# [3] A Function Accept Element To Deal With Called [Parameters]
# [4] A Function Can Do The Task Without Returning Data
# [5] A Function Can Return Data After Job is Finished
# [6] A Function Create To Prevent DRY
# [7] A Function Accept Elements When You Call It Called [Arguments]
# [8] There's A Built-In Functions and User Defined Functions
# [9] A Function Is For All Team and All Apps
# J$ def name():
# B~ def تستخدم لعمل متغير معين ومانداته بعد كده
# B~ return تستخدم لاسترجاع البيانات الذي بداخل ال function
# ----------------------------------------
# def function_name():

#     return "Hello Python From Inside Function Form Return"

# dataFromFunction = function_name()

# print(dataFromFunction)

# ? -------------------------------------- 057 ------------------------------------------------------
# ---------------------------------------
# -- Function Parameters And Arguments --
# V_ تستخدم بشكل طبيعي وعادي جدا زي باقي الاشياء لا يوجد فرق
# ---------------------------------------
# a, b, c = "Osama", "Ahmed", "Sayed"

# print(f"Hello {a}")
# print(f"Hello {b}")
# print(f"Hello {c}")

#! def                     => Function Keyword [Define]
#! say_hello()             => Function Name
#! name                    => Parameter
#! print(f"Hello {name}")  => Task
#! say_hello("Ahmed")      => Ahmed is The Argument

# -----
# def say_hello(name):

#   print(f"Hello {name}")

# say_hello(a)
# say_hello(b)
# say_hello(c)

# -----
# def addition(number1, number2):

#   print(number1 + number2)

# addition(100, 300)
# addition(50, 100)

# -----
# def addition(number1, number2):

#   if type(number1) != int or type(number2) != int:

#     print("Only Integers Allowed")

#   else:

#     print(number1 + number2)

# addition(100, 400)
# -----
# def full_name(first, middle, last):

#   print(f"Hello {first.strip().capitalize()} {middle.upper():.1s} {last.capitalize()}")

# full_name("   osama   ", 'mohamed', "elsayed")
# ? -------------------------------------- 058 ------------------------------------------------------
# -------------------------------------------------
# -- Function Packing, Unpacking Arguments *Args --
# _ ترجع لك بقائمة Tuple
# * تستخدم لاسترجاع البيانات بشكل عادي print(*myList)
# -------------------------------------------------
# print(1, 2, 3, 4)
# myList = [1, 2, 3, 4]

# print(myList)
# print(*myList) # => print(1, 2, 3, 4)

# def say_hello(*pepole): #@@ تستخدم عند عدم معرفه عدد العناصر الذي لديك او بيتم زياده او التعديل كل فتره

#     for name in pepole:

#         print(f"Hello {name}")

# say_hello("Osama", "Ahmed", "Sayed", "Mahmoud","Sona","Hany") #@@ ياخذ عدد غير محدود من العناصر

# def show_details(name,*skills): # كدا عملنا متغير ياخذ الاسم والثاني عدد لان نهائي من ال skills بشكل طبيعي 

#     print(f"Hello {name} Your Skills Is :")

#     for skill in skills:

#         print(f"Your SKill > {skill}")

# show_details("Osman", "HTML", "CSS", "JS", "Python", "MySQL","SQL Server","PHP")

# ? -------------------------------------- 059 ------------------------------------------------------
# ---------------------------------
# -- Function Default Parameters --
# ---------------------------------

# def say_hello(name = None , age = None, country = None):

#     print(f"Hello {name} Your Age is {age} and Your Country Is {country}")

# say_hello("Fona",30,"Egy")
# say_hello("Fona",30)
# say_hello("Fona")
# say_hello()

# Video 1:46
# ? -------------------------------------- 060 ------------------------------------------------------
# ----------------------------------------------------
# -- Function Packing, Unpacking Arguments **KWArgs --
# _ ترجع لك بقائمة Dict
# ----------------------------------------------------
# def show_skills(*skills): # الشكل التقليدي

#   print(type(skills)) # دي نوعها tuple 

#   for skill in skills:

#     print(f"{skill}")

# show_skills("Html", "CSS", "JS")
# ----------
# mySkills = {
#   'Html': "80%",
#   'Css': "70%",
#   'Js': "50%",
#   'Python': "80%",
#   "Go": "40%",
#   "PHP" : "30%"
# }

# def show_skills(**skills): # الشكل الجديد يقبل Dict

#   print(type(skills)) # بالشكل دا كدا Dict

#   for skill, value in skills.items():

#     print(f"{skill} => {value}")

# # # ! دي الطريقه ال Advanc
# show_skills(**mySkills) # تستخدم بهذه الطريقه لعمل فك لل dict نستخدم ** قبلها 

# show_skills(html = "70%" , css = "50%") # دي طريقه عادية 

# show_skills(mySkills) # ! Error
# show_skills(*mySkills) # ! Error

# ? -------------------------------------- 061 ------------------------------------------------------
# -----------------------------------------------------
# -- Function Packing, Unpacking Arguments Trainings --
# -----------------------------------------------------
# def show_skills(name, *skills,**skillsWithProgress):

#     print(f"Hello {name} \nSkills Without Progress Is: ")

#     for skill in skills:

#         print(f"- {skill}")

#     print("Skills With Progress Is: ")

#     for skill_key,skill_value in skillsWithProgress.items():

#         print(f"{skill_key} => {skill_value}")

# show_skills("Omar", "Js",Python="60%")

# ! ----------------------------------------------------- دي الطريقة المثالية 
# myTuple = ("Html", "CSS", "JS")

# mySkills = {
#   'Go': "80%",
#   'Python': "50%",
#   'MySQL': "80%"
# }

# def show_skills(name, *skills, **skillsWithProgres):

#   print(f"Hello {name} \nSkills Without Progress Is: ")

#   for skill in skills:

#     print(f"- {skill}")

#   print("Skills With Progress Is: ")

#   for skill_key, skill_value in skillsWithProgres.items():

#     print(f"- {skill_key} => {skill_value}")

# show_skills("Osama", *myTuple, **mySkills)
# ? -------------------------------------- 062 ------------------------------------------------------
# --------------------
# -- Function Scope --
#! لتحويل متغير من local الي Global نستخدم كلمه global ثم اسم المتغير
# --------------------
# x = 1  # Global Scope

# def one():

#   global x #? لتحويل متغير من local الي Global نستخدم كلمه global ثم اسم المتغير

#   x = 2

#   print(f"Print Variable From Function Scope {x}")

# def two():
#     x = 10

#     print(f"Print Variable From Function Scope {x}")

# one()
# print(f"Print Variable From Global Scope {x}")
# two()
# print(f"Print Variable From Global Scope After One Function Is Called {x}")
# ? -------------------------------------- 063 ------------------------------------------------------
# ------------------------
# -- Function Recursion --
# ------------------------
# ---------------------------------------------------------------------
# -- To Understand Recursion, You Need to First Understand Recursion --
# ---------------------------------------------------------------------
# ! هو عباره عن نداء ال function بداخل ال function

# x="WWWoooorrrldd"

# def cleanWord(word):

#   if len(word) == 1:

#     return word

#   if word[0] == word[1]:

#     return cleanWord(word[1:])

#   return word[0] + cleanWord(word[1:])

# print(cleanWord(x))
# ------------------------
# def recursion(num):

#     if num > 0 :

#         result = num+recursion(num-1)

#         print(result)

#     else:

#         result = 0 

#     return result

# recursion(6)
# ? -------------------------------------- 064 ------------------------------------------------------
# ------------------------
# -- Function => lambda --
# -- Anonymous Function --
# ? وظيفه مجهوله بدون اسم
# ------------------------
# [1] It Has No Name
# [2] You Can Call It Inline Without Defining It
# [3] You Can Use It In Return Data From Another Function
# [4] Lambda Used For Simple Functions and Def Handle The Large Tasks
# [5] Lambda is One Single Expression not Block Of Code
# [6] Lambda Type is Function
# -------------------------------------------------------------------
# def name_function(name, age) : return f"Hello {name} your Age Is: {age}"

# hello = lambda name, age : f"Hello {name} your Age Is: {age}" #t~ تستخدم لعمل function مجهولة

# print(name_function("Ahmed", 36))
# print(hello("Ahmed", 36))

# print(name_function.__name__) # name_function
# print(hello.__name__) # <lambda>

# print(type(name_function)) # <class 'function'>
# print(type(hello)) # <class 'function'>
# ? -------------------------------------- 065 ------------------------------------------------------
# _I
# -------------------
# -- File Handling --
# -------------------
# @@ يفتح الفايل ويمكن اضافه به عناصر جديده و لو الفايل مش موجود بيعمله
# "a" Append  Open File For Appending Values, Create File If Not Exists

# @@ يفتح الملف للقراءه لو الملف مش موجود سوف يعمل ERROR
#! "r" Read    [Default Value] Open File For Read and Give Error If File is Not Exists

# @@ يفتح الملف للكتابة في ولو الملف مش موجود سوف يتم انشاء
# "w" Write   Open File For Writing, Create File If Not Exists

# @@ يعمل لك ملف جديد لو لقي الملف هيعمل ERROR
# "x" Create  Create File, Give Error If File Exists
# --------------------------------------------------
#? open("File/Path","mode")

# @@ المكان الذي تريد عمل به الملف بشكل تفصيل
# my_file = open("E:\\HACKING\\Python\\File_Handling\\Read.txt")
# ! نخلي بلنا هنا ان لازم قبل كل \ نحط \ تانيه علشان ميعملش ERROR

# os = operating system
# import os

# @@  تستخدم لمعرفه مسار الملف الذي نحن به الي فتحينه ف ال VSCODE
#? Main Current Working Directory
# print(os.getcwd())

# @@ نستخدم هذا لمعرفه المسار بالتفصيل الذي نحن به
#! e:\HACKING\Python\Back.py
# print(os.path.abspath(__file__))

# @@ Directory For The Opened File لمعرفه مكان الملف الذي استخدمه حاليا
# print(os.path.dirname(os.path.abspath(__file__)))

# @@ Change Current Working Directory تغير مكان الملف الي مكان الذي نحن به بمعني اذا كان الملف الذي نستخدمه في مكان تاني سوف ينقله الي المكان الذي انت به
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# @@ نستخدم حرف ال r قبل المسار لكي يعرف ان هذا مكان الملف
# my_file = open(r"E:\HACKING\Python\File_Handling\Read.txt")

# ? -------------------------------------- 066 ------------------------------------------------------
# --------------------------------
# -- File Handling => Read File --
# --------------------------------
# my_file = open(r"E:\HACKING\Python\File_Handling\Read.txt","r")

# print(my_file)  # @@ File Data Object بيانات عن الفايل
# print(my_file.name) # @@ طباعه مسار الملف بالاسم كامل
# print(my_file.mode) # @@ طباعه نوع ال mode
# print(my_file.encoding) # @@ طباعه نوع التشفير

# # ? تستخدم للقراء وتقبل عدد الحروف الذي تريد قرءتها
# print(my_file.read())
# print(my_file.read(43))


# print(my_file.readline()) #? تستخدم لقراء سطر معين والي هو بيكون الاول
# print(my_file.readline()) # ? لقراء السطر الذي بعده نعمل نقس الكود مره ثانيه بعده
# print(my_file.readline(5)) # ? لقراء عدد حروف معين من السطر 


# print(my_file.readlines()) #? تستخدم لقراء السطور كلها ويرجع لك ب List
# print(my_file.readlines(30)) # ? لتحديد عدد حروف معين

# print(type(my_file.readlines())) # <class 'list'>

# for line in my_file: # @@ عمل loop علي السطور بداخل الملف 

#     print(line)

#     if line.startswith("07"):

#         break

#! Close The File
# my_file.close() # @@ تستخدم لغلق الملف بعد الانتهاء

# ? -------------------------------------- 067 ------------------------------------------------------
# -----------------------------------------------
# -- File Handling => Write and Append In File --
# -----------------------------------------------
# @@ اذا لم بكن الملف موجود سوف يتم انشاء
# ! عند استخدام نوع ال write يحذف العناصر الذي في الملف القديمة ويكتب العناصر الجديدة
# my_file_write = open(r"E:\HACKING\Python\File_Handling\write.txt","w")

# ? نكتب بداخل الملف باستخدام ال write
# my_file_write.write("Hello Form Python Learing\n")
# my_file_write.write("Third Line")

# ! هذه الطريقه لعمل تكرار لكلمه نكتبها 10 مرات
# my_file_write.write("NTFSx00\n"*10)

# @@ عند استخدام writelines بيحتاج list لكتابتاهم داخل ال file
# myList =["NTFSx00\n","NTFSx01\n","NTFSx02\n"]
# my_file_write.writelines(myList)

# t~ عند استخدام نوع ال Append يكتب العناصر الجديده علي العناصر الموجوده القديمه والملف اذا لم يكن موجود سوف يتم انشاء
# my_file_append = open(r"E:\HACKING\Python\File_Handling\append.txt", "a")
#! في معلومه مهمه ان لازم نستخدم ال \n علشان نبداء من اول السطر
# my_file_append.write("NTFS v6\n"*10)
# my_file_append.close()

# ? -------------------------------------- 068 ------------------------------------------------------
# -------------------------------------
# -- File Handling => Important Info --
# -------------------------------------
# import os

# my_file_append = open(r"E:\HACKING\Python\File_Handling\append.txt", "a")

# my_file_append.truncate(5) # @@ تستخدم لقص كلام او عدد معين من العناصر الموجوده داخل ال file ويحذف الباقي

# print(my_file_append.tell()) # @@ لمعرفه اين مؤشر الماوس ورقم المكان الذي هو به كام
#! ال newline بيتحسب ب 2 

# my_file_read = open(r"E:\HACKING\Python\File_Handling\read.txt", "r")

# my_file_read.seek(11) # @@ يجعل الموس يذهب الي الرقم الذي تضعه بمعني اكنه بدا الكتابه من هذا المكان
# print(my_file_read.read())

# my_file_append.close()
# my_file_read.close()

# @@ نستخدمها لحذف ملف او شي معين من خلال المسار بتاعه
# os.remove(r"E:\HACKING\Python\File_Handling\append.txt")
# ? -------------------------------------- 069 ------------------------------------------------------
# ------------------------
# -- Built In Functions --
# ------------------------
# t~ all() تستخدم لمعرف هل كل العناصر صحيحه اذا كان عنصر واحد خطاء سوف يرجع لك ب False
# t~ any() تستخدم لمعرفه هل اي عنصر من العناصر صح ام هل كل العناصر خطاء
# t~ bin() تستخدم لتحول اي شي الي binary للرقم الذي يفهمه الكمبيوتر 0-1
# t~ id() يرجع لك بقيمه الشي الذي تم وضعه بداخل ذاكره الجهاز
# ------------------------
# t~ all() تستخدم لمعرف هل كل العناصر صحيحه اذا كان عنصر واحد خطاء سوف يرجع لك ب False
# x = [1, 2, 3, 4]

# if all(x): # ? لو كل العناصر True 

#   print("All Elements Is True")

# else: # ? لو عنصر واحد False

#   print("Theres At Least One Element Is False")

# True_value = [1, 2, 3, 4] #@@ True
# print(all(True_value))
# False_value = [1, 2, 3, 4,""] #! Fasle
# print(all(False_value))
# @@ -------
# t~ any() تستخدم لمعرفه هل اي عنصر من العناصر صح ام هل كل العناصر خطاء
# x = [0, 0, [],1]

# if any(x): # @@ لو عنصر واحد من كله True

#   print("There's At Least One Element is True")

# else: # ! لو كل العناصر Fasle 

#   print("Theres No Any True Elements")

# True_value = [1, 0,None,False] #@@ True
# print(any(True_value))
# False_value = [0,None] #! Fasle
# print(any(False_value))
# @@ -------
# t~ bin() تستخدم لتحول اي شي الي binary للرقم الذي يفهمه الكمبيوتر 0-1
# print(bin(100))
# @@ -------
# t~ id() يرجع لك بقيمه الشي الذي تم وضعه بداخل ذاكره الجهاز
# a = 1
# b = 2

# print(id(a)) # 140718332044200
# print(id(b)) # 140718332044232
# ? -------------------------------------- 070 ------------------------------------------------------
# ------------------------
# -- Built In Functions --
# ------------------------
# t~ sum() تستخدم لجمع العناصر مع بعض الذي بداخل العنصر ويمكن الاضافه عليهم شي معين يمكنك وضعه
# t~ round() تستخدم لتقريب الرقم لاقرب قيمه عشريه
# t~ range() تستخدم لوضع من رقم معين الي رقم معين اخر ويمكن تحديد رقم القفزه الواحده كام تساوي
# t~ print("Hello", "Osama", sep=" $ ") عند استخدام كلمه sep ثم تضع اي شي تريده سوف يذيل الكومه ويضعه مكانه
# ------------------------
# t~ sum() تستخدم لجمع العناصر مع بعض الذي بداخل العنصر ويمكن الاضافه عليهم شي معين يمكنك وضعه
# ? sum(iterable, start)

# a = [1, 10, 19, 40]
# print(sum(a))
# print(sum(a, 30)) # @@ كدا هنيضف 30 علي مجموع الارقام الي بنجمعها كانه يبداء الجمع من اول 30
# ! -------
# t~ round() تستخدم لتقريب الرقم لاقرب قيمه عشريه
# ? round(number, numofdigits)

# print(round(150.501))
# print(round(150.5575, 2)) #! نستخدم ال numofdigits للتحكم في عدد الارقام العشرية

# @@ -------
# t~ range() تستخدم لوضع من رقم معين الي رقم معين اخر ويمكن تحديد رقم القفزه الواحده كام
# ? range(start, end, step) ( Defualt start=0 )

# print(list(range(0))) # start=0,end=0
# print(list(range(11))) # start=0,end=11
# print(list(range(0, 21, 2))) #@@ start=0,end=21,step=2
# @@ -------
# t~ print("Hello", "Osama", sep="  ",end="\n") عند استخدام كلمه sep ثم تضع اي شي تريده سوف يذيل الكومه ويضعه مكانه
# ? sep >> string inserted between values, default a space.
#! Defualt for comma , Is " " Space وبنغيرها باستخدام sep="*" 
# print("Hello $ Osama $ How $ Are $ You")
# print("Hello", "Osama", "How", "Are", "You", sep=" $ ") # ! كدا غيرنا ال Space ب علامه $

# ? end >> string appended after the last value, default a newline.
# t~ عند استخدم كلمه end وتضع بداخلها اي قيمه سوف يجعل السطر الاول جنب الثاني واذا لم تفعل فان ال 
#t~ Defualt value هي \n

# print("First Line",end=" * ")
# print("Second Line")
# print("Third Line")

# ? -------------------------------------- 071 ------------------------------------------------------
# ------------------------
# -- Built In Functions --
# ------------------------
# t~ abs() المسافه بين الصفر والرقم الذي سوف تضعه وترجع لك برقم موجب دئماٌ
# t~ pow() تستخدم لعمل عمليه حسابيه وهي الاوس وعند وضع قيمه اخر عنصر سوف يرجع لك بباقي القسمه بتاعت القسمه الاولي
# t~ min() تستخدم لعرض اقل عنصر موجود
# t~ max() تستخدم لعرض اعلي عنصر موجود
# t~ slice() استخدمها الطبيعي كما تعلمنا في الدرس السابق ولكن هنا يوجد بدايه ونهايه
# ------------------------
# t~ abs() المسافه بين الصفر والرقم الذي سوف تضعه وترجع لك برقم موجب دئماٌ
# t~ abs() بمعني اخر المسافة بين الصفر والرقم بتاعك

# print(abs(100))
# print(abs(-100))
# print(abs(10.19))
# print(abs(-10.19))
# @@ -------
#? pow(base, exp, mod) => Power
# t~ pow() تستخدم لعمل عمليه حسابيه وهي الاوس وعند وضع قيمه اخر عنصر سوف يرجع لك بباقي القسمه بتاعت القسمه الاولي

# print(pow(2, 5))  # 2 * 2 * 2 * 2 * 2
# print(pow(2, 5, 10))  # (2 * 2 * 2 * 2 * 2) % 10
# @@ -------
# ? min(item, item , item, or iterator)
# t~ min() تستخدم لعرض اقل عنصر موجود اذا كان رقم او حرف
#! لو حرف بيرجع باقرب حرف لل ( A )

# myNumbers = [1, 20, -50, -100, 100]
# print(min(1, 10, -50, 20, 30))
# print(min("X", "Z", "NTFSx00"))
# print(min(myNumbers))
# @@ -------
# ? max(item, item , item, or iterator)
# t~ max() تستخدم لعرض اعلي عنصر موجود
#! لو حرف بيرجع باقرب حرف لل ( Z )

# myNumbers = (1, 20, -50, -100, 100)
# print(max(1, 10, -50, 20, 30))
# print(max("X", "Z", "NTFSx00"))
# print(max(myNumbers))
# @@ -------
#? slice(start, end, step)
# t~ slice() استخدمها الطبيعي كما تعلمنا في الدرس السابق ولكن هنا يوجد بدايه ونهايه
#! Defualt start is 0

# a = ["A", "B", "C", "D", "E", "F"]
# print(a[:5])
# print(a[slice(5)]) # هيبدا من 0 الي 5
# print(a[slice(1,5,2)]) # هيبداء من 1 الي 5 وبينط في المره الوحده حركتين
# ? -------------------------------------- 072 ------------------------------------------------------
# -------------------------------
# -- Built In Functions => Map -- تستخدم لعمل loop
# -------------------------------
# [1] Map Take A Function + Iterator #@@ بتاخذ function و متغير
# [2] Map Called Map Because It Map The Function On Every Element #@@ ينفذ الكود علي جميع العناصر
# [3] The Function Can Be Pre-Defined Function or Lambda Function #@@ يتم تنفيذها علي function عاديه او lambda function
# ---------------------------------------------------------------
# Use Map With Predefined Function
# t~ map(function,iterable)

# def formatText(text):

#   return f"- {text.strip().capitalize()} -"

# myTexts = [" OSama ", "AHMED", "  sAYed  "]

# myFormatedData = map(formatText, myTexts)

# for name in list(map(formatText, myTexts)):

#   print(name)

# print("-" * 50)

# def my_map(name):

#     return f"- {name.strip().capitalize()} -" 

# for i in map(my_map,[" OSama ", "AHMED", "  sAYed  "]):
#    print(i)
# @@ ----------- lambda
# myTexts = [" OSama ", "AHMED", "  sAYed  "]

# for name in list(map(lambda name :f"- {name.strip().capitalize()} -",myTexts)):
  
#   print(name)
# ? --- OR لتسهيل قرائت الكود بيتكون داخل قوس (lambda etc...)
# myTexts = [" OSama ", "AHMED", "  sAYed  "]

# for name in list(map((lambda text: f"- {text.strip().capitalize()} -"), myTexts)):

#   print(name)

# ! My Example -------
# def my_map(num):

#     return num*2

# my_nums = [50, 10, 20, 100, 5]

# my_res = map(my_map,my_nums)

# for i in my_res:

#     print(i)
# ? -------------------------------------- 073 ------------------------------------------------------
# ----------------------------------
# -- Built In Functions => Filter --
# ----------------------------------
# [1] Filter Take A Function + Iterator #@@ بتاخذ function و متغير
# [2] Filter Run A Function On Every Element #@@ ينفذ الكود علي جميع العناصر
# [3] The Function Can Be Pre-Defined Function or Lambda Function #@@ يتم تنفيذها علي function عاديه او lambda function
# [4] Filter Out All Elements For Which The Function Return True #@@ عند تحقيق الهدف ب True يرجع لك بالقيمه غير ذالك يحذفه واكنه ليس متواجد
# [5] The Function Need To Return Boolean Value #@@ ترجع لك بقيمه False - True
# ---------------------------------------------------------------
# t~ filter(function,iterable)
# def checkNumber(num):
# ##!    if num > 10 : دا الشكل التقليدي
# ##!     return num
#     return num > 10 #@@ عند استخدام هذه الطريقه فان القيم الذي سوف ترجع هتكون True فهيطبع الرقم الي هو True بشكل عادي ومحترف

# myNumbers = [0, 0, 1, 19, 10, 20, 100, 5, 0]

# myResult = filter(checkNumber, myNumbers)

# for number in myResult:

#     print(number)
#! Example 2-----

# def checkName(name):

#     return name.startswith("O") # @@ بهذا الشكل اكنك عامل عمليه if

# myTexts = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman"]

# myReturnedData = filter(checkName, myTexts)

# for person in myReturnedData:

#     print(person)

#! Example 3----- lambda

# myNames = ["Osama", "Omer", "Smar", "Ahmed", "Sayed", "Sound", "Ameer"]

# myReturnNames = filter(lambda name: name.startswith("S"), myNames)
# for p in myReturnNames:
#     print(p)
#t~ ---------- لو مش عايز متغير اعملها بهذا الشكل 
# for p in filter(lambda name: name.startswith("S"), myNames):
#     print(p)

#! Example 4-----

# def num(nums):

#     return nums >= 10

# my_nums = range(1, 12)

# mynu = filter(num, my_nums)

# for nue in mynu:

#     print(nue)
#! > ---------- lambda
# my_nums = range(1, 12)

# mynu = filter(lambda num: num >= 10, my_nums)

# for nue in mynu:

#     print(nue)
# ? -------------------------------------- 074 ------------------------------------------------------
# ----------------------------------
# -- Built In Functions => Reduce --
# ----------------------------------
# [1] Reduce Take A Function + Iterator
# [2] Reduce Run A Function On FIrst and Second Element And Give Result #! تمجع اول عنصرين ثم ترجع لك بقيمه وتكمل الجمع علي باقي العناصر واحد وره التاني
# [3] Then Run Function On Result And Third Element
# [4] Then Run Function On Rsult And Fourth Element And So On
# [5] Till One ELement is Left And This is The Result of The Reduce
# [6] The Function Can Be Pre-Defined Function or Lambda Function #! ويمكن استخدام ال lambda function ايضا
# ---------------------------------------------------------------
#@@ from functools import reduce # لازم نعمل استدعاء لمكتبه ال reduce
# t~ reduce(function,iterable)

# def sumAll(num1, num2):

#   return num1 + num2

# numbers = [1, 8, 2, 9, 100]

# result = reduce(sumAll, numbers)

# print(result)

#! > ---------- lambda

# result_lambda = reduce(lambda num1, num2: num1 + num2, numbers)

# print(result_lambda)

# myTexts = ["Osama", "Omer", "Omar", "Ahmed", "Othman"]

#! Example -----

# def my_reduce(name1,name2):

#     return name1 , name2

# result = reduce(my_reduce,myTexts)

# print(result) # (((('Osama', 'Omer'), 'Omar'), 'Ahmed'), 'Othman')
# ? -------------------------------------- 075 ------------------------------------------------------
# ------------------------
# -- Built In Functions --
# ------------------------
#! enumerate() يعمل لك عداد ارقام بجانب ال العنصر المستخدم ويمكنك تحديد من كام يبداء
#! help() لمعرفه ما هي استخدمات ال Met او ال function وبيجبلك معلومات عنها
#! reversed() تستخدم لعكس وتغير مكان العنصر الي المكان المعكوس النحيه الثانية
# ------------------------
#t~ enumerate(iterable, start=0)

# mySkills = ["Html", "Css", "Js", "PHP"]

# mySkillsWithCounter = enumerate(mySkills,1)

# print(type(mySkillsWithCounter))

# for counter, skill in mySkillsWithCounter:

#     print(f"- {counter} Is {skill}")
#! -----
#t~ help() لمعرفه ما هي استخدمات ال Met او ال function وبيجبلك معلومات عنها
#t~ بيجبلك ال manual بتاع الحاجه الي بتحطها في 
# print(help(print))
# print(help(sum))
#! -----
#! reversed() تستخدم لعكس وتغير مكان العنصر الي المكان المعكوس النحيه الثانية
#t~ reversed(iterable)

# mySkills = ["Html", "Css", "Js", "PHP"]

# myString = "Elzero"

# for letter in reversed(myString):

#   print(letter)

# for s in reversed(mySkills):

#     print(s)
# ? -------------------------------------- 076 ------------------------------------------------------
# ---------------------------------
# -- Modules => Built In Modules --
# ---------------------------------
# [1] Module is A File Contain A Set Of Functions
#@@ عباره عن مكتبه بداخلها function معينه بتسخدمها بشكل طبيعي وعادي 
# [2] You Can Import Module in Your App To Help You
# @@ لاستخدامه لازم نتستدعي في البرنامج بتاعنا
# [3] You Can Import Multiple Modules
#@@ يمكننا استدعاء اكثر من مكتبه في البرنامج بشكل عادي
# [4] You Can Create Your Own Modules
#@@ يمكننا عمل مكتبه تخصنا احنا
# [5] Modules Saves Your Time
# @@ المكاتب معموله لتوفير الوقت والمجهود
# --------------------------------------------------
#? Import Main Module

# print(random) # @@ لعرض مكان المكتبه علي الجهاز
#! <module 'random' from 'C:\\Users\\NTFSv6\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\random.py'>

# import random,random # @@ لاستدعاء اكثر من مكتبه بهذا الشكل 

#? Show All Functions Inside Module

# print(random.__all__)
# print(dir(random)) # لعرض جميع ال function الي جوه المكتبه نستخدم dir 

# t~ نستخدم كلمه From ثم اسم المكتبه الذي نريد استدعاها ثم import * تعني جميع عناصر الشي الذي تم استدعاءه

# from random import *

#? Import One Or Two Functions From Module

# from random import randint #@@ بالشكل دا استدعينا function معينه 

# from random import randint,randrange #@@ بالشكل دا نقدر نستدعي اكثر من function

# print(f"Print Random Float {randrange(1,15)}")
# print(f"Print Random Integer {randint(1, 15)}")

# ? -------------------------------------- 077 ------------------------------------------------------
# -----------------------------------
# -- Modules => Create Your Module --
# -----------------------------------
# import sys

# print(sys.path) # @@ تستخددم هذه الطريقه لمعرفه اماكن تواجد المكاتب الي عندي كلها 

# sys.path.append(r"E:\HACKING\Python") 
# t~ لاضافة مسار جديد لمكان ال module الجديد
#! بالشكل دا كدا حطينا مكان المكتبه بتاعتنا في مجلد البحث بتاع المكاتب

# import ntfs

# print(dir(ntfs)) # show function in this module

# print(ntfs.hello("Ahmed"))

# print(ntfs.welcome("Ahmed"))

#? Alias

# import ntfs as ns
# #! لعمل اسم مستعار لل module او ال function الذي سوف نستدعيها نستخدم as ثم الاسم المستعار
# print(ns.hello("NTFSx00"))

# print(ns.welcome("NTFSx00"))

#? import some Function

# from ntfs import welcome

# print(welcome("NTFSx00"))

#? import some Function With Alias عمل اسم مستعار لل function بيكون بنفس الطريقه برضو

# from ntfs import welcome as we

# print(we("NTFSx00"))
# ? -------------------------------------- 078 ------------------------------------------------------
# ------------------------------------------
# -- Modules => Install External Packages --
# ------------------------------------------
# [1] Module vs Package
#t~ ال module عباره عن Single file جواه function بتعمل مهمه معينه
#t~ ال Package عباره عن حزمه جواه مجموعه module والملفات الخاصه بالمكاتب دي 
# [2] External Packages Downloaded From The Internet
#t~ بتنزل الحزمة الي محتاجها وقت ماتحب من الانترنت
# [3] You Can Install Packages With Python Package Manager PIP
#t~ بتستخدم حاجه اسمها pip لتنزيل هذه الحزمة او حزفها ألخ
# [4] PIP Install the Package and Its Dependencies
#t~ ال pip بينزل كل الادوات الي بتحتاجها الحزمة بشكل تلقائي
# [5] Modules List "https://docs.python.org/3/py-modindex.html"
#t~ الموقع دا بيجبلك كل ال buil-in modules وشرح ليهم وطريقه الاستخدام
# [6] Packages and Modules Directory "https://pypi.org/"
#t~ الموقع دا بيجبلك كل الحزم الموجوده ويمكنك البحث عن حزمة معينه
# [7] PIP Manual "https://pip.pypa.io/en/stable/cli/pip_install/"
#t~ موقع ال manual بتاع ال pip
# >-------------------------------------------------------------------------
# Command line for get Package
# >-------------------------------------------------------------------------
#! py -m pip --version .. لمعرفه اصدار ال pip وهل هو عندك ام لا

#! نستخدم pip لان هذه هي المسؤله عن جميع المكتبات الذي بداخل لغه Python

#! pip list .. لمعرفه جميع المكتبات الذي تم تحملها وجميع اصدرتها

#! pip -V .. لمعرفه رقم اصدار ال pip 

#! pip freeze .. لمعرفه الاصدارات الي عندك

#! pip install modules_name # pip install requests 
#t~ لتنزيل المكتبة 

#! pip install modules_name1,modules_name2 # pip install requests,pands
#t~ لتنزيل اكثر من مكتبة

#! pip install pyfiglet==verison_number # pip install requests==2.32.5
#t~ لتحميل verison معينه بيكون بهذا الشكل 

#! مثال pip install requests>=1.0
#t~ نستخدم هذه الطريقة لتحميل هذا الاصدار او الاعلي منه name_module>=number_verison

#! pip install pip --upgrade # pip install requests --upgrade
#t~ لعمل تحديث لل pip او اي مكتبه

#? ctrl+p >reload window
#@@ لعمل تحديث لل vscode من غير ما نقفله 

#! pip show requests
#t~ لمعرفة بعض المعلومات عن حزمة معينه 

# import pyfiglet

# print(dir(pyfiglet))

# print(pyfiglet.figlet_format("NTFS"))
# ? -------------------------------------- 079 ------------------------------------------------------
# -----------------------------------
# -- Date and Time => Introduction --
# -----------------------------------
# ? نستدعي مكتبه الوقت
# import datetime

# print(dir(datetime))

# print(dir(datetime.datetime))

# Print The Current Date and Time
# print(datetime.datetime.now()) #! لطباعة الوقت الحالي بجميع انواعة
# print(datetime.datetime.today())

# ? Print The Current Year
# print(datetime.datetime.now().year) #@@ لطباعة السنه فقط

# ? Print The Current Month
# print(datetime.datetime.now().month) #@@ لطباعة الشهر فقط

# ? Print The Current Day
# print(datetime.datetime.now().day) #@@ لطباعة اليوم فقط

# ? Print The Current Hour
# print(datetime.datetime.now().hour) #@@ لطباعة الساعة فقط

# ? Print The Current Minute
# print(datetime.datetime.now().minute) #@@ لطباعة الدقائق فقط

# ? Print The Current Second
# print(datetime.datetime.now().second) #@@ لطباعة الثواني فقط

# ? Print Start and End Of Date بدايه ونهاية التاريخ
# print(datetime.datetime.min) #@@ لطباعة اول وقت تم
# print(datetime.datetime.max) #@@ لطباعة اخر وقت تم

# ? لطباعة الوقت الحالي علي حسب ماتريد
# ? Print The Current Time
# print(datetime.datetime.now().time())

# ? Print The Current Time Hour
# print(datetime.datetime.now().time().hour)

# ? Print The Current Time Minute
# print(datetime.datetime.now().time().minute)

# ? Print The Current Time Second
# print(datetime.datetime.now().time().second)

# ? Print The Current Time Microsecond
# print(datetime.datetime.now().time().microsecond)

# ? Print Start and End Of Date بدايه ونهاية التاريخ الساعة,الدقائق,الثواني
# print(datetime.time.min)
# print(datetime.time.max)

# t~ لعمل وقت مخصص لك انت علي حسب ما تكبته
# ? Print Specific Date
# print(datetime.datetime(2000, 10, 25)) # @@ 2000-10-25 00:00:00
# print(datetime.datetime(2000, 10, 25, 10, 45, 55, 150364)) # @@ 2000-10-25 10:45:55.150364

# myBirthDay = datetime.datetime(2000, 6, 30,6,30)
# dateNow = datetime.datetime.now()

# print(f"My Birthday is {myBirthDay} ", end="And ")
# print(f"Date Now Is {dateNow}")

# print(f"I Lived For {dateNow - myBirthDay}")
# print(f"I Lived For {(dateNow - myBirthDay).days} Days.")

# ? -------------------------------------- 080 ------------------------------------------------------
# ----------------------------------
# -- Date and Time => Format Date --
# ----------------------------------
#@@ https://strftime.org/
# ---------------------
# import datetime

#! نستخدم function strftime لترجع لك ب String

# @@ عند استخدمها يوجد بعض الرموز الذي تطبع لك شي معين كالتالي وجميعها علي موقع باسم
# ? https://strftime.org/

# %a	Sun	Weekday as locale’s abbreviated name.
# %A	Sunday	Weekday as locale’s full name.
# %w	0	Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.
# %d	08	Day of the month as a zero-padded decimal number.
# %-d	8	Day of the month as a decimal number. (Platform specific)
# %b	لطباعة الشهر ب3 حروف Aug
# %B	لطباعه الشهر بشكل كامل August
# %m	09	Month as a zero-padded decimal number.
# %-m	9	Month as a decimal number. (Platform specific)
# %y	13	Year without century as a zero-padded decimal number.
# %Y	2013	Year with century as a decimal number.
# %H	07	Hour (24-hour clock) as a zero-padded decimal number.
# %-H	7	Hour (24-hour clock) as a decimal number. (Platform specific)
# %I	07	Hour (12-hour clock) as a zero-padded decimal number.
# %-I	7	Hour (12-hour clock) as a decimal number. (Platform specific)
# %p	AM	Locale’s equivalent of either AM or PM.
# %M	06	Minute as a zero-padded decimal number.
# %-M	6	Minute as a decimal number. (Platform specific)
# %S	05	Second as a zero-padded decimal number.
# %-S	5	Second as a decimal number. (Platform specific)
# %f	000000	Microsecond as a decimal number, zero-padded on the left.
# %z	+0000	UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).
# %Z	UTC	Time zone name (empty string if the object is naive).
# %j	251	Day of the year as a zero-padded decimal number.
# %-j	251	Day of the year as a decimal number. (Platform specific)
# %U	36	Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.
# %W	35	Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0.

# print(datetime.datetime.now().strftime("%b"))
# print(datetime.datetime.now().strftime("%B"))

# myBirthday = datetime.datetime(2000, 6, 30,18,30)

# print(myBirthday)

# print(myBirthday.strftime("%Y : %m : %d > %I : %M %p")) # 2000 : 06 : 30 > 06 : 30 PM
# print(myBirthday.strftime("%d - %B - %Y > %I - %M %p")) # 30 - June - 2000 > 06 - 30 PM

# ? -------------------------------------- 081 ------------------------------------------------------
# --------------------------
# -- Iterable vs Iterator --
# --------------------------
# Iterable
# [1] Object Contains Data That Can Be Iterated Upon
# @@ هو عباره عن العناصر الي تقدر تعمل عليها loop 
# [2] Like (String, List, Set, Tuple, Dictionary)
# ------------------------------------------
# Iterator
#? هو عباره عن اي شي لا يمكن عمل loop عليه
# @@ هو لوب ولكن بشكل اخر وراء الكواليس باستخدام Method next()
# [1] Object Used To Iterate Over Iterable Using next() Method Return 1 Element At A Time
# @@ ونستخدم iter() وهذه هي الذي تعمل اللوب
# [2] You Can Generate Iterator From Iterable When Using iter() Method
# [3] For Loop Already Calls iter() Method on The Iterable Behind The Scene
# [4] Gives "StopIteration" If Theres No Next Element
# -----------------------------------------------------------
#! Iterable

# myString = "Osama"

# myList = [1, 2, 3, 4, 5]

# for letter in myString:

#     print(letter, end=" ")

# for number in myList:

#     print(number, end=" ")

# ! كدا عملنا تحويل لل Iterable الي Iterator 

# myString = "Osama"

# myIterator = iter(myString)

#? وهذه الطريقه لطباعه عنصر وراء الاخر Used next()

# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))

# --
#@@ Easy loop
# for letter in "NTFSx00":

#     print(letter, end=" ")
# # --
# for letter in [1, 2, 3, 4, 5]:

#     print(letter, end=" ")

#@@ loop With Iterator
#@@ نفس فكره ال loop العادية اكنها هي دي بالظبط كدا
#! بياخذ ال Iterable بيعمل منه Iterator وراء الكواليس وبيفضل يعمل next(letter) لحد ما يوصل لاخر عنصر عنده

# for letter in iter("NTFSx00"):

#     print(letter, end=" ")

# ? -------------------------------------- 082 ------------------------------------------------------
# ----------------
# -- Generators --
# ----------------
# [1] Generator is a Function With "yield" Keyword Instead of "return"
# @@ عند استخدام ال yield يمكنك طباعة العنصر في الوقت المناسب لك علي حسب ما تريد ويمكنك عمل loop ايضا ويوجد بعض المميزات كالتالي
# @@ ال yield زيها زي ال return ولكن تستخدم لطباعه شي معين ف الوقت الذي تريده
# [2] It Support Iteration and Return Generator Iterator By Calling "yield"
# @@ تدعم استخدام ال Iteration + Iterator من خلال ال yield
# [3] Generator Function Can Have one or More "yield"
# @@ يمكن استخدام العديد من ال yield بشكل عادي بدون اي مشاكل
# [4] By Using next() It Resume From Where It Called "yield" Not From Begining
# @@ ويمكن استخدام ال next() لطباعه ال yield خلف بعض او يمكن طباعه شي معين ف النصف ثم تعمل باقي العمليه
# [5] When Called, Its Not Start Automatically, Its Only Give You The Control
# @@ عند البدايه لا يبداء تلقائي انت المسؤال عن البدايه والنهايه وما بالمنتصف
# -----------------------------------------------------------------
# name="ntfsv6"

# def myGenerator():
#     yield "NTFSx00"
#     yield name
#     yiled 3
#     yield 4

# myGen = myGenerator()

# print(f"Hello {next(myGen)} From Welcome In Programing")
# print(next(myGen))
# print("Hello From Python")
# print(next(myGen))
# print("Hello From Python")
# print(next(myGen))
# print("Hello From Python")

#t~ عند الطباعة بستخدام ال next اكنه بالظبط مسح العنصر الذي تم طباعته من جوه ال function

# for number in myGen:
#     print(number)

# ? -------------------------------------- 083 ------------------------------------------------------
# -------------------------
# -- Decorators => Intro --
# -------------------------
# [1] Sometimes Called Meta Programming

# [2] Everything in Python is Object Even Functions
# [3] Decorator Take A Function and Add Some Functionality and Return It
# [4] Decorator Wrap Other Function and Enhance Their Behaviour
# [5] Decorator is Higher Order Function (Function Accept Function As Parameter)
# ----------------------------------------------------------------------
# def myDecorator(func):

#     def nestedFunc():

#         print("Before")  # Message From Decorator

#         func()

#         print("After")  # Message From Decorator

#     return nestedFunc  # Return All Data

# @myDecorator # t~ نستخدمها للمناده علي ال function الام
# def sayHello():

#     print("Hello From Say Hello Function")

# #? دا الشكل المظبوط لطباعه ال Decorator
# sayHello()  # ! بعد المناده علي function الام نستدعي ال function الذي سوف نستخدمها بشكل عادي

# @myDecorator
# def sayHowAreYou():

#     print("Hello From Say How Are You Function")

# sayHowAreYou() # ! بعد المناده علي function الام نستدعي ال function الذي سوف نستخدمها بشكل عادي

#t~ هذا الشكل يعتبر قديم ولا يتم استخدامه 

# afterDecoration = myDecorator(sayHello) # @@ هذه شكل ال Decorator الطبيعي
# afterDecoration1 = myDecorator(sayHowAreYou) # @@ هذه شكل ال Decorator الطبيعي

# afterDecoration() #@@ ثم ننادي عليه هنا بشكل عادي

# sayHowAreYou() # ! بعد المناده علي function الام نستدعي ال function الذي سوف نستخدمها بشكل عادي
# afterDecoration1() #@@ ثم ننادي عليه هنا بشكل عادي
# ? -------------------------------------- 084 ------------------------------------------------------
# --------------------------------------------
# -- Decorators => Function With Parameters --
# --------------------------------------------
# def myDecorator(my_function):  # Decorator

#   def nestedFunc(num1, num2):  # Any Name Its Just For Decoration

#     if num1 < 0 or num2 < 0:

#       print("Beware One Of The Numbers Is Less Than Zero")

#     my_function(num1, num2)  # Execute Function

#   return nestedFunc  # Return All Data
# >--------------------------------------------
# def myDecoratorTwo(my_function):  # Decorator

#   def nestedFunc(num1, num2):  # Any Name Its Just For Decoration

#     print("Coming From Decorator Two")

#     my_function(num1, num2)  # Execute Function

#   return nestedFunc  # Return All Data

# @myDecorator #@@ يمكننا المناده علي 2 function الام لنفس ال function المستهدفه
# @myDecoratorTwo #@@ يمكننا المناده علي 2 function الام لنفس ال function المستهدفه
# def calculate(n1, n2):

#   print(n1 + n2)

# calculate(-5, 90)
# ! ------- Easy Test
# def dec(func):

#     def HelloFunction(name1,name2):

#         print(f"Hello {name1} And {name2}")
    
#         func(name1,name2)

#     return HelloFunction
# @dec
# def welcome(name1,name2):

#     print(f"Welcome {name1} And {name2}")

# welcome("NTFSx00","NTFSv6")
# ? -------------------------------------- 085 ------------------------------------------------------
# ----------------------------------------
# -- Decorators => Practical Speed Test --
# ----------------------------------------
# from time import time

# def myDecorator(func):  # Decorator

#     def nestedFunc(*numbers):  # Any Name Its Just For Decoration

#         for number in numbers:

#             if number < 0:

#                 print("Beware One Of The Numbers Is Less Than Zero")

#         func(*numbers)  # Execute Function

#     return nestedFunc  # Return All Data

# @myDecorator
# def calculate(n1, n2, n3, n4):

#     print(n1 + n2 + n3 + n4)

# calculate(-5, 90, 50, 150)
# ! --------------------------------

# def speedTest(func):

#     def wrapper():

#         start = time()

#         func()

#         end = time()

#         print(f"Function Running Time Is: {end - start}")
#     return wrapper

# @speedTest
# def bigLoop():

#     for number in range(1, 200):

#         print(number)

# bigLoop()

# ? -------------------------------------- 086 ------------------------------------------------------
# ----------------------------------------------------
# -- Practical => Loop on Many Iterators With Zip() --
# ----------------------------------------------------
# zip() Return A Zip Object Contains All Objects
# zip() Length Is The Length of Lowest Object
#? بترجع لك باقل عنصر عندك
# ------------------------------------------------
# list1 = [1, 2, 3, 4, 5]

# list2 = ["A", "B", "C", "D","N"]

# tuple1 = ("Man", "Woman", "Girl", "Boy", "Friend")

# dict1 = {"Name": "Osama", "Age": 36, "Country": "Egypt", "Skill": "Python","Stuuf":"Null"}


# for item1, item2, item3, item4 in zip(list1, list2, tuple1, dict1):

#     print("List 1 Item =>", item1)

#     print("List 2 Item =>", item2)

#     print("Tuple 1 Item =>", item3)

#     print("Dict 1 Key =>", item4, "=>", dict1[item4])

# ultimateList = zip(list1, list2)

# for item in ultimateList:

#     print(item)

# ? -------------------------------------- 087 ------------------------------------------------------
# -------------------------------------------------
# -- Practical => Image Manipulation With Pillow --
# ? https://pillow.readthedocs.io/en/stable/handbook/tutorial.html#using-the-image-class
# -------------------------------------------------
# t~ تم استدعاء مكتبه تعديل الصور ومن خلاللها استدعينا function Image
# from PIL import Image

#? Open The Image
#! هنا عوان الصوره وفتحها بكشل عادي
# myImage = Image.open(r"E:\HACKING\Python\pillow.jpg")

# Show The Image
# myImage.show()  # ! نستخدم ال show() لعرض الصوره

# لعرض نوع الصوره وحجمها ونوعها
# print(myImage.format, myImage.size, myImage.mode) #@@ format = JPEG , size = (553, 311) , mode = RGB

#? My Cropped Image
# t~ هنا تم استخدام ابعاد معينه لقص الصوره بالشكل الذي تريده
# @@      left,   upper,  right,  lower
# myBox = (0  ,     0,     64,      64)
# t~ تم استخدام .crop لتطبيق الابعاد الذي سوف تقصها من الصوره
# myNewImage = myImage.crop(myBox)

#? Show The New Image
# myNewImage.show()

# ! تم استخدام convert("L") لتحويل الصوره الي ابض واسود
# myConverted = myImage.convert("L")
# myConverted.show()
# ? -------------------------------------- 088 ------------------------------------------------------
# --------------------------------------------
# -- Doc String & Commenting vs Documenting --
# --------------------------------------------
# [1] Documentation String For Class, Module or Function
#@@ عباره عن شرح لحاجه معينه داخل ال function
# [2] Can Be Accessed From The Help and __doc__ Attributes
# يمكننا عرض محتوي ال Document من خلال استخدام ال ( help , __doc__)
# [3] Made For Understanding The Functionality of The Complex Code
# t~ نستخدمها لشرح كود معين ماذا يفعل
# [4] Theres One Line and Multiple Line Doc Strings
# -------------------------------------------------
# def NTFSx00_function(name):

#     ''' doc commenting''' #t~ لكتابه كومنت علي سطر واحد

# #t~ لكتابه كومنت علي اكثر من سطر
#     """ Ntfsx00 Function
#     It Say Hello From Ntfsx00
#     Parameter:
#         name => Person Name That Use Function
#     Return:
#         Return Hello Message To The Person"""

#     print(f"Hello {name} From NTFSx00")

# print(dir(NTFSx00_function))

# ! لمعرفه ما هو الكومنت المكتوب نستخدم اسم ال function.__doc__
# print(NTFSx00_function.__doc__)

# ! لمعرفه الكومنت المكتوب نستخدم ايضا help(function_name)
# help(NTFSx00_function)
# ? -------------------------------------- 089 ------------------------------------------------------
# -----------------------------------------------
# -- Installing And Use Pylint For Better Code --
# pylint.exe (name file)
# -----------------------------------------------
#@@ اول حاجه نعمل تنزيل للمكتبة 
#! terminal >> pip install pylint
# """
# This is My Module
# To Crate Function
# To Say Hello
# """
# ! للمناده علي المكتبه الذي تعدل الكود او تساعدك علي كتابه كود نظيف نستخدم هذا الامر في ال TERMINAL
# @@ pylint.py ثم Name File الذي تستخدمه
# @@ pylint.exe f:/path/file_name.py
# def say_hello(name):
#     ''' Use For Say Hello In Function'''
#     msg = "Hello"
#     print(f"{msg} {name}")
# say_hello("Omar")
# ? -------------------------------------- 090 ------------------------------------------------------
# -----------------------------------
# -- Errors And Exceptions Raising --
# -----------------------------------
# [1] Exceptions Is A Runtime Error Reporting Mechanism
#@@ تستخدم هذه الطريقه لجعل البرنامج يقف عند مشكله معينه مع اظهار الساله الذي تريد
# [2] Exception Gives You The Message To Understand The Problem
#@@ بتطبع رساله علشان تفهم المشكله
# [3] Traceback Gives You The Line To Look For The Code in This Line
#@@ بيقولك رقم السطر الي في المشكله
# [4] Exceptions Have Types (SyntaxError, IndexError, KeyError, Etc...)
# بعض اسماء ال ERRORS
# J$ [5] Exceptions List https://docs.python.org/3/library/exceptions.html
# @@  وهذا موقع به جميع انواع اسماء ال ERROR
# [6] raise Keyword Used To Raise Your Own Exceptions
#@@ نستخدم كلمه rasie قبل اسم ال ERROR ثم نكتب رساله ال ERROR
# B~ raise تستخدم لطباعه ال ERROR COde ثم بعدها نوع ال ERROR الذي تريد طباعته
# @@ raise NameError (----)
# @@ raise Exception ("FIx Your ERROR FROm HERE")
# -----------------------------------------------------------------
# x = -10

# if x < 0:

#   raise Exception(f"The Number {x} Is Less Than Zero")

#   print("This Will Not Print Because The Error") #! لا يتم طباعه اي شي بعد ال rasie

# else:

#   print(f"{x} Is Good Number and Ok")

# print('Print Message After If Condition')
# ! ------

# y = "S"

# if type(y) != int:

#     raise ArithmeticError("Only Numbers Allowed")

# print('Print Message After If Condition')
# ! ------
# names = 7841

# if type(names) != str :

#     raise TypeError("You'r Name Is No't String Values .. !")

# else:
#     print(f"Welcome {names}")
# ? -------------------------------------- 091 ------------------------------------------------------
# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# -----------------------------------
# Try     => Test The Code For Errors
#@@ تستخدم لعمل تجربه للكود
# Except  => Handle The Errors
#! الذي سوف يتم طباعته اذا تم ايجاد Error 
# ----------------------------
# Else    => If No Errors
#@@ لو مفيش Error بيطبع دا 
# Finally => Run The Code
#@@ لو حصل error او محصلش دا هيطبع ملهوش دعوه ب اي حاجه 
# ------------------------
# try:  # Try The Code and Test Errors
#   number = int(input("Write Your Age: "))

# # @@ عند كتابه رساله معينه هنا سوف يتم طباعتها اذا لم يتواجد ERROR ايضا وهنا افضل من ال else
#   print("Good, This Is Integer From Try")

# except:  # Handle The Errors If Its Found
#   print("Bad, This is Not Integer")

# # @@ نستخدم ال else لكي اذا لم يتواجد ERROR يطبع لك رساله
# else:  # If Theres No Errors
#   print("Good, This Is Integer From Else")

# # @@ نستخدم ال finally اذا وجد ERROR او لم يجد ERROR سوف يطبع لك الرساله بكل الطرق سوف تطبع
# finally:
#   print("Print From Finally Whatever Happens")

# >----------------------------------------------------
# >----------------------------------------------------
# @@ عند استخدام هذا الشكل اذا لم يجد ERROR سوف يطبع اول رساله موجوده ف ال try
# try:
#     # print(10 / 2)
#     # print(x)
#     # print(int("Hello"))

#     print("Nice Code Keep Going")

# # @@ اذا وجد ERROR بنوع ZeroDivisionError سوف يطبع لك هذه الرساله
# except ZeroDivisionError:
#     print("ERROR FroM ZeroDivisionError")

# # @@ اذا وجد ERROR بنوع NameError سوف يطبع لك هذه الرساله
# except NameError:
#     print("ERROR FroM NameError")

# # @@ اذا وجد ERROR بنوع ValueError سوف يطبع لك هذه الرساله
# except ValueError:
#     print("ERROR FroM ValueError")

# # @@ اذا وجدت اي نوع ERROR اخر اطبع الرساله دي
# except:
#     print("ERROR For Any Value")
# 11231=das
#! ----
# try :

    #   print(10/0)
    #   print("10" + 10)

# except SyntaxError:

#     print("SyntaxError Change name To name_value")

# except TypeError:

#     print("TypeError Cant + 'int' and 'str'")

# except:

#     print("All Error HEre ! :vV")

# ? -------------------------------------- 092 ------------------------------------------------------
# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# --       Advanced Example        --
# -----------------------------------
# the_file = None
# the_tries = 5 

# while the_tries > 0 :

#     try : # Try To Open The File

#         print("Enter The File Name With Absolute Path To Open")

#         print(f"You Have {the_tries} Tries Left")

#         print("Example: e:/HACKING/Python/yourfile.extension")

#         file_path = input("File Name => ").strip()

#         the_file = open (file_path,"r")

#         print(the_file.read())

#         break

#     except FileNotFoundError:

#         print("File Not Found Please Be Sure The Name is Valid")

#         the_tries -= 1

#     except:

#         print("Error Happen")

#     finally:

#         if the_file is not None:

#             the_file.close()

#             print("-" *30)

#             print("File Closed.")

# else:

#     print("All Tries Is Done Please Try Again")

# ? -------------------------------------- 093 ------------------------------------------------------
# --------------------
# -- Debugging Code --
# @@ نستخدم ال Debugging اذا كان في ERROR في كود ولا تعرف ما هو الكود الذي به ال ERROR ال Debugging يكشف لك كل هذه بكل بساطه
# @@ نضع بجانب الكود المشكوك به العلامه الحمرا لكي نرا ال Debugging الذي سوف يحدث عليه
#t~ للتشغيل نذهب لل Settings > CTRL + ,
#t~ ونكتب Debug هنلاقيها علي الشمال 
#t~ هنشغل خصيه ال Allow Breakpoints EveryWhere
# --------------------
# my_list = [1, 2, 3]

# my_dictionary = {"Name": "Osama", "Age": 36, "Country": "Egypt"}

# for num in my_list:

#   print(num)

# for key, value in my_dictionary.items():

#   print(f"{key} => {value}")

# def function_one_one():

#   print("Hello From Function One")

# function_one_one()
# ? -------------------------------------- 094 ------------------------------------------------------
# ------------------
# -- Type Hinting --
# @@ تكون عباره عن ملاحظه بسيطه لتقول ان نوع البيانات هو كذا
# B~ ال function() -> نوع البيانات
# B~ function()  -> str
# ------------------
# def say_hello(name) -> str:

#     print(f"Hello {name}")

# say_hello("Ahmed")

# def calculate(n1, n2) -> int:

#     print(n1 + n2)

# calculate(10, 40)
# ? -------------------------------------- 095 ------------------------------------------------------
# ----------------------------------
# -- Regular Expressions => Intro --
# ----------------------------------
# [1] Sequence of Characters That Define A Search Pattern
# [2] Regular Expression is Not In Python Its General Concept
# [3] Used In [Credit Card Validation, IP Address Validation, Email Validation]
# [4] Test RegEx "https://pythex.org/"
# [5] Characters Sheet "https://www.debuggex.com/cheatsheet/regex/python"
# -----------------------------------------------------------
#* \d => One digit > رقم واحد
#* \D => One non-digit > اي حاجه غير الارقام
#* \s => One whitespace > بيعلم علي المسطره " "
#* \S => One non-whitespace > بيعلم علي اي حاجه غير المسطره 
#* \w => One word character > بيعلم علي الاحرف والارقام
#* \W => One non-word character > بيعلم علي اي حاجه غير الاحرف والارقام
#* \d\s => كدا عايز رقم وراه مسطره
#* \d\d => كدا عايز رقمين واره بعض وكل ما تزود كل ما تزود رقم

#! لاستخدم ال Regular Expression نستدعي مكتبه re 
# import re
# txt = '''
# Hello Iam NTFSx00 From Python Learing Hacking
# My Number is 01236547890
# My Email Is NTFSx00@gmail.com
# @#^%*(&*(%&(!*$!
# 12312313213 132132 123132
# '''
#? findall لعرض جميع العناصر الذي تبحث عنها 
# x = re.findall(r"\w\w\w\w\w.com", txt) # ['gmail.com']
# print(x)
# ? -------------------------------------- 096 ------------------------------------------------------
# ----------------------------------------
# -- Regular Expressions => Quantifiers --
# B~ WebSite =>> https://regex101.com/
# ----------------------------------------
# *	0 or more
#! مثال > \w* > صفر او اكثر
# +	1 or more
#! مثال > \w+ > حرف واحد او اكثر 
# ?	0 or 1
#! مثال > \d? > لو رقم موجود تمام لو مش موجود اطن مفيش حاجه
# {3}	Exactly 3
#! مثال > \w{3} > هيدور علي 3 حروف فقط
# {1,3}	Between 1 and 3
#! مثال > \w{1,3} > هيدور علي الي بين 1 و 3
# {2,}	2 or more
#! مثال > \w{1,} > هيدور علي 2 او اكثر 
# (,5}	Up to 5
#! مثال > \w{,5} > من ال 0 حتي ال 5 اخرك 5

# import re
# txt = '''
# Hello Iam NTFSx00 From Python Learing Hacking
# Phone 123-148-995-44
# My Number is 01236547890
# My Email Is NTFSx00@gmail.com
# @#^%*(&*(%&(!*$!
# 12312313213 132132 123132
# '''

# x = re.findall(r"\w\w\wne\s\d\d\d-148-\d\d\d-\d\d", txt) # ['Phone 123-148-995-44']
# print(x)

# x = re.findall(r"\w+e \d*-\d+-\d*-\d+", txt) # ['Phone 123-148-995-44']
# print(x)

# x = re.findall(r"\w*\s\w{3}-\w{,3}-\w{1,}-\w{2}", txt) # ['Phone 123-148-995-44']
# print(x)

# phone = '''
# 020 9534-4648
# +1 9054956597
# '''
# phones = re.findall(r"\d{3}\s\w{4}-\w{4}", phone) # ['020 9534-4648']
# print(phones)

# phones = re.findall(r"\+\d\s\d*", phone) # ['+1 9054956597']
# print(phones)
# ? -------------------------------------- 097 ------------------------------------------------------
# -----------------------------------------------------------------------
# -- Regular Expressions => Characters Classes Training's --
# Hello Im try_ElDeep from Learing Python
# My Number Is 1545842515 s55w
# My Email eldeep@sona.net
# 123123123 123456 15288152
# -----------------------------------------------------------------------
# [0-9] > من 0 الي 9
# [^0-9] > اعرض كل حاجه معاده من 0 الي 9 
# [A-Z] > من A الي Z حروف كبيره
# [^A-Z] > اعرض كل حاجه معاده من A الي Z 
# [a-z] من a الي z حروف صغيره
# [^a-z] اعرض كل حاجه معاده من a الي z 
# [a-z0-9] > كدا الي بين a , z & 0 , 9
# [^a-z0-9] > كدا معاده الي بين a , z & 0 , 9
# \s[0-9] > اعرض الي قبله مسطره وبعده حرف واحد فقط من 0,9

# import re
# phone = '''
# 020 9534-4648
# Hello Iam NTFSx00 From Python Learing Hacking
# My Number is 01236547890
# My Email Is NTFSx00@gmail.com
# @#^%*(&*(%&(!*$!
# 12312313213 132132 123132
# +1 9054956597
# '''
# phones = re.findall(r"\s[a-z]", phone)
# print(phones)
# ! Quiz
# import re
# quiz = " ME 777 NTFSv6"
# answer = re.findall(r"\s[A-Za-z]{2}\s[0-9]{3}\s\w{,6}", quiz)
# print(answer)
# ? -------------------------------------- 098 ------------------------------------------------------
# ---------------------------------------
# -- Regular Expressions => Assertions --
# ---------------------------------------
# ?	0 or 1
#! مثال > \d? > لو رقم موجود تمام لو مش موجود اكن مفيش حاجه
# x = re.findall(r"\d{3}\s\d{4}-?\s?\d{4}",data)
# ^  Start of String
#! مثال > ^\d > لازم يبداء برقم 
# $  End of string
#! مثال > $\d > لازم ينتهي برقم 
# -------------------------
# import re
# data1 = '''
# => 541 7223 4888
# => 123 1489-9544

# 541 0321 7895 =>
# 123 9874-3247 =>

# 541 3266 0237
# 123 1405-1090'''
# x = re.findall(r"^\d{3}\s\d{4}-?\s?\d{4}$",data1,flags=re.MULTILINE)
# print(x)
# ! ----- Test for me
# data2 = '''
# +61 483026490 Astr
# +61 494330461
# +599 7703930
# +376 690615189#
# +376 690085786
# +20 1563232761**
# +20 1081664845
# +93 734149930!!
# +93 717463953
# '''
# x = re.findall(r"^\+\d*\s\d+$",data2,flags=re.MULTILINE)
# print(x)
#! ------ Test Email
# data3 = '''
# test8867@
# @test8867@
# user@example.com
# user example.com
# test8867@example.com
# some.one184@invalid.org
# dummy54547@mailinator.net
# info_my@hotmail.ru
# info_my@hotmail.RS
# '''
# x = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.[A-z]+",data3)
# x = re.findall(r"^[A-z0-9\.]+@[A-z0-9]+\.(com|org|net|ru|RS)$",data3) #! Don't Working
# print(x)
# ? -------------------------------------- 099 ------------------------------------------------------
# ----------------------------------------------------
# -- Regular Expressions => Logical Or And Escaping --
# ----------------------------------------------------
# |	  Or
#? (\d-|\d\)|\d>) > بيشوف لو بيبداء برقم و علامه - او رقم وعلامه ) او رقم وعلامه > و
# \	  Escape Special Characters
# ()  Separate Groups
#? (\d{4}) > دا كدا يسمي مجموعه مع بعض 
# -----------------------------
#? (\d-|\d\)|\d>)\s(\w+) 0R (\d-?\)?\>?)\s(\w+)
# 1- Sona
# 1) Nile
# 1> goos
# -------------------
#? (\d{3}) (\d{4}) (\d{3}|\(\d{3}\))
# 123 1258 952
# 123 1258 (952)
# -------------------
#? ^(https?://)(www\.)?(\w+)\.(net|org|com|info|me)$
# https://www.nileDeep.com
# https://sonanileDeep.org
# https://nileDeep.me
# http://nileDeep.net
# ? -------------------------------------- 100 ------------------------------------------------------
# ---------------------------------------------------------
# -- Regular Expressions => Re Module Search And FindAll --
# ---------------------------------------------------------
# search()  => Search A String For A Match And Return A First Match Only
#? تبحث عن اول شي بتدور عليه فقط يعني عنصر واحد
# findall() => Returns A List Of All Matches and Empty List if No Match
# ---------------------------------------------------------------------
# Email Pattern => [A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)
# ----------------------------------------------------------
# import re
# my_string = "NTFSx00ntfsX00"
# my_search = re.search(r"[A-Z]{2}", my_string)

# print(my_search)
# print(my_search.span()) #! (0, 2) > دي معنها انه من index 0 to 2 
# print(my_search.string) #@@ لعرض المحتوي ذات نفسه
# print(my_search.group())
# !-----------
# my_string = "sona15@gmail.com"
# is_mail = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)", my_string)
# if is_mail:
#     print(f"Your Mail Span => {is_mail.span()}")
#     print(f"Your Mail Is => {is_mail.group()}")
#     print(f"Your Mail Is => {is_mail.string}")
# else:
#     print("Type Your Mail True")
# !-------- findall
# email_input = input("Please Write Your Email: ")

# search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net", email_input)

# my_mail = []

# if search != []:

#     my_mail.append(search)

#     print(f"Your Email Added")

# else : 

#     print("Invalid Email")

# for email in my_mail:

#     print(email)

# ? -------------------------------------- 101 ------------------------------------------------------
# ----------------------------------------------------
# -- Regular Expressions => Re Module Split And Sub --
# ----------------------------------------------------
# split(Pattern, String, MaxSplit)  => Return A List Of Elements Splitted On Each Match
#! Pattern > الكود , String > النص بتاعنا , MaxSplit > عدد القص
# sub(Pattern, Replace, String, ReplaceCount) => Replace Matches With What You Want
#! Pattern > الحاجه الي عايز تغيرها , Replace > التغير الي عايز تعمله , String > النص , Count > عدد التغير
# ---------------------------------------------------------------------
# import re
# string_one = "I Love Python Programming Language"

# search_one = re.split(r"\s", string_one, 1)

# print(search_one)
# ! -----------
# string_two = "How-To_Write_A_Very-Good@Article"

# search_two = re.split(r"-|_|@", string_two)

# print(search_two)

#? Get Words From URL

# for counter, word in enumerate(search_two,1):

#   if len(word) <= 1:

#     continue

#   print(f"Word Number: {counter} => {word.lower()}")
# ! ---- sub
#! Pattern > الحاجه الي عايز تغيرها , Replace > التغير الي عايز تعمله , String > النص , Count > عدد التغير
# string_t = "How-To_Write_A_Very-Good@Article"
# print(re.sub(r"-|@","_",string_t))
# ? -------------------------------------- 102 ------------------------------------------------------
# ------------------------------------------------------
# -- Regular Expressions => Group Trainings And Flags --
# ------------------------------------------------------
# import re
# my_web = "https://www.elzero.org:8080/category.php?article=105?name=how-to-do"
#! (.+) > نستخدم ال .+ بعمني اي حاجه وكمان مش عارف العدد بتاعها 
# search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", my_web)
# print(search)
#! يتم كتابه ال flag بهذا الشكل بكل سهوله

#@@ MULTILINE > علشان يقدر يشوف اكثر من سطر
# lines = '''
# line2
# line1
# '''
# MULTILINE = re.findall(r"^[a-z0-9]+$", lines,re.MULTILINE)
# print(MULTILINE)
# !---
#@@ IGNORECASE > بيدور علي اذا كان الحروف كبيره او صغيره
# IGNORECASE = re.findall(r"osooda", "OSOODA",re.IGNORECASE)
# print(IGNORECASE)
# !---
#@@ DOTALL > بنستخدم ال . وحتي بيقدر يشوف ال Newline 
# my_str = '''OSOODA
# OSOODA'''
# DOTALL = re.findall(r"(.+)", my_str,re.DOTALL)
# print(DOTALL)
# !---
# VERBOSE = re.findall(r"osooda#Comment", "osooda",re.VERBOSE)
# #@@ VERBOSE > يمكنك عمل comment وكتابه الكومنت بتكون بهذا الشكل 
# print(VERBOSE)
# ? -------------------------------------- 103 ------------------------------------------------------
# ------------------------------------------
# -- Object Oriented Programming => Intro --
#! تستخدم لجعل الكود بكل سلسة واكثر فعاليه ويوجد منه انواع
# ------------------------------------------
# [1] Python Support Object Oriented Programming
# [2] OOP Is A Paradigm Or Coding Style
#@@ عباره عن طريقه لكتابه الكود
#     OOP Paradigm =>
#       Means Structuring Program So The Methods[Functions] and Attributes[Data]
#       Are Bundled Into Objects
# [3] Methods => Act As Function That Use The Information Of The Object
# [4] Python Is Multi-Paradigm Programming Language [Procedural, OOP, Functional]
#     - Procedural => Structure App Like Recipe, Sets Of Steps To Make The Task
#     - Functional => Built On the Concept of Mathematical Functions
# [5] OOP Allow You To Organize Your Code and Make It Readable and Reusable
# [6] Everything in Python is Object
# [7] If Man Is Object
#     - Attributes => Name, Age, Address, Phone Number, Info [Can Be Differnet]
#     - Methods[Behaviors] => Walking, Eating, Singing, Playing
# [8] If Car Is Object
#     - Attributes => Model, Colour, Price
#@@ عباره عن المعلومات عن الشي
#     - Methods[Behaviors] => Walking, Stopping
#@@ عباره عن الوظائف الذي يعملها الشي
# [9] Class Is The Template For Creating Objects [Object Constructor | Blueprint]
#     - Class Car Can Create Many Cars Object
# ---------------------------------------------
# ? -------------------------------------- 104 ------------------------------------------------------
# ----------------------------------------------------------
# -- Object Oriented Programming => Class Syntax and Info --
# ----------------------------------------------------------
# [01] Class is The Blueprint Or Construtor Of The Object
#! ال class تكون عباره عن مخطط الي من عن طريقه نقدر ننشاء المشروع الخاص بينا
# [02] Class Instantiate Means Create Instance of A Class
#! يتم انشاء من ال class ال instance وهذا عباره عن ال object الي انت بتنشاء من ال class وتاخد منه ال Methods + Attributes
# [03] Instance => Object Created From Class And Have Their Methods and Attributes
#! يمكننا استخدام ال class من خلال استخدام كلمه class
# [04] Class Defined With Keyword class
# [05] Class Name Written With PascalCase [UpperCamelCase] Style
#! يمكن ال class بتاعك يحتوي علي Methods and Attributes وممكن لا
# [06] Class May Contains Methods and Attributes
#! لمه بتنشاء object جديد لغه بايثون بتدور علي حاجه اسمها  __init__ ويتم منادتها كل لحظه انت بتنشاء في ال object من ال class المستخدمه
# [07] When Creating Object Python Look For The Built In __init__ Method
# [08] __init__ Method Called Every Time You Create Object From Class
#! تستخدم لتهياء الداته لل object الذي سوف يتم انشاءه
# [09] __init__ Method Is Initialize The Data For The Object
#! اي شي في لغه بايثون يبداء ب __name__ يسمي ال Dunder or Magic Method
# [10] Any Method With Two Underscore in The Start and End Called Dunder or Magic Method
#! يستحسن يكون اول براميتر عند انشاء ال class
# [11] self Refer To The Current Instance Created From The Class And Must Be First Param
#! ويمكن تسميته ب اي اسم عادي جدا
# [12] self Can Be Named Anything
# [13] In Python You Dont Need To Call new() Keyword To Create Object
# -------------------------------------------------------------------
# class NameClass:
#     Constructor => Do Instantiation [ Create Instance From A Class ]
#     Each Instance Is Separate Object
#     def __init__(self, other_data)
#         Body Of Function
#! يتم عمل ال class بهذا الشكل نستخدم كلمه class ثم اسمها
# class Member:
#! وهنا تم عمل function وتم استخدامها باسم __init__(self)
#   def __init__(self):

    # print(f"A New Member Has Been Added")
#! للمناده علي ال class واستخدمه بشكل عادي ننده علي اسم ال class
# Member()
# member_one = Member()
# member_two = Member()
# member_three = Member()

# print(member_one.__class__)
# ? -------------------------------------- 105 ------------------------------------------------------
# --------------------------------------------------------------------
# -- Object Oriented Programming => Instance Attributes and Methods --
# --------------------------------------------------------------------
# Self: Point To Instance Created From Class
#! ال Attributes الخاصه بال Instance بتكون داخل ال Constructor البناء
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# -----------------------------------------------------------------------
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class

# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself
# -----------------------------------------------------------
# class Member:
#     def __init__(self,first_name,middle_name,last_name):
#         self.fname = first_name
#@@ هذا هو ال Attributes
#         self.mname = middle_name
#         self.lname = last_name

# member_one = Member("Osama", "Mohamed", "elsayed")
# member_two = Member("Ahmed", "Ali", "Mahmoud")
# member_three = Member("Mona", "Ali", "Mahmoud")

# print(dir(member_one))

# print(member_one.fname, member_one.mname, member_one.lname)
# print(member_two.fname)
# print(member_three.fname)
#! --- Test
# class Cars:
#     def __init__(self,moduel,year,price):
#         self.moduel = moduel
#         self.year = year
#         self.price = price

# bmw = Cars("BMW",2024,500000)
# honda = Cars("HONDA",2025,700000)

# print(f"Moudel => ' {bmw.moduel} ' Year => ' {bmw.year} ' Price => ' {bmw.price} '")
# print(f"Moudel => ' {honda.moduel} ' Year => ' {honda.year} ' Price => ' {honda.price} '")
# ? -------------------------------------- 106 ------------------------------------------------------
# --------------------------------------------------------------------
# -- Object Oriented Programming => Instance Attributes and Methods --
# --------------------------------------------------------------------
# Self: Point To Instance Created From Class
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# -----------------------------------------------------------------------
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself
# -----------------------------------------------------------
# class Member:

# ^^ self هنا تعود علي اسم ال Instance ويمكن تغير اسمها بشكل عادي جدا وبجانبها اي متغير تريد وضعه ويتغير قمته علي حسب الادخال الذي يضعه المستخدم
    # def __init__(self, first_name, middle_name, last_name, gender):
# ^^ الذي يتم كتابته هنا يكون غير الي مكتوب بره والفرق ان هنا بداخل ال Instance وبره في ال class

# ^^ لعمل ال Methods بشكل داينامك نستدعي ال self. اسم ال Methods = قيمه ال  Methods الذي سوف تضعها حين النده عليها
        # self.fname = first_name
        # self.mname = middle_name
        # self.lname = last_name
        # self.gender = gender

    # def full_name(self):
        # return f"{self.fname} {self.mname} {self.lname}"
#! عملنا function عاديه بتعمل وظيفه معينه
    # def name_with_title(self):

        # if self.gender == "Male":
            # return f"Hello Mr {self.fname} Your Gender : {self.gender}"
        
        # elif self.gender == "Female":
            # return f"Hello Miss {self.fname} Your Gender : {self.gender}"
        
        # else:
            # return f"Hello {self.fname}"

    # def get_all_info(self):

    # ^^ ويمكننا دمج اكثر من Methods مع بعض بهذا الشكل لان كلهم مفتحوين ع بعض بشكل عادي جدا
        # return f"{self.name_with_title()}, Your Full Name Is => {self.full_name()}" 

#! هذه قيمه ال methods وطبعا لا نحسب ال self منهم نستعدي اسم ال class ثم متغيرات ال methods
# member_one = Member("NTFSx00", "Rusty", "RedTeam", "Male")
# member_two = Member("Ahmed", "Ali", "Mahmoud", "Male")
# member_three = Member("Mona", "Ali", "Mahmoud", "Female")

# print(dir(member_one))

# print(member_one.fname, member_one.mname, member_one.lname)
# print(member_two.fname)
# print(member_three.fname)

# print(member_two.full_name())
# print(member_two.name_with_title())

# print(member_one.get_all_info())
# print(member_three.get_all_info())
# ?-------------------------------- test
# class test:

#     def __init__(self, name, age, gender):

#         self.name = name
#         self.age = age
#         self.gender = gender

#     def fix_all(self):

#         if self.gender == "Male":

#             return f"Hello Mr {self.name}"

#         elif self.gender == "Female":

#             return f"Hello Miss {self.name}"

#         else:
#             return f"Hello {self.name}"

# msg_hello = test("RooT", 22, "Male")
# msg_hello1 = test("Sandy", 20, "Female")
# msg_hello2 = test("Ahmed", 20, "Male")

# msg_hello1 = msg_hello1.fix_all()
# msg_hello2 = msg_hello2.fix_all()

# print(msg_hello.fix_all())
# print(msg_hello1)
# print(msg_hello2)
# ? -------------------------------------- 107 ------------------------------------------------------
# -----------------------------------------------------
# -- Object Oriented Programming => Class Attributes --
# -----------------------------------------------------
# Class Attributes: Attributes Defined Outside The Constructor
# -----------------------------------------------------------
# class Member:

# # ^^ الذي يتم انشاءه هنا يكون بداخل ال class ليس بداخل ال Instance
#     not_allowed_names = ["Hell", "Shit", "Baloot"]

#     users_num = 0

#     def __init__(self, first_name, middle_name, last_name, gender):

#         self.fname = first_name

#         self.mname = middle_name

#         self.lname = last_name

#         self.gender = gender

#         Member.users_num += 1

#     def full_name(self):

#         if self.fname in Member.not_allowed_names:

#             raise ValueError("Name Not Allowed")

#         else:

#             return f"{self.fname} {self.mname} {self.lname}"

#     def name_with_title(self):

#         if self.gender == "Male":

#             return f"Hello Mr {self.fname}"

#         elif self.gender == "Female":

#             return f"Hello Miss {self.fname}"

#         else:

#             return f"Hello {self.fname}"

#     def get_all_info(self):

#         return f"{self.name_with_title()}, Your Full Name Is: {self.full_name()}"

#     def delete_user(self):

#         Member.users_num -= 1

#         return f"User {self.fname} Is Deleted."

# print(Member.users_num)

# member_one = Member("Osama", "Mohamed", "Elsayed", "Male")
# member_two = Member("Ahmed", "Ali", "Mahmoud", "Male")
# member_three = Member("Mona", "Ali", "Mahmoud", "Female")
# member_four = Member("Shit", "Hell", "Metal", "DD")

# print(Member.users_num)

# print(member_three.delete_user())

# print(Member.users_num)
# ? -------------------------------------- 108 ------------------------------------------------------
# -------------------------------------------------------------------
# -- Object Oriented Programming => Class Methods & Static Methods --
# -------------------------------------------------------------------
# Class Methods:
# ^^ @classmethod
# - Marked With @classmethod Decorator To Flag It As Class Method
# t~ @classmethod
# t~ def show_classmethods(cls):
# @@ اجباري وضع Parameters ال cls
# - It Take Cls Keyword to Parameter Not Self To Point To The Class not The Instance
# t~ مش محتاج تنشاء Inctance من ال class المستخدم  علشان تشغل ال Methods
# - It Doesn't Require Creation of a Class Instance
# t~ ويتم استخدمها عندما تريد التعامل مع ال class مش ال Instance
# - Used When You Want To Do Something With The Class Itself
# >--------------------------------------------------------------------------
# B~ عند استخدام ال Static Methods
# @@ نستخدم ال Keyword التالي
# C% @staticmethod
# @@ def say_hello():
# Static Methods: => @staticmethod Keyword
# - It Takes No Parameters
# @@ لا تحتاج الي Parameters ويمكنك وضع اي عدد Parameters كما تشاء
# - Its Bound To The Class Not Instance
# @@ يتم استخدام نوع ال staticmethod لعمل شي معين يخص ال class بدون عمل access علي ال class ولا ال Object
# - Used When Doing Something Doesnt Have Access To Object Or Class But Related To Class
# -----------------------------------------------------------
# class Member:
#     not_allowed_names = ["Hell", "Shit", "Baloot"]
#     users_num = 0
# #! يتم عمل ال @classmethod بهذا الشكل وعند عملها بهذا الشكل تكون تخص ال class ليست تخص ال Instance
#     @classmethod
# #! وتاخذ class => ( cls ) Parameter مش زي ال Instance => ( self )
#     def show_users_count(cls):
#         print(f"We Have {cls.users_num} Users In Our System.")

#     @staticmethod
# #! هذه هي طريقه عمل ال staticMethod ومش شرط نحط فيها parameter زي ال self , cls دي براحتك
#     def say_hello():
#         print("Hello From Static Method")

#     def __init__(self, first_name, middle_name, last_name, gender):
#         self.fname = first_name
#         self.mname = middle_name
#         self.lname = last_name
#         self.gender = gender
#         Member.users_num += 1

#     def full_name(self):
#         if self.fname in Member.not_allowed_names:
#               raise ValueError("Name Not Allowed")

#         else:
#               return f"{self.fname} {self.mname} {self.lname}"

#     def name_with_title(self):
#         if self.gender == "Male":
#             return f"Hello Mr {self.fname}"

#         elif self.gender == "Female":
#              return f"Hello Miss {self.fname}"

#         else:
#              return f"Hello {self.fname}"

#     def get_all_info(self):
#         return f"{self.name_with_title()}, Your Full Name Is: {self.full_name()}"

#     def delete_user(self):
#         Member.users_num -= 1
#         return f"User {self.fname} Is Deleted."

# print(Member.users_num)

# member_one = Member("Osama", "Mohamed", "Elsayed", "Male")
# member_two = Member("Ahmed", "Ali", "Mahmoud", "Male")
# member_three = Member("Mona", "Ali", "Mahmoud", "Female")
# member_four = Member("Shit", "Hell", "Metal", "DD")

# print(Member.users_num)
# print(member_four.delete_user())
# print(Member.users_num)

# Member.show_users_count()

# Member.say_hello()
# ? -------------------------------------- 109 ------------------------------------------------------
# --------------------------------------------------
# -- Object Oriented Programming => Magic Methods --
# --------------------------------------------------
# @@ كل حاجه في البايثون عباره عن Object
# Everything in Python is An Object
# __init__  Called Automatically When Instantiating Class
#t~ ال __init__ بتتعمل بشكل Automatically عند عمل اي Class جديد
# self.__class__ The class to which a class instance belongs
# __str__   Gives a Human-Readable Output of the Object
# __len__   Returns the Length of the Container
# Called When We Use the Built-in len() Function on the Object
# ------------------------------------------------------
# class Skill:

#     def __init__(self):

#         self.skills = ["Html", "Css", "Js"]

#     def __str__(self):
# ! استخدمنا ال __str__ لعرض محتوي ال String الي موجود 

#         return f"This is My Skills => {self.skills}"

#     def __len__(self):

#         return len(self.skills)
    
# profile = Skill()

# # print(profile) #^^ With out __str__ > Output > <__main__.Skill object at 0x0000027DCD656A50>

# # print(profile) #^^ With __str__ > Output > This is My Skills => ['Html', 'Css', 'Js']
# print(profile.__str__()) #? او نستخدم هذه الطريقة 

#@@ عند استخدام هذه الطريقه كدا علشان نعرف ال instance دا بينتمي ل class اسمه ايه 
#! نستخدم __class__ لمعرفه profile دي تنتمي لانهي class
# print(profile.__class__) # <class '__main__.Skill'>

# print(Skill().skills) # كدا هيعرض محتوي ال skills > self.skills > ['Html', 'Css', 'Js']
# print(profile.skills) # كدا هيعرض محتوي ال skills > self.skills > ['Html', 'Css', 'Js']

# print(len(profile)) # بعد استخدام ال def __len__(self)
# print(profile.skills.__len__())

#@@ ممكن نضيف كمان عناصر علي العناصر بتاعتي بهذا الشكل 
# profile.skills.append("PHP")
# profile.skills.append("MySQL")
# print(len(profile))

# ss = "String"
#@@ عرض نفس القيم ولكن بشكل مختلف
# print(str.upper(ss))
# print(ss.upper())
#@@ عند استخدام هذه الطريقه كدا علشان نعرف ال instance دا بينتمي ل class اسمه ايه 
# print(ss.__class__)
# ? -------------------------------------- 110 ------------------------------------------------------
# ------------------------------------------------
# -- Object Oriented Programming => Inheritance #! الوراثه --
# ------------------------------------------------
# class Food:  # Base Class
#     def __init__(self, name, price):

#         self.name = name

#         self.price = price

#         print(f"{self.name} Is Created From Base Class And Price Is {self.price}")

#     def eat(self):

#         print("Eat Method From Base Class")

# # ! يمكننا وراثه class بداخل class ثاني من خلال (اسم ال class الذي سوف يتم الوراثه منه)
# # ! Name_class_2th(Name_class_1th)
# class Apple(Food):  # Derived Class

# #! * ال __init__ دي كدا عملت overwrite علي الي احنا ورثنها من فوق  *
# #@@ ويمكننا اضافه العناصر الذي نريد بيشكل عادي وطبيعي جدا زي amount كدا
#     def __init__(self, name, price, amount):

#     # ^^ (بشكل مبتتداء) لعمل وراثه للاشياء الذي بداخل ال Instance ذات نفسها الي هي القيم الذي تم صنعها
#         Food.__init__(self, name,price)  # Create Instance From Base Class

#         # t~ (بشكل متقدم) لعمل وراثه للاشياء الذي بداخل ال Instance ذات نفسها الي هي القيم الذي تم صنعها
#         super().__init__(name,price)

#     # t~ يتم عمل وراثه لل قيم الذي مثل هذه من خلال استخدام ال super()
#         self.amount = amount

#         print(f"{self.name} Is Created From Derived Class And Price Is {self.price} And Amount Is {self.amount}")

#     def get_from_tree(self):

#      print(f"Get From Tree From Derived Class Price => {self.price}")

# food_one = Food("Pizza",17)
# food_two = Apple("Pizza", 150, 500)
# food_two.eat()
# food_two.get_from_tree()
# ? -------------------------------------- 111 ------------------------------------------------------
# ---------------------------------------------------------
# -- Object Oriented Programming => Multiple Inheritance --
# ---------------------------------------------------------
# class BaseOne:
#     def __init__(self):
#         print("Base One")

#     def func_one(self):
#         print("One")

#     def Override(self):
#         print("You Override From BaseOne")
# class BaseTwo:
#     def __init__(self):
#         print("Base Two")

#     def func_two(self):
#         print("Two")

#     def Override(self):
#         print("You Override From BaseTwo")

# ^^ عند الوراثه من اكثر من مكان هذا يترتب علي حسب ترتبهم في الخانه
# class Derived(BaseOne, BaseTwo):
#     pass

# my_var = Derived()

# my_var.func_one()
# my_var.func_two()

# @@ هذه هو ال Multiple Inheritance ان يتم وراثه من اكثر من شخص عمل الوراثه من شخص اخر بمعني انك ترث خصائص الشخص الاول

#@@ بأختصار هذه طريقه ال Multiple Inheritance بشكل مختصر 
# class Base: #^^ الاب
#     pass
# class DerivedOne(Base): #^^ الابن
#     pass
# class DerivedTwo(DerivedOne): #^^ الحفيد
#     pass
# ! -------------- test
# class BaseOne:
#     def __init__(self):
#         print("__init__BaseOne")

#     def one(self):
#         print("BaseOne")

# class Basetwo:
#     def __init__(self):
#         print("__init__BaseTwo")

#     def two(self):
#         print("BaseTwo")

#? لوراثه اكثر من class يكون بهذه الطريقه 
#^^ وبيكون علي حسب ترتيب الوراثه يطبع لك ال __init__
# class Derived(BaseOne,Basetwo):
#     pass

# my_var = Derived()

#! لدينا Access علي كل عناصر الاثنين class بشكل طبيعي جدا 
# my_var.one()
# my_var.two()

# ^^ لمعرفه ترتيب الوراثه
# print(Derived.mro())
# ? -------------------------------------- 112 ------------------------------------------------------
# -------------------------------------------------
# -- Object Oriented Programming => Polymorphism #? تعداد الاوجه--
# @@ تعدد الاوجه ان يتم وراثه شي معين ويمكنك التحكم به ع حسب المكان الذي تستخدمه به
# -------------------------------------------------
# class A:

#   def do_something(self):

#     print("From Class A")

# # ^^ هنا عملنا هذا ال ERROR لكي لا تستخدم نفس ال output وتعدله علي حسب ماتريد في اي class ثاني
#     raise NotImplementedError("Derived Class Must Implement This Method")

# ^^ هنا تم عمل OverRide علي نفس اسم inctance من ال A
# class B(A):

#   def do_something(self):

#     print("From Class B")

# class C(A):

#   def do_something(self):

#     print("From Class C")

# my_instance = B()
# my_instance.do_something()
# my_instance1 = C()
# my_instance1.do_something()
# ? -------------------------------------- 113 ------------------------------------------------------
# --------------------------------------------------
# -- Object Oriented Programming => Encapsulation --
# --------------------------------------------------
# Encapsulation
# - Restrict Access To The Data Stored in Attirbutes and Methods
# Public
# ? يكون عباره عن استخدام العادي لل class يكون كل شي متاح ويمكننا التعديل علي عناصره
# - Every Attribute and Method That We Used So Far Is Public
# - Attributes and Methods Can Be Modified and Run From Everywhere
# - Inside Our Outside The Class
# Protected
# ? عباره عن Attributes and Methods يمكنك الدخول عليهم من خلال ال class و ال class الذي يرث الخصائص
# - Attributes and Methods Can Be Accessed From Within The Class And Sub Classes
#@@ للدخول علي هذا العنصر نستخدم قبله _Varname
# - Attributes and Methods Prefixed With One Underscore _
# ? يمكنك الدخول اليها من خلال ال class , Object فقط
# Private
# - Attributes and Methods Can Be Accessed From Within The Class Or Object Only
# @@ لايمكن عمل Modified بره ال class
# - Attributes Cannot Be Modified From Outside The Class
# - Attributes and Methods Prefixed With Two Underscores __
# ---------------------------------------------------------
# - Attributes = Variables = Properties
# -------------------------------------
# class Member:
#   def __init__(self, name):

#^^ وهذا شكل ال Public الطبيعي الذي نعرفه
#     self.name = name  # Public

# one = Member("Ahmed")
# print(one.name)

#? بهذه الطريقه يمكننا التعديل علي متغير بداخل ال class الاب
# one.name = "Sayed"
# print(one.name)
# ! -----Two
# class MemberTwo:
#   def __init__(self, name):
# ^^ هذا يكون شكل ال Attributes ال Protected يكون قبلها _ (_name)
#     self._name = name  # Protected

# one = MemberTwo("Ahmed")
# print(one._name)
# one._name = "Sayed"
# print(one._name)

# ! -----Three
# class Member:
#   def __init__(self, name):
# ^^ هذا يكون شكل ال Attributes ال Private يكون قبلها __ (__name)
    # self.__name = name  # Private

#   def say_hello(self):
    # return f"Hello {self.__name}"

# one = Member("Ahmed")
# print(one.say_hello())

# @@ يمكننا عمل Access علي ال Private بهذا الشكل
# print(one._Member__name)
# ? -------------------------------------- 114 ------------------------------------------------------
# ------------------------------------------------------
# -- Object Oriented Programming => Getters & Setters --
# ------------------------------------------------------
# class Member:

#     def __init__(self, name):

#         self.__name = name  # Private

#     def say_hello(self):

#         return f"Hello {self.__name}"

# @@ هذه طريقه الصحيحه لعمل Getter للبيانات ال Private
    # def get_name(self):  # Getter

    #     return self.__name

# @@ هذه طريقه الصحيحه لعمل Setters للبيانات ال Private ان تعدل عليها
#     def set_name(self, new_name):  # Setters

#         self.__name = new_name

# one = Member("Ahmed")

# t~ هذه طريقه غير سليمه للتعامل مع البيانات ال Private
# one._Member__name = "Sayed"
# print(one._Member__name)

#^^ هذه هي الطريقه السليمه لتعديل علي العناصر
# print(one.get_name())
# one.set_name('Abbas')
# print(one.get_name())
# ? -------------------------------------- 115 ------------------------------------------------------
# --------------------------------------------------------
# -- Object Oriented Programming => @Property Decorator --
# --------------------------------------------------------
# class Member:

#     def __init__(self, name, age):

#         self.name = name

#         self.age = age

#     def say_hello(self):

#         return f"Hello {self.name}"

# # ! لتحويل ال Object نستخدم @property قبل ال Object بهذا الشكل لكي يمكننا المناده عليها بشكل عادي
#     @property
#     def age_in_days(self):

#         return self.age * 365

# one = Member("Ahmed", 40)

# print(one.name)
# print(one.age)

#^^ لاستخدام هذه الطريقه لازم نشيل ال @property
# print(one.say_hello())
# print(one.age_in_days())

#t~ لاستخدام هذه الطريقه لازم نعمل @property قبل ال function
# print(one.age_in_days)
# ? -------------------------------------- 116 ------------------------------------------------------
# ----------------------------------------------------------------
# -- Object Oriented Programming => ABCs => Abstract Base Class --
# ----------------------------------------------------------------
# - Class Called Abstract Class If it Has One or More Abstract Methods
# @@ يتسخدم لعمل بنيه لشي معين ولكن لاتنطبق عليه نفسه وتنطبق علي الذي يرثها منه
# - abc module in Python Provides Infrastructure for Defining Custom Abstract Base Classes.
# - By Adding @absttractmethod Decorator on The Methods
# - ABCMeta Class Is a Metaclass Used For Defining Abstract Base Class
# --------------------------------------------------------------------
# @@ نستعدي من ال abc النوعين دول لكي يتم تفعلهم
# from abc import ABCMeta, abstractmethod

#! تستخدم ال ABCMeta بهذا الشكل
# class Programming(metaclass=ABCMeta):

#! تستخدم ال @abstractmethod بهذا الشكل
#   @abstractmethod
#   def has_oop(self):

#     pass

#! عند عمل اكثر من @abstractmethod لازم نعملهم كلهم في باقي ال class الي بيرث الحاجه دي
#   @abstractmethod
#   def has_name(self):

#     pass

# class Python(Programming):

#   def has_oop(self):

#     return "Yes From Python"

#   def has_name(self):

#     return "Printed From Python"

# class Pascal(Programming):

#   def has_oop(self):

#     return "No From Pascal"

#   def has_name(self):

#     return "Printed From Pascal"

# one = Python()
# two = Pascal()

# print(one.has_oop())
# print(one.has_name())
# print(two.has_oop())
# print(two.has_name())
# ? -------------------------------------- 117 ------------------------------------------------------
# ------------------------
# -- Databases => Intro --
# ------------------------
# - Database Is A Place Where We Can Store Data
#@@ هي عباره عن قاعده بيانات بتخزن فيها البيانات بتاعتك
# - Database Organized Into Tables (Users, Categories)
#@@ والبيانات دي بتكون منظمه علي هياء جداول
# - Tables Has Columns (ID, Username, Password)
#@@ الجداول تنقسم الي اعمده كل عمود عباره عن بعض البيانات
# - There's Many Types Of Databases (MongoDB, MySQL, SQLite)
# ال python بيتعامل مع MongoDB, MySQL, SQLite
# - SQL => Structured Query Language
# - SQLite => Can Run in Memory or in A Single File
# - You Can Browse File With https://sqlitebrowser.org/
# Download => https://sqlitebrowser.org/dl/
# - Data Inside Database Has Types (Text, Integer, Date)
# ------------------------------------------------------
# ? -------------------------------------- 118 ------------------------------------------------------
# --------------------------------------------------------
# -- Databases => SQLite => Create Database And Connect --
# --------------------------------------------------------
# - Connect
# - Execute
# - Close
# --------------------------------------------------
# @@ نستدعي ال SQLite من خلال ال import sqlite3
# import sqlite3

# @@ يتم انشاء ال DB من خلال sqlite3.connect("Name File.db") > Create Database And Connect
# db = sqlite3.connect(r"E:\HACKING\Python\SQLITE\Coding\app.db")

# @@ لعمل ال DB نستخدم اسم ال متغير الذي تم عمله ثم نستخدم كلمه execute > Create The Tables and Fields
# ^^ وعند كتابه البيانات نكتب create table is not exists ثم اسم ملف البيانات نستخدم هذه الطريقه علشان لو شكك الجدول دا موجود قبل كدا
# ^^ وبداخل ال (البيانات ذات نفسها)
# db.execute("create table if not exists skills (name text, progress integer, user_id integer)")
#! بستخدم الطريقه دي لو الجدول الي هعمله مش موجود قبل كدا 
# db.execute("create table skills (name text, progress integer, user_id integer)")

# t~ لغلق الملف بعد الانتهاء > Close Database
# db.close()
# ? -------------------------------------- 119 ------------------------------------------------------
# ------------------------------------------------------
# -- Databases => SQLite => Insert Data Into Database --
# ------------------------------------------------------
# - cursor => All Operation in SQL Done By Cursor Not The Connection Itself
# - commit => Save All Changes
# ------------------------------------------------------
# import sqlite3 

# db = sqlite3.connect(r"E:\HACKING\Python\SQLITE\Coding\app.db")

# ! نستخدم ال cursor لوضع مؤسر الماوس في مكان معين وهذه هو الاعتماد الكلي للاستخدام
# cr = db.cursor()

#? بهذه الطريقه عملنا جودل باسم users
# cr.execute("create table if not exists users (user_id integer , name text)")

# t~ هذا شكل يدائي لعمل البيانات طبعا يمكننا عمل LooP بشكل عادي كما سوف نفعل
# ^^ Inserting Data نضع البيانات بداخل ال DB بهذا الشكل
# cr.execute("insert into users(user_id, name) values(1, 'Ahmed')")
# cr.execute("insert into users(user_id, name) values(2, 'Sayed')")
# cr.execute("insert into users(user_id, name) values(3, 'Osama')")

# my_list = ["Ahmed", "Sayed", "Mahmoud", "Ali", "Kamel", "Ibrahim", "Enas"]
# for key,value in enumerate(my_list,1):
    # cr.execute(f"insert into users(user_id, name) values({key}, '{value}')")

#! نستخدم ال commit لحفظ البيانات الذي تم وضعها وهذه اهم خطوه لتنفيذ ما تم عمله
# db.commit()

# db.close()
# ? -------------------------------------- 120 ------------------------------------------------------
# --------------------------------------------------------
# -- Databases => SQLite => Retrieve Data From Database --
# --------------------------------------------------------
# - fetchone => returns a single record or None if no more rows are available.
#@@ هو عباره عن عنصر واحد فقط 
# - fetchall => fetches all the rows of a query result. It returns all the rows
# as a list of tuples. An empty list is returned if there is no record to fetch.
#@@ هو عباره عن كل العناصر 
# - fetchmany(size) =>
# ------------------------------------------------------
# import sqlite3 

# db = sqlite3.connect(r"E:\HACKING\Python\SQLITE\Coding\app.db")

# cr = db.cursor()

# cr.execute("create table if not exists users (user_id integer , name text)")

# cr.execute("insert into users(user_id, name) values(1, 'Ahmed')")
# cr.execute("insert into users(user_id, name) values(2, 'Sayed')")
# cr.execute("insert into users(user_id, name) values(3, 'Osama')")
# cr.execute("insert into users(user_id, name) values(4, 'Ali')")

# cr.execute("select * from users")

#@@ لعرض عنصر واحد فقط 
# print(cr.fetchone())

#@@ لعرض جميع العناصر بداخل list وكل صف بداخل Tuple
# print(cr.fetchall())

#@@ تستخدم لعرض عدد معين من الصفوف علي حسب انت محدد كام صف 
# print(cr.fetchmany(2))

# db.commit()

# db.close()

# ? -------------------------------------- 121 ------------------------------------------------------
# ---------------------------------------------------
# -- Databases => SQLite => Training On Everything --
# ---------------------------------------------------
# import sqlite3
# def get_all_data():
#     try:
#         db = sqlite3.connect(r"E:\HACKING\Python\SQLITE\Coding\app.db")

#         print("Connected To Database Successfully")

#         cr = db.cursor()

#         cr.execute("select * from users")

#         results = cr.fetchall()

#         print(f"DataBase Has {len(results)} Rows.")

#         print("Showing Data: ")

#         for key, row in results:
#             print(f"User_ID => {key}, Username => {row}")

# #@@ تم استخدم هنا كلمه as لعمل اختصار لاسم sqlite3.Error وتم تغيره الي SE
#     except sqlite3.Error as SE:

#         print(f"Error Reading Data {SE}")

#     finally:

#         if(db):

#             db.close()

#             print("Connection To Database Is Closed")

# get_all_data()
# ? -------------------------------------- 122 ------------------------------------------------------
# ----------------------------------------------
# -- Databases => SQLite => Update and Delete --
# ----------------------------------------------
# import sqlite3

# db = sqlite3.connect(r"E:\HACKING\Python\SQLITE\Coding\app.db")

# cr = db.cursor()

#? لعمل update علي حسب ال id بتاع المستخدم يكون بهذه الطريقه 
# Update Data
# ^^ لعمل تحديث للبيانات من شي الي اخري
# ^^ update users set اسم ال table = ثم القيمه الجديده لل لعنصر الاول او علي حسب العنصر الذي تريد تحديثه
# ^^ ونستخدم كلمه where ثم اسم ال user_id ونضع بجانبه رقمه لكي تغير شخص او علي حسب طلبك
# cr.execute("update users set name = 'Mahmoud' where user_id = 1")
# cr.execute("update users set name = 'Glal' where user_id = 2")
# cr.execute("update users set name = 'Ameer' where user_id = 3")
# cr.execute("update users set name = 'Hany' where user_id = 4")

# Delete Data
# ^^ لحذف قيمه معينه من خلال ال user_id بيتم كتابتها بهذا الشكل
# num_int = int(input("Write User_id > "))
# cr.execute(f"delete from users where user_id = {num_int}")

#! Delete All Data 
# cr.execute("delete from users")

# cr.execute("select * from users")

# for i,d in cr.fetchall():
#     print(f"{i} => {d}")

# db.commit()

# db.close()
# ? -------------------------------------- 123_124_125_126 ---------------------------------------------------
# -----------------------------------------------------
# -- Databases => SQLite => Create Skills App Part 1 - 4 --
# -----------------------------------------------------
# import sqlite3

# db = sqlite3.connect(r"E:\HACKING\Python\SQLITE\Coding\app.db")

# cr = db.cursor()

# def commit_close():
#     """Commit Changes And Close Connection To DataBase .."""
#     db.commit() # Save (Commit) Changes
#     db.close() # Close DataBase File ..
#     print("Connection To DataBase Is Closed.")

# input_message = """What Do You Want To Do ?
# "s" => Show All Skills
# "a" => Add New Skill
# "d" => Delete A Skill
# "u" => Update Skill Progress
# "q" => Quit The App
# Choose Option : """
# user_input = input(input_message).strip().lower()  # Input Option Choose

# commands_list = ["s", "a", "d", "u", "q"]  # Command List

# def show_skills():
#     cr.execute(f"select * from skills where user_id ={uid}")
#     results = cr.fetchall()
#     print(f"Your Have {len(results)} Skills.")

#     if len(results) > 0 :
#         print("Showing Skills With Progress: ")

#         for row,prog,ids in results :
#             print(f"Skills => {row}, Progress => {prog} %, ID => {ids}")
#     else :
#         print(f"Go To Append New Skill")

#     commit_close()

# def add_skill():
#     sn = input("WRite Skill Name: ").strip().capitalize()
#     cr.execute(f"select name from skills where name ='{sn}' and user_id ='{uid}'")
#     results = cr.fetchone()

#     if results == None:
#         prog = input("WRite SKill Progress: ").strip()
#         cr.execute(
#             f"insert into skills(name,progress,user_id) values('{sn}','{prog}','{uid}')")  # Theres No Skill With This Name In Database
#         print(f"Your Skill Name => {sn} and Progress => {prog}")

#     else:# Theres A Skill With This Name in Database
#         print("You Can't Add This Skill Beacuse This SKill in DB.")
#         option = input("if Need To Update You Progress WRite (y) Or (n) To Close: ")
        
#         if option == "y":
#              new_prog = input("WRite The New Skill Progress: ").strip()
#              cr.execute(f"update skills set progress ='{new_prog}' where name ='{sn}' and user_id ='{uid}'")
#              print(f"Your Skill Name => {sn} and New Progress => {new_prog}%")
#         else:
#             print("Sorry Try Again .. :-)")
#     commit_close()

# def del_skill():
#     sk = input("Write Skill Name > ").strip().capitalize()
#     cr.execute(f"delete from skills where name = '{sk}' and user_id ='{uid}' ")
#     print(f"Your Skill Id {uid} Succsessfully Deleted..")
#     commit_close()

# def update_skill():
#     sk = input("Write Skill Name > ").strip().capitalize()
#     new_prog = input("WRite The New SKill Progress: ").strip()
#     cr.execute(f"update skills set progress ='{new_prog}' where name ='{sk}' and user_id ='{uid}'")
#     print(f"Your Skill Name => {sk} and New Progress => {new_prog}")
#     commit_close()

# if user_input in commands_list:
#     print(f"Command Found {user_input}")
#     uid = int(input("Write Y0ur ID > "))

#     if user_input == 's':
#         show_skills()

#     elif user_input == 'a':
#         add_skill()

#     elif user_input == 'd':
#         del_skill()

#     elif user_input == 'u':
#         update_skill()

#     else :
#         print("App Is Closed.")
#         commit_close()
# else:
#     print(f"Sorry This Command \"{user_input}\" Is Not Found")
# ? -------------------------------------- 127 ------------------------------------------------------
# --------------------------------------------------------
# -- Databases => SQLite => Very Important Informations --
# --------------------------------------------------------
# import sqlite3

# db = sqlite3.connect(r"E:\HACKING\Python\SQLITE\Coding\last.db")
# # 
# cr = db.cursor()
#@@ make a Table skills
# cr.execute("create table if not exists skills (skill text , progress integer , user_id integer)")

#@@ هذا بالظبط نفس شكل الي تحت
# cr.execute("insert into skills(name,progress,user_id) values('JS',65,2)")


# Inserting Data
# ^^ بعض اوامر ال ((SQL)) الذي سوف تفيدنا في الحياه العمليه

# my_tuple = ('mysql', 80, 1)
# cr.execute("insert into skills values('Pascal', '65', 4)")
#! لمنع ال SQL Injection نستخدم هذا الشكل من وضع البيانات
# نضع مكان ال values ثلاث علامات استفهام (?,?,?) ثم ال values الذي تريد وضعها
# cr.execute("insert into skills values(?, ?, ?)",('Asoum', '65', 4))
# cr.execute("insert into skills values(?, ?, ?)", my_tuple)
# Fetch Data From Database
# @@ نستخدم كلمه order by لترتيب العناصر علي حسب ماتريد ونستخدم وللترتيب التصادعي نستخدم asc
# cr.execute("select * from skills order by user_id asc")

# @@ وللترتيب التصادعي نستخدم desc
# cr.execute("select * from skills order by user_id desc")

# @@ لتحديد العناصر الذي تريد ان تظهر لك نستخدم كلمه limit ثم العدد
# cr.execute("select * from skills order by skill limit 2")

# @@ نستخدم offset ثم الرقم الذي تريد ان يبداء بعده اركن 2
# cr.execute("select * from skills order by skill limit 4 offset 2 ")

# @@ ان يبداء طباعه الارقام الذي اكبر او اصغر من الذي تريد وضعه
# cr.execute("select * from skills where user_id >= 2")
# cr.execute("select * from skills where user_id > 1 ")

# @@ يمكننا استخدم ال no in ++ ,و ال in هنا بشكل عادي جدا ايضا
# ? هنا تقول له اذا كان ال id بداخل ال tuple الي قدامك دي اطبعهم in(from,to)
# cr.execute("select * from skills where user_id in(1, 4)")

# ? هنا تقول له اذا كان ال id ليس بداخل ال tuple الي قدامك دي اطبعهم not in(from,to)
# cr.execute("select * from skills where user_id not in(1, 2, 3)")

# cr.execute("select * from skills where user_id not in(2,4) ")


# results = cr.fetchall()

# for row,prog,ids in results :
#     print(f"Skills => {row}, Progress => {prog} %, ID => {ids}")

# db.commit()

# db.close()
# ? -------------------------------------- 128 ------------------------------------------------------
# -------------------------------------------------
# -- Advanced_Lessons => __name__ And "__main__" --
# -------------------------------------------------
# ! هنا عند استخدام ال __name__ بداخل الملف الاساسي يعني انه هو ال __main__
# ! لو تم استدعاء الملف من خلال ال import هنا لم يكن نوعه __main__ لانه تم استدعاء
# if __name__ == "__main__":
# - __name__ => Built In Variable
# - "__main__" => Value Of The __name__ Variable
# Executions Methods
# - Directly => Execute the Python File Using the Command Line.
#^^ Directly > يعني الملف دا هو الاساسي الي هتشغل منه البرنامج
# - From Import => Import The Code From File To Another File
#^^ From Import > يعني انك بتستدعي الملف دا من ملف تاني فا هو كدا مش __main__
# -------------------------------------------------------------
# In Some Cases You Want To Know If You Are Using A Module Method As Import
# Or You Use The Original Python File
# -------------------------------------------------------------------------
# In Direct Mode Python Assign A Value "__main__"
# To The Built In Variable __name__ in The Background
# ---------------------------------------------------
# print(type(__name__))  # ^^ Output => <class 'str'>

# if __name__ == "__main__" : 
#     print("Welcome from __main__ File") # ^^ Output => Welcome from __main__ File
# else :
#     print("Welcome from Imported File")
#     print(f"Your File Name Is {__name__}")
# ? -------------------------------------- 129 ------------------------------------------------------
# ------------------------------------------------ 
# t~ يتم استخدام هذا الشكل بشكل Advanced لقياس الوقت الذي تم انهاء في الكود الخاص بك
# -- Advanced_Lessons => Timing Your Code With Timeit --
# ------------------------------------------------------
# - timeit: - Get Execution Time Of Code By Running 1M Time And Give You Minimal Time
# -         - It Used For Performance By Testing All Functionality
# - timeit(stmt, setup, timer, number)
# - timeit(pass, pass, default, 1.000.000) Default Values
# -------------------------------------------------------
# -------------------------------------------------------
# ^^ stmt = الكود الذي تريد ان تحسب الوقت بتاعه
# - stmt: Code You Want To Measure The Execution Time
# ^^ setup = عمل شي معين مثال import Module او اشي شي علي حسب الفكره
# - setup: Setup Done Before The Code Execution (Import Module Or Anything)
# ^^ timer = وقت الشي الذي سوف يحدث
# - timer: The Timer Value
# ^^ number = عدد الشي الذي سوف يتم تنفيذه
# - number: How Many Execution That Will Run
# -------------------------------------------------------
# import timeit

# print(dir(timeit))

# print(timeit.timeit("'ntfsx00' * 1000")) #@@ الشكل الطبيعي لقياس الوقت للكود 

# print(timeit.timeit("name = 'ntfsx00'; name * 1000")) #! ; لكتابه اكثر من سطر نستحدم الفاصله المنقوطه

#? نستخدم ال stmt لكتابه الكود الذي نريد حساب الوقت بتاعه ثم setup لعمل import للحاجه الذي نريد استخدامها في ال stmt
# print(timeit.timeit(stmt="random.randint(0, 50)", setup="import random")) 

#@@ هنا بنحسب الوقت الذي تم انهاء فيه الكود بتاعنا
# print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))

#@@ لستدعاء random لازم نعمل import random في ال setup وحطينا number=1.000.000 يعني هيعملها مليون مره
# print(timeit.timeit('random.random()', setup='import random', number=1000000))

#@@ لو عايز تعرف الوقت في اكتر من مره تستخدم ال repeat بدل ال timeit
#@@ هنا هيعملها 4 مرات ويطبع الوقت في كل مره
# print(timeit.repeat(stmt="random.randint(0, 50)", setup="import random", repeat=4))
# ? -------------------------------------- 130 ------------------------------------------------------
# -------------------------------------------------
#! (explorer .) نستخدمها لفتح الملف الذي نحن به في ال command Line
# --------------------------------------------------
# -- Advanced_Lessons => Add Logging To Your Code --
# --------------------------------------------------
# - Print Out To Console Or File
# - Print Logs Of What Happens
# ------------------------------
# ^^ انواع ال ERROR الذي يمكنك ان تتبعها
# - DEBUG
# - INFO
# - WARNING
# - ERROR
# - CRITICAL
# ----------
# name => Logging Module Give It To The Default Logger. ( root )
# -----------------------------------------------------
# Basic Config
# @@ filename = اسم الملف بالاكستينشن بتاعه.log >>> my_logging.log
# - filename => File Name and Extension
# @@ filemode = نوع ال mode بتاع الملف اذا كان ('a',,'r',,'w') الافضل بتكون استخدام ال 'a' لان بيتم كتابه الرساله بعد الرساله القديمه وهكذا علي حسب الفكره
# - filemode => Mode Of The File a => Append
# @@ format = الرساله الذي تريد ان تظهر لك
# - format => Format For The Log Message
# @@ levelname = اسم ال ERROR المستخدم
# - levelname => Level of Severity
# @@ datefmt = نوع كتابه ال Data وهذا من خلال درس الوقت الذي اخدنا
# - datefmt => Type Date
# ------------------------
# ^^ تستخدم لاسترجاع لك اسم ال logger الي هو ال RooT ويمكننا تغيره بشكل عادي جدا
# getLogger => Return a Logger With the Specified Name
# ------------------------
# @@ %(asctime)s => ليطبع كل الوقت الذي حدث به ال ERROR وطبعا يتم استخدامها بهذا الشكل  %(..)s
# @@ %(name)s => اسم ال root وعلي حسب ما تريد تغيره
# @@ %(levelname)s => اسم ال ERROR المستخدم
# @@ %(message)s => الرساله الذي بداخل ال ERROR
# @@ %(filename)s => اسم الملف الذي سوف يتم تسجيل في ال log -- my_logging.log
# ? ------------------------
# import logging

# print(dir(logging))

# logging.basicConfig(filename="my_logging.log",filemode="a",format="Date => ( %(asctime)s ) LoggerUser => %(name)s - ErrorName => %(levelname)s - Message => %(message)s",datefmt="%m-%d-%Y %I:%M:%S")
# ! ----------------- TRYY
# logging.basicConfig(filename="my_logging.log",filemode="a",format="Date => ( %(asctime)s ) LoggerUser => %(name)s - ErrorName => %(levelname)s - Message => %(message)s",datefmt="%m-%d-%Y %I:%M:%S")

# my_logger = logging.getLogger("ManualName")

# my_logger.critical("Critical Error")
# my_logger.error("Error Message")
# my_logger.warning("Warning Message") 
# ! ----------------- TRYY with input
# name_loger = input("Wreite UserName Loger : ")

# logging.basicConfig(filename="my_logging.log",filemode="a",format=f"Date => ( %(asctime)s ) LoggerUser => {name_loger} - ErrorName => %(levelname)s - Message => %(message)s",datefmt="%m-%d-%Y %I:%M:%S")

# my_logger = logging.getLogger(name_loger)

# my_logger.critical("Critical Error")
# my_logger.error("Error Message")
# my_logger.warning("Warning Message") 
# ! ----------------- TRYY
# logging.basicConfig(filename="my_logging.log",filemode="a",format="Date => ( %(asctime)s ) LoggerUser => %(name)s - ErrorName => %(levelname)s - Message => %(message)s",datefmt="%m-%d-%Y %I:%M:%S")

# name_loger = input("Wreite UserName Loger : ")

# my_logger = logging.getLogger(name_loger)

# my_logger.critical("Critical Error")
# my_logger.error("Error Message")
# my_logger.warning("Warning Message") 

# ? -------------------------------------- 131 ------------------------------------------------------
# ----------------------------------------------------
# -- Advanced_Lessons => Unit Testing With Unittest --
# P# اختبار وحدات الكود بتاعك من خلال ال unittest
# ^^ هو نوع معين من البيانات الذي انتظره يمعني ان يتم عمل test لكل الاكواد الذي لدينا وننتظر قيمه معينه
# ----------------------------------------------------
# Test Runner
# C% انواع Module الذي تستخدم لعمل ال Test هي => (unittest, pytest)
# - The Module That Run The Unit Testing (unittest, pytest)
# ---------------------------------------------------------
# Test Case
# @@ اقل وحدات في ال test هي test Case
# - Smallest Unit Of Testing
# @@ نستخدم Methods ال Asserts لمعرفه الشي الذي سوف يسترجع من خلال ال test Case
# - It Use Asserts Methods To Check For Actions And Responses
# Test Suitea
# @@ ال Test Suitea هي مجموعه من ال Test Cases مع بعض بمعني انه كذا مجموعه من ال Test Cases
# - Collection Of Multiple Tests Or Test Cases
# Test Report
# @@ ال Test Report هي نتيجه ال Test الذي حدث
# - A Full Report Contains The Failure Or Succeed
# -------------------------------------------------------

# @@ نستخدم ال assert ثم الكود الذي تريد التجريه عليه والبيانات الذي تنتظرها منه ثم رساله اذا لم تطلع النتيجه صحيحه
# assert الكود == الاخراج, "الرساله لو الكود خطاء"0
# assert 3 * 8 == 22, "Should Be 24"

# ! AssertionError: Equal 10 Is True .. 
# assert 5 + 5 == 11, "Equal 10 Is True .. "

#t~ تجربه بسيطه علي ال assert
# def test_case_one():
    
#     assert 5 * 10 == 50, "Should Be 50"

# def test_case_two():

#     assert 5 * 50 == 250, "Should Be 250"

# if __name__ =="__main__":
  
#   test_case_one()
#   test_case_two()

#   print("All Tests Passed")

# ^^---------------------------------------
# import unittest

# class MyTestCase(unittest.TestCase):
#     def test_case_one(self):
#         #@@ assertTrue > هل الشرط صحيح
#         self.assertTrue(100 < 101 , "100 Is Greater Than 97")

#     def test_case_two(self):
#         #@@ assertEqual > هل الاول يساوي التاني
#         self.assertEqual("ntfsx00".upper(), "NTFSX00", "Should Be Upper Case")

#     def test_case_three(self):
#         #@@ assertGreater > هل الرقم الاول اكبر من التاني
#         self.assertGreater(50, 20, "50 Is Greater Than 20")

#     def test_case_four(self):
#         #@@ assertFalse > هل الشرط خطاء
#         self.assertFalse(5 != 5, "Should Be False")

#     def test_case_five(self):
#         #@@ assertIn > هل العنصر موجود في التاني
#         self.assertIn("Hello", "Hello World", "'Hello' Is Found In 'Hello World'")

#     def test_case_six(self):
#         #@@ assertIsInstance > هل العنصر من نفس النوع
#         self.assertIsInstance(100, int, "100 Is An Integer")

#     def test_case_seven(self):
#         #@@ assertNotEqual > هل الاول لا يساوي التاني
#         self.assertNotEqual(10 + 5, 20, "10 + 5 Is Not Equal 20")

#         #@@ وفي حاجات كثيرة جدا تقدر تستخدمها في ال unittest ممكن تشوفها في التوثيق بتاع ال unittest > https://docs.python.org/3/library/unittest.html
        
# if __name__ == "__main__":
#     #^^ unittest.main() > دي معنها ان يتم تشغيل كل ال test Case الي جوه ال MyTestCase
#     unittest.main()
# ? -------------------------------------- 132 ------------------------------------------------------
# --------------------------------------------------------
# -- Advanced_Lessons => Generate Random Serial Numbers --
# ^^ فكره عمل ال Serial Numbers بشكل عشوائي
# --------------------------------------------------------
# نستخدم import لل string بداخلها الحروف الكبيره والصغيره وجميع الارقام

# import string
# import random

# print(string.punctuation)  #@@ طباعة جميع علامات الترقيم
# print(string.digits)  # @@ طباعة جميع الارقام من 0 الي 9
# print(string.ascii_uppercase)  # @@ طباعة جميع الحروف الكبيره
# print(string.ascii_lowercase)  # @@ طباعة جميع الحروف الصغيره
# print(string.ascii_letters)  # @@ طباعة جميع الحروف الكبيره والصغيره
# print(string.printable)  # @@ طباعة جميع الحروف والارقام وعلامات الترقيم
# print(string.hexdigits)  # @@ طباعة جميع الحروف والارقام المستخدمه في ال Hexadecimal

# def serial(count):
#     all_chars = string.ascii_letters + string.digits 
#     chars_count = len(all_chars)
#     serial_list = []

#     while count > 0 :
#         random_number = random.randint(0,chars_count - 1 )
#         random_char = all_chars[random_number]
#         serial_list.append(random_char)
#         count -=1

#     return "".join(serial_list)
# serial_number = serial(30)
# print(f"Your Serial Number Is : {serial_number}")
# !----------------- Two Way To get Random Serial
# def serial(count):
#     all_chars = string.ascii_letters + string.digits
#     chars_count = len(all_chars)
#     serial_list = []

#     for _ in range(count):
#         serial_list.append(all_chars[random.randint(0, chars_count - 1)])
        
#     return "".join(serial_list)
#     # ^^ هنا بنستخدم ال join علشان نحول الليست الي سترينج عادي

# serial_number = serial(30)
# print(f"Your Serial Number Is : {serial_number}")
