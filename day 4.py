import random

steen = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papier = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

schaar = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

foto = [steen, papier, schaar]

mens = int(input("Steen (0)\nPapier (1)\nSchaar (2)?\n"))
if mens >= 3 or mens < 0:
  print("HAHAH noob jij hebt verloren")
else:
  print(foto[mens])

robot = random.randint(1, 3)
print("Robot kiest:")
print(foto[robot])

if mens == 0 and robot == 2:
  print("GG bozo")
elif robot == 0 and mens == 2:
  print("L bozo")
elif robot > mens:
  print("L BOZO")
elif mens > robot:
  print("GG BOZO")
elif robot == mens:
  print("NOOB")