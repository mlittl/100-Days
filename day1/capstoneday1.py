#Band Name Generator
print("Hello, welcome to the band name generator!")

city = input("What city did you grow up in?\n")
pet = input("What is the name of your pet?\n")


if city == "" or pet == "":
  print("You didn't enter a city or pet name.")

citycase = city.upper()
petcase = pet.upper()

combined = citycase[0] + city[1:] + " " + petcase[0] + pet[1:]

print("\n" + combined)
