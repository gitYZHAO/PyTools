@echo off

cls
SETLOCAL ENABLEDELAYEDEXPANSION
SET BLANK= 

echo Current path is %cd%

FOR /F %%i IN ('DIR /t/b %cd%') DO (
  REM ECHO %%i
  SET str=%%i
  IF NOT "!str:.apk=!"=="!str!" ( 
    ECHO Find "!str!" 
    SET M_APK_PATH=!M_APK_PATH!!str!!BLANK!
  )
)

ECHO PATHNAME='%M_APK_PATH%'
adb install-multiple %M_APK_PATH%

@PAUSE