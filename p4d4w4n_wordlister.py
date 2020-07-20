isim = input("name: ")
soyisim = input("surname: ")

tercih = input("Will extra information be entered?[yes/No]: ")

if tercih == "yes" or tercih=="y":
    girdi = int(input("how many information will be entered?: "))
    liste = []
    ekler = []
    for i in range(girdi):
        liste.append(input(f"{i+1}. girdi: "))
        ekler.append(input("will be added to the beginning or end of the password?[b/e]"))

else:
    pass

pass_array = []

def format1():
    pass_array.append(f"{isim.capitalize()}{soyisim.capitalize()}")
    pass_array.append(f"{soyisim.capitalize()}{isim.capitalize()}")
    pass_array.append(f"{isim[0].capitalize()}{soyisim.capitalize()}")
    pass_array.append(f"{isim}{soyisim}")
    pass_array.append(f"{soyisim}{isim}")
    pass_array.append(f"{isim[0]}{soyisim}")
    if tercih=="yes":

            for i in range(girdi):
                if ekler[i] == "s":
                    pass_array.append(f"{isim.capitalize()}{soyisim.capitalize()}{liste[i]}")
                    pass_array.append(f"{soyisim.capitalize()}{isim.capitalize()}{liste[i]}")
                    pass_array.append(f"{isim[0].capitalize()}{soyisim.capitalize()}{liste[i]}")
                    pass_array.append(f"{isim}{soyisim}{liste[i]}")
                    pass_array.append(f"{soyisim}{isim}{liste[i]}")
                    pass_array.append(f"{isim[0]}{soyisim}{liste[i]}")
                    pass_array.append(f"{isim.capitalize()}{liste[i]}")
                    pass_array.append(f"{soyisim.capitalize()}{liste[i]}")
                    pass_array.append(f"{isim}{liste[i]}")
                    pass_array.append(f"{soyisim}{liste[i]}")
                if ekler[i] == "b":
                    pass_array.append(f"{liste[i]}{isim.capitalize()}{soyisim.capitalize()}")
                    pass_array.append(f"{liste[i]}{soyisim.capitalize()}{isim.capitalize()}")
                    pass_array.append(f"{liste[i]}{isim[0].capitalize()}{soyisim.capitalize()}")
                    pass_array.append(f"{liste[i]}{isim}{soyisim}")
                    pass_array.append(f"{liste[i]}{soyisim}{isim}")
                    pass_array.append(f"{liste[i]}{isim[0]}{soyisim}")
                    pass_array.append(f"{liste[i]}{isim.capitalize()}")
                    pass_array.append(f"{liste[i]}{soyisim.capitalize()}")
                    pass_array.append(f"{liste[i]}{isim}")
                    pass_array.append(f"{liste[i]}{soyisim}")

symbols = [".","_"]
def format2():
    for j in symbols:
        pass_array.append(f"{isim.capitalize()}{j}{soyisim.capitalize()}")
        pass_array.append(f"{soyisim.capitalize()}{j}{isim.capitalize()}")
        pass_array.append(f"{isim[0].capitalize()}{j}{soyisim.capitalize()}")
        pass_array.append(f"{isim}{j}{soyisim}")
        pass_array.append(f"{soyisim}{j}{isim}")
        pass_array.append(f"{isim[0]}{j}{soyisim}")
        if tercih=="yes":

                for i in range(girdi):
                    if ekler[i] == "s":
                        pass_array.append(f"{isim.capitalize()}{j}{soyisim.capitalize()}{liste[i]}")
                        pass_array.append(f"{soyisim.capitalize()}{j}{isim.capitalize()}{liste[i]}")
                        pass_array.append(f"{isim[0].capitalize()}{j}{soyisim.capitalize()}{liste[i]}")
                        pass_array.append(f"{isim}{j}{soyisim}{liste[i]}")
                        pass_array.append(f"{soyisim}{j}{isim}{liste[i]}")
                        pass_array.append(f"{isim[0]}{j}{soyisim}{liste[i]}")
                        pass_array.append(f"{isim.capitalize()}{j}{liste[i]}")
                        pass_array.append(f"{soyisim.capitalize()}{j}{liste[i]}")
                        pass_array.append(f"{isim}{j}{liste[i]}")
                        pass_array.append(f"{soyisim}{j}{liste[i]}")
                        pass_array.append(f"{isim.capitalize()}{soyisim.capitalize()}{j}{liste[i]}")
                        pass_array.append(f"{soyisim.capitalize()}{isim.capitalize()}{j}{liste[i]}")
                        pass_array.append(f"{isim[0].capitalize()}{soyisim.capitalize()}{j}{liste[i]}")
                        pass_array.append(f"{isim}{soyisim}{j}{liste[i]}")
                        pass_array.append(f"{soyisim}{isim}{j}{liste[i]}")
                        pass_array.append(f"{isim[0]}{soyisim}{j}{liste[i]}")
                    if ekler[i] == "b":
                        pass_array.append(f"{liste[i]}{j}{isim.capitalize()}{soyisim.capitalize()}")
                        pass_array.append(f"{liste[i]}{j}{soyisim.capitalize()}{isim.capitalize()}")
                        pass_array.append(f"{liste[i]}{j}{isim[0].capitalize()}{soyisim.capitalize()}")
                        pass_array.append(f"{liste[i]}{j}{isim}{soyisim}")
                        pass_array.append(f"{liste[i]}{j}{soyisim}{isim}")
                        pass_array.append(f"{liste[i]}{j}{isim[0]}{soyisim}")
                        pass_array.append(f"{liste[i]}{j}{isim.capitalize()}")
                        pass_array.append(f"{liste[i]}{j}{soyisim.capitalize()}")
                        pass_array.append(f"{liste[i]}{j}{isim}")
                        pass_array.append(f"{liste[i]}{j}{soyisim}")
                        pass_array.append(f"{liste[i]}{isim.capitalize()}{j}{soyisim.capitalize()}")
                        pass_array.append(f"{liste[i]}{soyisim.capitalize()}{j}{isim.capitalize()}")
                        pass_array.append(f"{liste[i]}{isim[0].capitalize()}{j}{soyisim.capitalize()}")
                        pass_array.append(f"{liste[i]}{isim}{j}{soyisim}")
                        pass_array.append(f"{liste[i]}{soyisim}{j}{isim}")
                        pass_array.append(f"{liste[i]}{isim[0]}{j}{soyisim}")
from random import randint

x=int(input("random numbers: "))
y=int(input("number of digits: "))
def format3():
    for i in range(x):
        password = ""
        for j in range(y):
            password+=str(randint(0,10))
        pass_array.append(password)
        del password
def format4():
    pass_array.append("123456789")
    pass_array.append("987654321")
    pass_array.append("12345678dokuz")
    pass_array.append("159753456852")
    pass_array.append("741852963")
    pass_array.append("111111111")
    pass_array.append("222222222")
    pass_array.append("444444444")
    pass_array.append("555555555")
    pass_array.append("666666666")
    pass_array.append("777777777")
    pass_array.append("888888888")
    pass_array.append("999999999")
    pass_array.append("11111111")
    pass_array.append("22222222")
    pass_array.append("44444444")
    pass_array.append("55555555")
    pass_array.append("66666666")
    pass_array.append("77777777")
    pass_array.append("88888888")
    pass_array.append("99999999")
    pass_array.append("birikiucdortbes")
    pass_array.append("1234567sekiz")
    pass_array.append("123456yedi")
    pass_array.append("12345alti")
    pass_array.append("12345678987654321")
    pass_array.append("123456789987654321")
format1()
format2()
format3()
format4()

with open("wifi_wordlist.txt","w") as file:
    for i in pass_array:
        if len(i)>=8:
            file.write(f"{i}\n")
print("saved as wifi_wordlist.txt")
