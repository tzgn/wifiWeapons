echo "[0;1;35;95m┌─[0;1;31;91m──[0;1;33;93m──[0;1;32;92m──[0;1;36;96m──[0;1;34;94m──[0;1;35;95m──[0;1;31;91m──[0;1;33;93m──[0;1;32;92m──[0;1;36;96m──[0;1;34;94m─┐[0m
[0;1;31;91m│P[0;1;33;93m4D[0;1;32;92m4W[0;1;36;96m4N[0;1;34;94m's[0m [0;1;35;95mW[0;1;31;91mIF[0;1;33;93mI[0m [0;1;32;92mWE[0;1;36;96mAP[0;1;34;94mON[0;1;35;95mS│[0m
[0;1;33;93m└─[0;1;32;92m──[0;1;36;96m──[0;1;34;94m──[0;1;35;95m──[0;1;31;91m──[0;1;33;93m──[0;1;32;92m──[0;1;36;96m──[0;1;34;94m──[0;1;35;95m──[0;1;31;91m─┘[0m"
echo "1--deauther"
echo "2--handshaker"
echo "3--cracker"
echo "4--wordlister"
read -p "your choice.....: " choice

if [ "$choice" -eq "1" ]; then
    python3 /root/.p4d4w4nsystems/p4d4w4n_deauther.py
elif [  "$choice" -eq "2" ]; then
    python3 /root/.p4d4w4nsystems/p4d4w4n_handshaker.py
elif [ "$choice" -eq "3" ]; then
    python3 /root/.p4d4w4nsystems/p4d4w4n_wificracker.py
elif [ "$choice" -eq "4" ]; then
    read -p "default or special passwords:[def/spe]: " pass
    if [ "$pass" == "def" ]; then
        python3 /root/.p4d4w4nsystems/p4d4w4n_router_def_wordlister.py
    elif [ "$pass" == "spe" ]; then
        python3 /root/.p4d4w4nsystems/p4d4w4n_wordlister.py
    else
        echo "wrong input quitting.............."; exit 1
    fi
fi