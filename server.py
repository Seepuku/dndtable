import sys
import re
import socket
import time

station1 = ['', '192.168.1.201']
station2 = ['', '192.168.1.12']
station3 = ['', '192.168.1.13']
station4 = ['', '192.168.1.14']
station5 = ['', '192.168.1.15']
KaD = {} #Keep alive Dictionary

def write_online():
    onlinetxt = open("online.txt", 'w')
    if station1[0] != '':
        onlinetxt.writelines(station1[0] + ',' + station1[1] + "\n")
    else:
        onlinetxt.writelines('No Toon' + "\n")
    if station2[0] != '':
        onlinetxt.writelines(station2[0] + ',' + station2[1] + "\n")
    else:
        onlinetxt.writelines('No Toon' + "\n")
    if station3[0] != '':
        onlinetxt.writelines(station3[0] + ',' + station3[1] + "\n")
    else:
        onlinetxt.writelines('No Toon' + "\n")
    if station4[0] != '':
        onlinetxt.writelines(station4[0] + ',' + station4[1] + "\n")
    else:
        onlinetxt.writelines('No Toon' + "\n")
    if station5[0] != '':
        onlinetxt.writelines(station5[0] + ',' + station5[1])
    else:
        onlinetxt.writelines('No Toon' + "\n")
    onlinetxt.close()



while True:
    #msg = client.recv(BUFSIZ).decode("utf8")
    msg=input("TYPE TO ME: ")
    msgSplit = msg.split("||")
    if re.match('keepalive', msgSplit[0], re.IGNORECASE):
        KaD[msgSplit[1]] = time.time()
        print(KaD)

    elif re.match('message', msgSplit[0], re.IGNORECASE):
        msgTo = msgSplit[2]
        msgFrom = msgSplit[1]
        msgText = msgSplit[3]
        if msgSplit[1] > msgSplit[2]:
            logname = msgSplit[1]+"-"+msgSplit[2]
        else:
            logname = msgSplit[2]+'-'+msgSplit[1]

        f = open('./chatlogs/' + logname+'.txt', 'a+')
        f.write(msgSplit[1]+": " +msgText + '\n')
        f.close()
    elif re.match('register', msgSplit[0], re.IGNORECASE):
        #msgSplit[1] = toon [2] = IP
        if msgSplit[2] == station1[1]:
            station1[0] = msgSplit[1]
        elif msgSplit[2] == station2[1]:
            station2[0] == msgSplit[1]
        elif msgSplit[2] == station3[1]:
            station3[0] == msgSplit[1]
        elif msgSplit[2] == station4[1]:
            station4[0] == msgSplit[1]
        elif msgSplit[2] == station5[1]:
            station5[0] == msgSplit[1]
        write_online()

#Keepalive Purge
    if station1[0] in KaD:
        if time.time() - KaD[station1[0]] > 30:
            print(station1[0] + ' Removed from Reg')
            station1[0] = ''
            write_online()
    if station2[0] in KaD:
        if time.time() - KaD[station2[0]] > 30:
            print(station2[0] + ' Removed from Reg')
            station2[0] = ''
            write_online()
    if station3[0] in KaD:
        if time.time() - KaD[station3[0]] > 30:
            print(station3[0] + ' Removed from Reg')
            station3[0] = ''
            write_online()
    if station4[0] in KaD:
        if time.time() - KaD[station4[0]] > 30:
            print(station4[0] + ' Removed from Reg')
            station4[0] = ''
            write_online()
    if station5[0] in KaD:
        if time.time() - KaD[station5[0]] > 30:
            print(station5[0] + ' Removed from Reg')
            station1[0] = ''
            write_online()
