import os
channel=input("router cahnnel: ")
bssid=input("router mac adress: ")
writername=input("cap name: ")
interface=input("interface name: ")

os.system(f"airodump-ng -c {channel} --bssid {bssid} -w {writername} -i {interface}")

