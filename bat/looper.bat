@echo off
cls
rem show current path
echo %cd%

:start

::do something

echo wait 5s
ping -n 5 127.0.0.1 > nul
goto start