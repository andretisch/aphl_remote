import subprocess
import requests

def Get_tor_url(tor_url):
    a = requests.get('https://qps.ru/'+tor_url)
    return a.text.split('url=')[1].split('"')[0].split('//')[1]
while True:
    print('Введите ID: '.encode().decode())
    ID = str(input())
    remote_host = Get_tor_url(ID)
    print(remote_host)
    if ID !='':
        subprocess.Popen(['vnc\\VNC-Viewer.exe',remote_host+':15902','-ProxyServer','socks://127.0.0.1:9051','2>Nul'], shell=True)
    else:
        pass
        pass