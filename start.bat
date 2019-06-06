@echo off
title I am a Man!!!
cd Tor
echo HiddenServiceDir "./hidden_service/" > torrc
echo HiddenServicePort 15902 %computername%:5902>> torrc
echo SocksPort 9150 KeepAliveIsolateSOCKSAuth PreferSOCKSNoAuth>> torrc
pause
set $tor="tor.exe -f torrc"
start "" "%$tor%"
cd hidden_service
for /f "" %%i in ('findstr onion hostname') do set hn_onion=%%i
echo %hn_onion%
pause
taskkill /im "tor.exe" /t>nul