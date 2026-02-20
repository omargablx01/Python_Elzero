
# todo >>>>                                                 Assignments  41 ==> 46                                            <<<<<
# ? --------------------------------- 1  -------------------------
# num1 = int(input("Num One : ").strip())
# num2 = int(input("Num Two : ").strip())
# operation = input("Write You'r Operation ( '+' '-' '*' '**' '/' '//' '%' ) : ").strip()

# if operation == "+" :
#     print(f"{num1} {operation} {num2} = {num1 + num2 }")
# elif operation == "-" :
#     print(f"{num1} {operation} {num2} =  {num1 - num2 }")
# elif operation == "*" :
#     print(f"{num1} {operation} {num2} =  {num1 * num2 }")
# elif operation == "**" :
#     print(f"{num1} {operation} {num2} =  {num1 ** num2 }")
# elif operation == "/" :
#     print(f"{num1} {operation} {num2} =  {num1 / num2 }")
# elif operation == "//" :
#     print(f"{num1} {operation} {num2} =  {num1 // num2 }")
# elif operation == "%" :
#     print(f"{num1} {operation} {num2} =  {num1 % num2 }")
# else :
#     print("Wrong operation Try Again Later ..!")

# ? --------------------------------- 2  -------------------------
# age = 17
# my_age ="App Is Suitable For You" if age > 16 else "App Is Not Suitable For You"
# print(my_age)
# ? --------------------------------- 3  -------------------------
# my_age = int(input("Write Age : ").strip())

# months = my_age * 12
# weeks = months * 4
# days = 365 * my_age
# hours = days * 24
# minutes = hours * 60
# seconds = minutes * 60

# if my_age > 10 and my_age < 100:
#     print(f"Your Age In Months Is {months} Months")
#     print(f"Your Age In Weeks Is {weeks} Weeks")
#     print(f"Your Age In Days Is {days} Days")
#     print(f"Your Age In hours Is {hours:,} hours")
#     print(f"Your Age In minutes Is {minutes:,} minutes")
#     print(f"Your Age In seconds Is {seconds:,} seconds")
# else : 
#     big_small = f"Bad Age You Soo Small {my_age} Year .. Go To Your M0M .." if my_age < 10 else f"You Soo Big {my_age} Year Go To Allah .."
#     print(big_small)

# ? --------------------------------- 4  -------------------------
# country = input("Input Your Country : ").strip().capitalize()
# countries = ["Egypt", "Palestine", "Syria", "Yemen", "Ksa", "Usa", "Bahrain", "England"]
# price = 100
# discount = 30

# if country in countries :
#     print(f"Your Country {country} For Discount And The Price After Discount Is ${price - discount}")
# else :
#     print(f"Your Country Not Eligible For Discount And The Price Is ${price}")