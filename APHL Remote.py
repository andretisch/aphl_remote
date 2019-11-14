# -*- coding: utf-8 -*-
import subprocess
import random
import socket
import os
import requests
from time import sleep


def Set_tor_url(tor_url):
    """
    Функция получения URL tor хоста через сокращатель ссылок QPS.RU
    Можно переделать на свой API в будущем.
    :param tor_url: имя тор хоста
    :return: индикатор страницы на qps.ru
    """
    b = requests.get('https://qps.ru/api?url=' + tor_url)
    return b.text.split('/')[3]


def VNC_Pass_gen():
    """
    Генерация пароля VNC и его файла настроек
    :return:
    """
    r_pwd = str(random.randint(100000, 999999))
    output = str(subprocess.check_output(['vnc\\vncpassword.exe', r_pwd], shell=True))[2:-1].split('\\r\\n')[:-1]
    pwd = ''
    for i in output:
        pwd += str(i)
    vncini = '[80000001\\Software\\ORL\\WinVNC3]\nSocketConnect=D1\nAutoPortSelect=D0\nPortNumber=D5902\nHTTPPortNumber=D5802\nInputsEnabled=D1\nLocalInputsDisabled=D0\nIdleTimeout=D0\n\
    LocalInputsPriorityTime=D3\nQuerySetting=D2\nQueryTimeout=D30\nQueryAccept=D0\nQueryAllowNoPass=D0\nLockSetting=D1\nRemoveWallpaper=D1\nBlankScreen=D0\nEnableFileTransfers=D1\n\
    PollUnderCursor=D0\nPollForeground=D1\nPollFullScreen=D0\nOnlyPollConsole=D1\nOnlyPollOnEvent=D0\nPollingCycle=D300\nDontSetHooks=D0\nDontUseDriver=D0\nDriverDirectAccess=D1\n\
    LocalInputsPriority=D0\nPassword=B' + pwd + '\nPasswordViewOnly=B' + pwd + '\n[80000002\Software\ORL\WinVNC3]\nConnectPriority=D2\nLoopbackOnly=D0\nEnableHTTPDaemon=D0\nEnableURLParams=D0\n\
    AllowLoopback=D1\nAuthRequired=D1\nDebugMode=D0\nDebugLevel=D2\n'
    vnc_file = open("vnc\\winvnc.ini", "w")
    vnc_file.write(vncini)
    vnc_file.close()
    return r_pwd


def Tor_rc_gen():
    """
    Файл настроек TOR
    :return:
    """
    torrc = 'HiddenServiceDir "./Tor/hidden_service/"\nHiddenServicePort 15902 ' + socket.gethostname() + ':5902\nSocksPort 127.0.0.1:9051 PreferSOCKSNoAuth'
    tor_file = open("Tor\\torrc", "w")
    tor_file.write(torrc)
    tor_file.close()
    return socket.gethostname()

def Start_Services():
    """
    Запуск Vnc и Tor с проверкой.
    :return:
    """
    os.system("taskkill /im tor.exe /f >NUL 2>Nul")
    os.system("taskkill /im winvnc.exe /f >NUL 2>Nul")
    subprocess.Popen(['vnc\\winvnc.exe'], shell=True)
    subprocess.Popen(['Tor\\tor.exe', '-f', 'Tor\\torrc', '>>Tor\\log.txt'], shell=True)
    print("Запуcr через ...".encode().decode(), end='')
    i = 10
    while i != 0:
        print(' '.encode().decode() + str(i), end='')
        sleep(1)
        i -= 1
    tor_host = open("Tor\\hidden_service\\hostname", "r+")
    th = tor_host.readlines()[0]
    tor_host.close()
    return th


def Play_The_Game():
    """
    Ну и понеслась сама программа
    :return:
    """
    r_pwd = VNC_Pass_gen()
    localhostname = Tor_rc_gen()
    print('Имя компьютера: '.encode().decode() + localhostname)
    print('Ваш пароль: '.encode().decode() + r_pwd)
    tor_hostname = Start_Services()
    id_host = Set_tor_url(tor_hostname[:-1])
    while True:
        print('\nВаш ID: '.encode().decode() + id_host)
        print('\nВведите "q" для выхода!'.encode().decode())
        if str(input()) == 'q':
            os.system("taskkill /im tor.exe /f >NUL 2>Nul")
            os.system("taskkill /im winvnc.exe /f >NUL 2>Nul")
            os.system("start https://hostlip.ru/stati/")
            break
        else:
            print('\nЭто не "q"'.encode().decode())
    exit(0)

if __name__ == "__main__":
    Play_The_Game()