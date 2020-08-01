from colorama import Fore,Back
from random import randint

lower = "abcdefghijklmnoprstuvyzqx"
upper = "ABCDEFGHIJKLMNOPRSTUVYZQX"
numbers = "1234567890"
symbols = "!%&/?*#_-.,"

print (Fore.RED+"keymaster#~",end="")
quest = input(Fore.BLUE+"do you want add symbols?[Y/n]>")

if quest =="y" or quest=="Y" or quest =="yes" or quest=="YES":
	all = lower+upper+numbers+symbols
elif quest =="n" or quest=="N" or quest =="no" or quest=="NO":
	all = lower+upper+numbers
else:
	all = lower+upper+numbers+symbols

print (Fore.RED,end="")
print ("keymaster#~",end="")
print (Fore.BLUE,end="")
keys = int(input("keys>"))
print (Fore.RED,end="")
print ("keymaster#~",end="")
print (Fore.BLUE,end="")
cells = int(input("cells>"))
print (Fore.GREEN,end="")

counter = 0
passwords = []

for i in range(keys):
    words = []
    for j in range(cells):
        words.append(all[randint(0,len(all)-1)])
    word = ""
    for k in words:
        word+=k
    passwords.append(word)
    counter+=1
    print (Fore.MAGENTA+f"##keymaster is created {counter} keys....")
    del word
    del words

with open("passwords.txt","w") as file:
    for i in passwords:
        file.write(f"{i}\n")

print (Fore.RED+"keymaster#~",end="")
print (Fore.GREEN+"response: passwords.txt created.")
