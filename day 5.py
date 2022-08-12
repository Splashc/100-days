
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welkom bij anti hack sim")
nr_letters = int(input("hoeveel letters wil je hebben?\n"))
nr_symbols = int(input("hoeveel symbolen wil je hebben?\n"))
nr_numbers = int(input("hoeveel nummber wil je hebben?\n"))
wachtwoord_emo = []
for char in range(1, nr_letters + 1):
  wachtwoord_emo.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
  wachtwoord_emo += random.choice(symbols)
for char in range(1, nr_numbers + 1):
  wachtwoord_emo += random.choice(numbers)
random.shuffle(wachtwoord_emo)
wachtwoord = ""
for char in wachtwoord_emo:
  wachtwoord += char
print(f"jij wachttwoord is: {wachtwoord}")