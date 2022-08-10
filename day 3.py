#number = int(input("Which number do you want to check? "))
##
#if number % 2 == 0:
#    print("lOl")
#else:
#    print("Noob")

#height = float(input("enter your height in m: "))
#weight = float(input("enter your weight in kg: "))

#height = height/100
#bmi= weight/(height*height)
#if bmi < 18.5:
#  print(f"Je hebt ondergwicht sukkel {bmi}.")
#elif bmi < 25:
#  print(f"JE bent normal {bmi}.")
#elif bmi < 30:
#  print(f"JE bent beetje dik {bmi}.")
#elif bmi < 35:
#  print(f"Je bmi is {bmi} ga sporten.")
#else:
#  print(f"Erik je hebt kaulo veel overgewicht {bmi}.")
# Ole advontuur
import time
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("\nWelkom bij Ole Simulator")
username = input("Vul je Username in:\n")
print(f"Welkom bij Ole Simulator {username}")
print("Game is aan het laden.")
time.sleep(1)
print("Game is aan het Laden..")
time.sleep(1)
print("Laden…\n█▒▒▒▒▒▒▒▒▒")
time.sleep(3)
print("10%\n███▒▒▒▒▒▒▒")
time.sleep(1)
print("30%\n█████▒▒▒▒▒")
time.sleep(2)
print("50%\n███████▒▒▒")
time.sleep(3)
print("100%\n██████████")
time.sleep(3)
print("Klaar met laden")
leeftijd = input('Je moet 18 jaar zijn om deze game te spelen hou oud ben je?:\n').lower()
if leeftijd != "18":
    print("Je bnet geen 18+ dus je mag niet veder")
    exit()
if leeftijd == "18":
    print("Jij bent 18 top nu mag je veder met spelen")