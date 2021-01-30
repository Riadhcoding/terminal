import os, sys, time
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(00000.02)
def clear():
    os.system('clear')
os.system('git pull')

logo = """
\033[1;34m                       dP   dP                         
\033[1;34m                       88   88                         
\033[1;37m   88d888b. dP    dP d8888P 88d888b. .d8888b. 88d888b. 
\033[1;37m   88'  `88 88    88   88   88'  `88 88'  `88 88'  `88 
\033[1;33m   88.  .88 88.  .88   88   88    88 88.  .88 88    88 
\033[1;33m   88Y888P' `8888P88   dP   dP    dP `88888P' dP    dP 
\033[1;34m   88            .88                                   
\033[1;34m   dP        d8888P  

\033[1;34m   dP    8888b          
\033[1;37m   88 o  88             
\033[1;33m   88 dP 88aaa  .d8888b. 
\033[1;33m   88 88 88     88ooood8 
\033[1;37m   88 88 88     88 \033[1;31m    Created by Riad
\033[1;34m   dP dP dP     `88888P
"""
clear()
print(logo)
print("\033[1;31m{1} \033[1;34mRestore the default terminal")
time.sleep(0.3)
print("\033[1;31m{2} \033[1;34mMy Youtube")
time.sleep(0.3)
print("\033[1;31m{3} \033[1;34mMy instagram")
time.sleep(0.3)
print("\033[1;31m{0} \033[1;34mExit")
time.sleep(0.3)
print('')
choose = input("\033[1;31m{?}\033[1;37mChoose an option : ")
if choose == '1':
    jalan("please wait...")
    os.chdir('/data/data/com.termux/files/usr/etc')
    if os.path.exists('bash.bashrc'):
        os.remove('bash.bashrc')
    os.chdir('/data/data/com.termux/files/home/terminal')
    os.system('cp bash.bashrc /data/data/com.termux/files/usr/etc')
    clear()
    print(logo)
    os.system('termux-reload-settings')
    print("\033[1;31mPlease Restart Application")
    os.system('exit')
elif choose == '2':
    os.system('xdg-open https://www.youtube.com/c/pythonlife')
    clear()
    print(logo)
    time.sleep(0.3)
    os.system('exit')
elif choose == '3':
    os.system('xdg-open https://www.instagram.com/python.life')
    clear()
    print(logo)
    time.sleep(0.3)
    os.system('exit')
elif choose == '0':
    clear()
    print(logo)
    os.system('exit')
