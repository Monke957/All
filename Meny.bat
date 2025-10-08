@echo off
title Bernardos meny
chcp 65001 >nul
call :banner

 

:banner 

echo.
echo.
echo              		 [95m███╗   ███╗███████╗ ███╗   ██╗ ██╗   ██╗[0m
echo               		 [95m████╗ ████║██╔════╝████╗  ██║╚██╗ ██╔╝[0m
echo             		 [95m██╔████╔██║█████╗  ██╔██╗ ██║ ╚████╔╝ [0m
echo               		 [95m██║╚██╔╝██║██╔══╝  ██║╚██╗██║  ╚██╔╝  [0m
echo               		 [95m██║ ╚═╝ ██║███████╗██║ ╚████║   ██║ [0m
echo                		 [95m╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝    ╚═╝   [0m
echo.
echo.                                      
      

:ask
echo Vart ska du?
echo  1) skola
echo  2) Gaming
echo  3) Cmd
choice /c 123 /m "Svara:

:: Check response
if errorlevel 3 goto cmd
if errorlevel 2 goto Gaming
if errorlevel 1 goto skola


:skola
start https://online.liber.se
start https://kahoot.it
start https://www.office.com/?auth=2
cd C:\ProgramData\Microsoft\Windows\Start Menu\Programs & start Powerpoint & start word
start https://app.skolon.com/apps/my-collection
start https://km.se/learn/student.php
cls <nul

goto banner


:Gaming

cd..
cd..
cd..
cd..
cd..
cd..
cd Steam
start steam.exe
start https://www.crazygames.se

cls >nul

goto banner

:cmd
cd C:\Users\11EDM001\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools & start cmd.exe & cd.. & cd.. & cd.. & cd..

cls >nul


