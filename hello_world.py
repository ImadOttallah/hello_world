print("Howdy Y'all!!")

animals = [ "Triceratops", "Gorilla", "Corgi", "Toucan"]

for animal in animals:
  if len(animal) == 5:
    print(animal)

greeting = input("Pick your greeting: \n A. Howdy B. hello C. OK' [A/B/C]? : ")
if greeting == "A": 
  print ("Yes")
elif greeting == "B":
  print("no")
elif greeting == "C":
  print("PK")
 