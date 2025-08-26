import math
import random

NA = random.random()
print(NA)
print(50*("-"))

NA2 = random.randrange(0 ,100)
print(NA2)
print(50*("-"))

NA3 = random.randrange(0 , 100 , 5)
print(NA3)
print(50*("-"))

LI = ["Pão" , "Leite" , "Batata" ,"Alface"]
print(random.choice(LI))
print(50*("-"))
print(random.choices(LI , k = 2))



