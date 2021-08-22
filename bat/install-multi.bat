@echo off

REM 当前多个apk都是以split的形式安装，导出来后再安装需要输入多个apk包名，此脚本用于安装当前目录下的多个apk文件。
REM 参数1：输入需要安装的APK文件夹路径。
REM       如果没有输入参数，则默认安装bat当前路径下的所有apk文件。
cls
SETLOCAL ENABLEDELAYEDEXPANSION
SET BLANK= 

IF NOT [%1] == [] (
  CD %1
)
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
IF '%M_APK_PATH%'=='' (
  ECHO Error: Can not fine the apks!
  GOTO END
)

adb install-multiple %M_APK_PATH%

:END
@PAUSE