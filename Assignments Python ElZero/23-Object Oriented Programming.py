
# t~ >>>>                                                 Assignments  103 ==> 116                                            <<<<<
# ? --------------------------------- 1  -------------------------
# class Game:
#     def __init__(self,name,developer,year,price):
#         self.name = name
#         self.developer = developer
#         self.year = year
#         self.price = price

#     def price_in_pounds(self):
#         return self.price * 15.6

# game_one = Game("Ys", "Falcom", 2010, 50)

# print(f"Game Name Is \"{game_one.name}\", ", end="")
# print(f"Developer Is \"{game_one.developer}\", ", end="")
# print(f"Release Date Is \"{game_one.year}\", ", end="")
# print(f"Price In Egypt Is {game_one.price_in_pounds()}", end="")
# ! ----------SOme Way (AI)
# class Game:
#     def __init__(self, name, developer, year, price_in_dollars):
#         self.name = name
#         self.developer = developer
#         self.year = year
#         self.price_in_dollars = price_in_dollars

#     def price_in_pounds(self):
#         exchange_rate = 15.6

#         price_egp = self.price_in_dollars * exchange_rate

#         return f"{price_egp:.1f} Egyptian Pounds"
    
# game_one = Game("Ys", "Falcom", 2010, 50)

# print(f"Game Name Is \"{game_one.name}\", ", end="")
# print(f"Developer Is \"{game_one.developer}\", ", end="")
# print(f"Release Date Is \"{game_one.year}\", ", end="")
# print(f"Price In Egypt Is {game_one.price_in_pounds()}", end="")
# ? --------------------------------- 2  -------------------------
# class User:
#     def __init__(self,fname,lname,age,gender):
#         self.fname = fname
#         self.lname = lname
#         self.age = age
#         self.gender = gender

#     def full_details(self):
#         if self.gender == "Male":
#             return f"Hello Mr {self.fname} {self.lname:.1s}. [{str(40 - self.age).zfill(2)}] Years To Reach 40"
        
#         elif self.gender == "Female":
#             return f"Hello Mrs {self.fname} {self.lname:.1s}. [{str(40 - self.age).zfill(2)}] Years To Reach 40"
        
#         else : 
#             return f"Hello {self.fname} We Cont Find Your Gender \"{self.gender}\" .."
        
# user_one = User("Osama", "Mohamed", 38, "Male")
# user_two = User("Eman", "Omar", 25, "Female")
# user_three = User("Eman", "Omar", 25, "Other")

# print(user_one.full_details()) # Hello Mr Osama M. [02] Years To Reach 40
# print(user_two.full_details()) # Hello Mrs Eman O. [15] Years To Reach 40
# print(user_three.full_details()) # Hello Eman We Cont Find Your Gender "Other" ..
# ! ----------SOme Way (AI)
# class User:
#     def __init__(self, first_name, last_name, age, gender):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.gender = gender

#     def full_details(self):
#         title = "Mr" if self.gender == "Male" else "Mrs"
        
#         last_initial = self.last_name[0]
        
#         years_left = f"{40 - self.age:02}"
        
#         return f"Hello {title} {self.first_name} {last_initial}. [{years_left}] Years To Reach 40"
    
# user_one = User("Osama", "Mohamed", 38, "Male")
# user_two = User("Eman", "Omar", 25, "Female")

# print(user_one.full_details()) # Hello Mr Osama M. [02] Years To Reach 40
# print(user_two.full_details()) # Hello Mrs Eman O. [15] Years To Reach 40
# ? --------------------------------- 3  -------------------------
# class Message:
#     def print_message():
#         return "Hello From Class Message"

# print(Message.print_message())
# ! -------Some Way (AI)
# class Message:
#     @staticmethod
#     def print_message():
#         return "Hello From Class Message"

# print(Message.print_message())
# ! -------Some Way
# class Message:

#   @classmethod
#   def print_message(cls):
#     return "Hello From Class Message"

# print(Message.print_message())
# ? --------------------------------- 4  -------------------------
# class Games:
#     def __init__(self,num_game):
#         self.num_game = num_game

#     def show_games(self):
#         if type(self.num_game) == list :
#             print("I Have Many Games: ")

#             for i in self.num_game :
#                 print(f" -- {i}")

#         elif type(self.num_game) == int :
#             print(f"I Have {self.num_game} Game.")

#         else :
#             print(f"I Have One Game Called \"{self.num_game}\"")

# my_game = Games("Shadow Of Mordor")
# my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
# my_games_count = Games(80)

# my_game.show_games()

# my_games_names.show_games()

# my_games_count.show_games()
# ! ---------- Some Way (AI)
# class Games:
#     def __init__(self, data):
#         self.data = data

#     def show_games(self):

#         if isinstance(self.data, str):
#             print(f'I Have One Game Called "{self.data}"')
            
#         elif isinstance(self.data, list):
#             print("I Have Many Games:")
#             for game in self.data:
#                 print(f"-- {game}")
                
#         elif isinstance(self.data, int):
#             print(f"I Have {self.data} Game.")

# my_game = Games("Shadow Of Mordor")
# my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
# my_games_count = Games(80)

# my_game.show_games()

# my_games_names.show_games()

# my_games_count.show_games()
# ! ---------- Some Way (ME)
# class Games:
#     def __init__(self, namegame):

#         self.namegame = namegame

#     def show_games(self):
#         if self.namegame.__class__ is str:
#             print(f"I Have One Game Called \"{self.namegame}\"")
#         if self.namegame.__class__ is list:
#             print("I Have Many Games:")
#             for x in self.namegame:
#                 print(f"-- {x}")
#         if self.namegame.__class__  is int:
#             print(f"I Have {self.namegame} Game.")

# my_game = Games("Shadow Of Mordor")
# my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
# my_games_count = Games(80)

# my_game.show_games()
# my_games_names.show_games()
# my_games_count.show_games()
# ? --------------------------------- 5  -------------------------
# Main Class
# class Members:

#   def __init__(self, n, p):

#     self.name = n

#     self.permission = p

#   def show_info(self):

#     return f"Your Name Is {self.name} And You Are {self.permission}"

# class Admins(Members):
#     pass

# class Moderators(Members):
#     def __init__(self,n,p):
#         Members.__init__(self,n,p)
# ! ------------- Some Way
# class Moderators(Members):
#     def __init__(self,n,p):
#         super().__init__(n,p)

# member_one = Admins("Osama", "Admin")
# member_two = Moderators("Ahmed", "Moderator")

# print(member_one.show_info())

# print(member_two.show_info())

# ? --------------------------------- 6  -------------------------
# class A:

#   def __init__(self, one):

#     self.one = one

# class B:

#   def __init__(self, two):

#     self.two = two

# class C:

#   def __init__(self, three):

#     self.three = three

# class Name(A,B,C):
#     def __init__(self,one,two,three):
#       A.__init__(self,one)
#       B.__init__(self,two)
#       C.__init__(self,three)

#     def show_name(self):
#       return f"The Name Is \" {self.one}{self.two}{self.three} \""
    
# the_name = Name("El", "ze", "ro")

# print(the_name.show_name())