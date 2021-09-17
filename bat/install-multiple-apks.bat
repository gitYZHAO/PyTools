@echo off

REM 当前多个apk都是以split的形式安装，导出来后再安装需要输入多个apk包名，此脚本用于安装当前目录下的多个apk文件。
REM 参数1：输入需要安装的APK文件夹路径。
REM       如果没有输入参数，则默认安装bat当前路径下的所有apk文件。
cls
SETLOCAL ENABLEDELAYEDEXPANSION

SET APK_PATH=
SET BLANK= 

IF NOT [%1] == [] (
  CD /d %1
)

:START
ECHO Current path is %cd%
IF NOT "%APK_PATH%"=="" (
  CD /d %APK_PATH%
)

FOR /F %%i IN ('DIR /t/b %cd%') DO (
  REM ECHO %%i
  SET str=%%i
  IF NOT "!str:.apk=!"=="!str!" (
    IF "!str:base.=!"=="!str!" (
      IF "!str:split_config.=!"=="!str!" (
        ECHO FATEL ERROR:Bad apk name "!str!"
        GOTO END
      )
    )
    ECHO Find "!str!" 
    SET M_APK_PATH=!M_APK_PATH!!str!!BLANK!
  )
)

ECHO Check path ...
IF "%M_APK_PATH%"=="" (
  ECHO ERROR : Current path can NOT find apks!
  SET /p APK_PATH=Please input APK path:
  GOTO START
)
ECHO PATHNAME: %M_APK_PATH%
ECHO Start installing ...
adb install-multiple %M_APK_PATH%

:END
@PAUSE