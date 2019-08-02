import subprocess
import requests


while True:
    print('Введите ID: '.encode().decode())
    ID = str(input())
    id_id = requests.get('http://aphl.ru:19191/id='+ID+'&user=123123')
    remote_host = id_id.text
    print(remote_host)
    if ID !='':
        subprocess.Popen(['vnc\\VNC-Viewer.exe',remote_host+':15902','-ProxyServer','socks://127.0.0.1:9051','2>Nul'], shell=True)
    else:
        pass