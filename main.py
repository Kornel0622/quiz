from functions import *


valasz = input("Melyik évben született Hitler? ")
if valasz == "1889":
    print("A válasz helyes!")
else:
    print(f"A válasz '1889', nem {valasz!r}")

kerdes3()
choice = ''
while choice != '0':
    choice = kerdesMenu3()
    if choice == '1':
        valasz1()
        input()
    elif choice == '2':
        valasz2()
        input()
    elif choice == '3':
        valasz3()
        input()