# -*- coding: utf-8 -*-
import subprocess
import random
import socket
import os
import requests
from time import sleep

def Set_tor_url(tor_url):
    b = requests.get('https://qps.ru/api?url='+tor_url)
    return b.text.split('/')[3]

r_pwd = str(random.randint(100000,999999))
output = str(subprocess.check_output(['vnc\\vncpassword.exe', r_pwd], shell=True))[2:-1].split('\\r\\n')[:-1]
pwd=''

for i in output:
    pwd+=str(i)
print('Ваш пароль: '.encode().decode()+r_pwd)


vncini = '[80000001\\Software\\ORL\\WinVNC3]\nSocketConnect=D1\nAutoPortSelect=D0\nPortNumber=D5902\nHTTPPortNumber=D5802\nInputsEnabled=D1\nLocalInputsDisabled=D0\nIdleTimeout=D0\n\
LocalInputsPriorityTime=D3\nQuerySetting=D2\nQueryTimeout=D30\nQueryAccept=D0\nQueryAllowNoPass=D0\nLockSetting=D1\nRemoveWallpaper=D1\nBlankScreen=D0\nEnableFileTransfers=D1\n\
PollUnderCursor=D0\nPollForeground=D1\nPollFullScreen=D0\nOnlyPollConsole=D1\nOnlyPollOnEvent=D0\nPollingCycle=D300\nDontSetHooks=D0\nDontUseDriver=D0\nDriverDirectAccess=D1\n\
LocalInputsPriority=D0\nPassword=B'+pwd+'\nPasswordViewOnly=B'+pwd+'\n[80000002\Software\ORL\WinVNC3]\nConnectPriority=D2\nLoopbackOnly=D0\nEnableHTTPDaemon=D0\nEnableURLParams=D0\n\
AllowLoopback=D1\nAuthRequired=D1\nDebugMode=D0\nDebugLevel=D2\n'

torrc = 'HiddenServiceDir "./Tor/hidden_service/"\nHiddenServicePort 15902 '+socket.gethostname()+':5902\nSocksPort 127.0.0.1:9051 PreferSOCKSNoAuth'

vnc_file = open("vnc\\winvnc.ini", "w")
vnc_file.write(vncini)
vnc_file.close()

tor_file = open("Tor\\torrc", "w")
tor_file.write(torrc)
tor_file.close()

os.system("taskkill /im tor.exe /f >NUL 2>Nul")
os.system("taskkill /im winvnc.exe /f >NUL 2>Nul")

vncstart = subprocess.Popen(['vnc\\winvnc.exe'], shell=True)
torstart = subprocess.Popen(['Tor\\tor.exe','-f','Tor\\torrc','>>Tor\\log.txt'], shell=True)
sleep(3)
tor_host = open("Tor\\hidden_service\\hostname", "r+")
th = tor_host.readlines()[0]
tor_host.close()
while True:
    id_host=Set_tor_url(th[:-1])
    print('\nВаш ID: '.encode().decode() +id_host)
    print('\nВведите "q" для выхода!')
    if str(input()) == 'q':
        os.system("taskkill /im tor.exe /f >NUL 2>Nul")
        os.system("taskkill /im winvnc.exe /f >NUL 2>Nul")
        os.system("start https://hostlip.ru/stati/")
        break
    print('Ваш пароль: '.encode().decode() + r_pwd)
exit(0)