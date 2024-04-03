# z = 0
# y = 0
# x = []
# x1 = []
# n = int(input("Wpisz dane n: "))
#
# for i in range(n):
#     l=int(input("Wpisz liczbę do n-permutacji: "))
#     x.append(l)
# print(x)
# # for i in x:
# #     if i>n:
# #         i+=1
# for i in x:
#     if i>n:
#         y += 1
#
#     elif x1.count(i)>=1:
#         y += 1
#     x1.append(i)
#
# print(f"Musisz pozamieniać: {y} liczby :3")

# ----------------Lista zakupów--------------------------------
# n = 10
# n1 = 20
# n2 = 30
# l = []
# wyb = int(input("Wybierz długość listy |10|20|30|:      "))
# if wyb == 10:
#     for i in range(n):
#         list = input("lista zakupów:")
#         l.append(list)
#
# elif wyb == 20:
#     for i in range(n1):
#         list1 = input("lista zakupów:")
#         l.append(list)
#
# elif wyb == 30:
#     for i in range(n2):
#         list2 = input("lista zakupów:")
#         l.append(list)
#
# else:
#     print("źle wpisałeś")
#
# print(f"Twoja lista zakupów: {l} |")
#
# for i in l:
#     if i == "hamburger":
#         print("ty gruba świnio nie ma fast foodów!!!")
#         l.remove(i)
# print(l)
# #
# ----------------Funkcje--------------------------------

# x = int(input("Podaj liczbę 1: "))
# x1 = int(input("Podaj liczbę 2: "))
# def mnożenie(x,x1):
#         y = x * x1
#         print(y)
#         if y % 2 == 0:
#             print("Wynik parzysty")
#         else:
#             yW = y % 2
#             print(yW)
# mnożenie(x,x1)

# --------------Zad-1------------------------------------
# x = input("podaj zdanie: ")
# if x.find("samochód"):
#     print("w zdaniu jest samochód!")
# else:
#     print("Ni ma")
#--------------------------------------------------------
t = [
    ['tesco', 'lidl', 'biedronka', 'biedronka', 'biedronka', 'biedronka'],
    ['makro', 'lidl', 'carrefour'],
    ['arhelan', 'biedronka', 'tesco']
]
s = {}
for i in t:
     try:
          print(i[3])
     except:
          print("nie")

     for j in i:
          print(j[0])
     print("\n")
