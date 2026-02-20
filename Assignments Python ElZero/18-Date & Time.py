
# t~ >>>>                                                 Assignments  79 ==> 80                                            <<<<<
# ? --------------------------------- 1  -------------------------
# import datetime

# mydate = f"{datetime.datetime(2021,6,25)}".split(" ")
# datenow = f"{datetime.datetime.now()}".split(" ")

# mydate1 = datetime.datetime(2021,6,25)
# datenow1 = datetime.datetime.now()

# print(f"Days From {mydate[0]} To {datenow[0]} Is => {(datenow1 - mydate1).days} Days.")
# ? --------------------------------- 2  -------------------------
# import datetime

# datenow = datetime.datetime.now()

# print(datenow.strftime("%Y-%m-%d")) # 2026-01-16
# print(datenow.strftime("%b %d,%Y")) # Jan 16,2026
# print(datenow.strftime("%d - %b - %Y")) # 16 - Jan - 2026
# print(datenow.strftime("%d / %b / %y")) # 16 / Jan / 26
# print(datenow.strftime("%d / %B / %Y")) # 16 / January / 2026
# print(datenow.strftime("%a, %d %B %Y")) # Fri, 16 January 2026