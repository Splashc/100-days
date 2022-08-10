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
time.sleep(2)
print("10%\n███▒▒▒▒▒▒▒")
time.sleep(3)
print("30%\n█████▒▒▒▒▒")
time.sleep(3)
print("50%\n███████▒▒▒")
time.sleep(10)
print("Fout bij het laden opnieuw laden.")
time.sleep(1)
print("Game is aan het laden.")
time.sleep(1)
print("Game is aan het Laden..")
time.sleep(1)
print("Laden…\n█▒▒▒▒▒▒▒▒▒")
time.sleep(2)
print("10%\n███▒▒▒▒▒▒▒")
time.sleep(3)
print("30%\n█████▒▒▒▒▒")
time.sleep(3)
print("50%\n███████▒▒▒")
time.sleep(10)
print("100%\n██████████")
time.sleep(1)
print("Klaar met laden")
leeftijd = input('Je moet 18 jaar zijn om deze game te spelen hou oud ben je?:\n').lower()
if leeftijd != "18":
    print("Je bent geen 18+ dus je mag niet veder")
    exit()
if leeftijd == "18":
    print("Jij bent 18 top nu mag je veder met spelen")
meintje = input('JE komt meintje tegen op straat ze vraagt of je mee naar haar huis gaat wat ga je doen\n(1) Rennen\n(2) Me naar huis\n').lower()
if meintje != "1":
    print("Je bent met meintje naar huis gegaan en daar heeft ze je vast gebonden aan een bed")
    print("Nu kom je niet meer weg GAME OVER")
    exit()
if meintje  == "1":
    print("Je bent weg weggerend en hebt meintje haar val overleeft")
erik = input('JE komt erik tegen en hij heeft je wil je wat vertelen over luckycraft ranks wat ga je doen\n(1) Je gooit erik van en gebouw\n(2) Je luisterd naar erik\n(3) Je pleegd zelfmoord\n').lower()
if erik == "1":
    print("HAHAHA erik gooit jou eerder L bozo game over")
    exit()
if erik  == "2":
    print("Erik zorgt ervoor daat jij hem 10000 euro geeft nu woon je onder en brug GAME OVER")
    exit()
if erik == "3":
    print("HMM erik houd je tegen en laat je gaan")
luuk = input('Luuk houd van koekjes geef je hem dino koekjes\n(1) Ja\n(2) Nee\n').lower()
if luuk != "1":
    luuk2 = input("Hmm dat vind hij jammer hij wordt super boos en rent achter je wat ga je doen\n(1) fornite battlpass\n(2) 360 no scope\n")
    if luuk2 != "1":
        print("de 360 no scope was zo goed dat je je zelf raakte GAME OVER")
        exit()
    if luuk2 == "1":
        print("je leeft en mag door naar de volgende opdracht onderweg breek je je hand")
if luuk  == "1":
    print("Luuk is heel blij maar zo blij dat hij ook bijna je hand op eet")
ole = input('Je hebt veel pijn daarom ga je naar het ziekenhuis van OLe Wat ga je doen\n(1) $10000 betaalen\n(2) Ole dood maken\n').lower()
if leeftijd != "1":
    print("L bozo Ole is 10x beter NOOB GAME OVER")
    exit()
if leeftijd == "1":
    print("JE hebt betaald maar heb geen geld meer nu leeft je onder en brug en ga je dood door ziektes GAME OVER")
else:
    ("DOmbo dat kan niet he")