@echo off

ipconfig
systeminfo

:: Simulate Ctrl+A (Select All)
powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys('^{A}')"

:: Simulate Ctrl+C (Copy)
powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys('^{C}')"

:: Navigate to the Info_grabber directory
cd ..\..\..\..\..\..\Info_grabber

:: Open info_grabber_paste.txt
start info_grabber_paste.txt >nul

timeout /t 2

powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys('~')
:: Wait for a few seconds
timeout /t 3

:: Simulate Ctrl+V (Paste)
powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys('^{V}')"

:: Simulate Ctrl+S (Save)
powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys('^{S}')"

timeout /t 2

powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys('~')"

powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys('{LEFT}')"

powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys('~')"

timeout /t 2

cd..

start .

:: Simulate Ctrl+A (Select All)
powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys('^{A}')"


pause

taskkill /IM notepad.exe /F

powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.SendKeys('%{F4}')"

exit
