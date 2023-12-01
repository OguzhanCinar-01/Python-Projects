import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Pypassword Genarator! ")
num_letters = int(input("How many letters would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))

password = ""
random_list = []
for char in range (1, num_letters+1):
    random_char = random.choice(letters)
    random_list.append(random_char)

for char in range (1, num_numbers+1):
    random_number = random.choice(numbers)
    random_list.append(random_number)

for char in range (1, num_symbols+1):
    random_symbols = random.choice(symbols)
    random_list.append(random_symbols)

random.shuffle(random_list)
#print(random_list)
for x in random_list:
    password = password + x
print(password)
