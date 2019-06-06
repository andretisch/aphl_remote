import subprocess
import random
import socket

r_pwd = str(random.randint(100000,999999))
output = subprocess.check_output(['vnc\\vncpassword.exe', r_pwd], shell=True).split('\r\n')
pwd=''

for i in output:
    pwd+=str(i)
print pwd,r_pwd


vncini = '[80000001\\Software\\ORL\\WinVNC3]\nSocketConnect=D1\nAutoPortSelect=D0\nPortNumber=D5902\nHTTPPortNumber=D5802\nInputsEnabled=D1\nLocalInputsDisabled=D0\nIdleTimeout=D0\n\
LocalInputsPriorityTime=D3\nQuerySetting=D2\nQueryTimeout=D30\nQueryAccept=D0\nQueryAllowNoPass=D0\nLockSetting=D1\nRemoveWallpaper=D1\nBlankScreen=D0\nEnableFileTransfers=D1\n\
PollUnderCursor=D0\nPollForeground=D1\nPollFullScreen=D0\nOnlyPollConsole=D1\nOnlyPollOnEvent=D0\nPollingCycle=D300\nDontSetHooks=D0\nDontUseDriver=D0\nDriverDirectAccess=D1\n\
LocalInputsPriority=D0\nPassword=B'+pwd+'\nPasswordViewOnly=B'+pwd+'\n[80000002\Software\ORL\WinVNC3]\nConnectPriority=D2\nLoopbackOnly=D0\nEnableHTTPDaemon=D0\nEnableURLParams=D0\n\
AllowLoopback=D1\nAuthRequired=D1\nDebugMode=D0\nDebugLevel=D2\n'

torrc = 'HiddenServiceDir "./hidden_service/"\nHiddenServicePort 15902 '+socket.gethostname()+':5902'

vnc_file = open("vnc\\winvnc.ini", "w")
vnc_file.write(vncini)
vnc_file.close()

tor_file = open("Tor\\torrc", "w")
tor_file.write(torrc)
tor_file.close()

import os
os.system("taskkill /im tor.exe")

#vncstart = subprocess.Popen(['vnc\\winvnc.exe'], shell=True)
#torstart = subprocess.Popen(['Tor\\tor.exe','-f','torrc'], shell=True)

tor_host = open("Tor\\hidden_service\\hostname", "r")
print tor_host.read()
tor_host.close()
#vncstart.wait()