import os
from time import sleep


a ='\033[31m'
b ='\033[32m'
c ='\033[35m'
os.system('clear')
print(a+'\tMENAMBAHKAN PINTASAN')
print(b+'\tUP, DOWN, RIGHR, LEFT, DLL')
print('\t Channel Youtube :  Tutorial pedia')
print('\t Github          : https://www.github.com/borneoX')
print(a+'+'*60)
print('\nProccess..')
sleep(1)
print(a+'\n[+] Mengambil File Default Termux')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(b+'[+]Success !')
sleep(1)
print(a+'\n[+] menambahkan File Pintasan....')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontrol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontrol.write(key)
kontrol.close()
sleep(1)
print(a+'[+] Proccessing....')
sleep(1)
print(b+'\n[+] Please wait....')
sleep(2)
os.system('termux-reload-settings')
print(c+'[+] Proccessing Completed')
os.system('xdg-open https://www.youtube.com/c/Tutorial pedia')
sleep(1)
