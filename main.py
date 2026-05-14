import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number =['0','1','2','3','4','5','6','7','8','9']
symbols =['!','@','#','$','%','^','&','*','()','_','-','+']

print("Welcome to my password Generator")
nr_letters = int(input("How many letters would you like in your password \n"))
nr_number = int(input("How many password would you like \n"))
nr_symbols = int(input("How many symbols would you like \n"))


password_list = []

for char in range (0, nr_letters):
    password_list.append(random.choice(letters))


for char in range (0, nr_number):
    password_list.append(random.choice(number))


for char in range (0, nr_symbols):
    password_list.append(random.choice(number))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is:{password}")