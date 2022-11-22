import random
from main import kerdesek
from main import *

corrCount = 0
random.shuffle(kerdesek)
for kerdes in kerdesek:
  print(kerdes.question)
  print("Lehetséges válaszok:")
  possible = kerdes.otherAnsw + [kerdes.corrAnsw]
  random.shuffle(possible)
  count = 0
  while count < len(possible):
    print(str(count+1) + ": " + possible[count])
    count += 1
  print("Add meg a válaszod:")
  userAnsw = input()
  while not userAnsw.isdigit():
    print("Ez nem egy szám volt:")
    userAnsw = input()
  userAnsw = int(userAnsw)
  while not (userAnsw > 0 and userAnsw <= len(possible)):
    print("Ez a szám nem tartozik egy válaszhoz se:")
    userAnsw = input()
  if possible[userAnsw-1] == kerdes.corrAnsw:
    print("Helyes válasz.")
    corrCount += 1
  else:
    print("A válasz rossz.")
    print("A helyes válasz: " + kerdes.corrAnsw)
  print("")

print("A " + str(corrCount) + " elérhető pontból " + str(len(kerdesek)) + "-ot sikerült elérnie a kedves játékosnak.")
