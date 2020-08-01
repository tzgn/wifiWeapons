echo "[0;1;35;95m┌─[0;1;31;91m──[0;1;33;93m──[0;1;32;92m──[0;1;36;96m──[0;1;34;94m──[0;1;35;95m──[0;1;31;91m──[0;1;33;93m──[0;1;32;92m──[0;1;36;96m─┐[0m
[0;1;31;91m│t[0;1;33;93mzg[0;1;32;92mn'[0;1;36;96ms[0m [0;1;34;94mWi[0;1;35;95m-F[0;1;31;91mi[0m [0;1;33;93mWe[0;1;32;92map[0;1;36;96mon[0;1;34;94ms│[0m
[0;1;33;93m└─[0;1;32;92m──[0;1;36;96m──[0;1;34;94m──[0;1;35;95m──[0;1;31;91m──[0;1;33;93m──[0;1;32;92m──[0;1;36;96m──[0;1;34;94m──[0;1;35;95m─┘[0m"


echo "1--deauther"
echo "2--handshaker"
echo "3--cracker"
echo "4--wordlister"
read -p "your choice.....: " choice

if [ "$choice" -eq "1" ]; then
    python3 /root/.tzgnsystems/tzgn_deauther.py
elif [  "$choice" -eq "2" ]; then
    python3 /root/.tzgnsystems/tzgn_handshaker.py
elif [ "$choice" -eq "3" ]; then
    python3 /root/.tzgnsystems/tzgn_wificracker.py
elif [ "$choice" -eq "4" ]; then
    read -p "default or special passwords:[def/spe]: " pass
    if [ "$pass" == "def" ]; then
        python3 /root/.tzgnsystems/tzgn_router_def_wordlister.py
    elif [ "$pass" == "spe" ]; then
        python3 /root/.tzgnsystems/tzgn_wordlister.py
    else
        echo "wrong input quitting.............."; exit 1
    fi
fi
