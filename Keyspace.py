# Keyspace Puzzle 64 Random
# Made by Andrei Melek
# https://github.com/xh0st/keyspace64

try:
    import random
    from bitcoin import *

# If required imports are unavailable, we will attempt to install them!

except ImportError: 
    import subprocess
    subprocess.check_call(["python3", '-m', 'pip', 'install', 'bitcoin'])

while True:  
    low  = 0x100000000000000000
    high = 0x1fffffffffffffffff
    val = str ( hex ( random.randrange( low, high ) ) )[2:]
    result = val.rjust(46 + len(val), '0')
    priv = result
    pub = privtopub(priv)
    pubkey1 = encode_pubkey(privtopub(priv), "bin_compressed")
    addr = pubtoaddr(pubkey1)
    n = addr
    if n.startswith('19vkiEajfhuZ8bs8Zu2jgmC6oqZbWqh'):
        print ("found!!",addr,result)
        k1 = priv
        k2 = pub
        k3 = addr

        file = open('boom.txt', 'a')
        file.write("Private key: " + k1 + '\n' + "Public key: " + k2 + '\n' + "Address: " + k3 + '\n\n')    
        file.close()
    else:
        print("\rsearching...", addr, result, end='')
