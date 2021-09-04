@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

SET APK_PACKAGE_NAME=

IF NOT [%1] == [] (
  SET APK_PACKAGE_NAME=%1
  GOTO START
)

SET /p APK_PACKAGE_NAME=Please input the package name:

:START

ECHO Now to get %APK_PACKAGE_NAME% 's APK ...
MKDIR %APK_PACKAGE_NAME%

FOR /f "delims=" %%i in ('adb shell pm path %APK_PACKAGE_NAME%') do (
  REM ECHO %%i
  SET str=%%i
  SET str=!str:package:=!
  ECHO !str!
  adb pull !str! %APK_PACKAGE_NAME%
)

:END
@PAUSE