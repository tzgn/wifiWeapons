from os import system
wordlist=input("wordlist name: ")
routermac=input("router mac adress: ")
capname=input("cap file name: ")
system(f"aircrack-ng -w {wordlist} -b {routermac} {capname}*.cap")

