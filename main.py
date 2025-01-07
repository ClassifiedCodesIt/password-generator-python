print("Welcome to the Classified Password Generator!")
def my_function():
  import random
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
  pass_length = int(input("How many characters do you need your password to be?\n"))
  nr_letters= int(input("How many letters would you like in your password?\n")) 
  nr_symbols = int(input(f"How many symbols would you like?\n"))
  nr_numbers = int(input(f"How many numbers would you like?\n"))
  if pass_length != nr_letters + nr_symbols + nr_numbers:
    print(f"Error!! Your password needs to equal {pass_length} characters total.\nPlease try again...")
    my_function()
  elif pass_length == nr_letters + nr_symbols + nr_numbers:
    password_list = []
    for char in range(1, nr_letters +1):
      password_list.append(random.choice(letters))
    for char in range(1, nr_symbols +1):
      password_list.append(random.choice(symbols))
    for chare in range(1, nr_numbers +1):
      password_list.append(random.choice(numbers))
    random.shuffle(password_list)
    password = ""
    for char in password_list:
      password += char
    print(f"Your password is: {password}")
my_function()    