
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random
a = 0
while a != 10:
  letter_part = ""
  for letter in letters:
    letter = random.choice(letters)
    letter_part += letter
    if len(letter_part) == nr_letters:
      break

  number_part = ""
  for number in numbers:
    number = random.choice(numbers)
    number_part += number
    if len(number_part) == nr_numbers:
      break

  symbol_part = ""
  for symbol in symbols:
    symbol = random.choice(symbols)
    symbol_part += symbol
    if len(symbol_part) == nr_symbols:
      break

  easy_password = letter_part + number_part + symbol_part
  list1 = list(easy_password)
  random.shuffle(list1)
  hard_password = ""
  for hard1 in list1:
    hard_password += hard1
  print(hard_password)
  a +=1