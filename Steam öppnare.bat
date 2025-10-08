
cd..

cd..

cd..

cd..

cd..

cd steam

start steam.exe

timeout /t 3

@echo off
echo Set objShell = CreateObject("WScript.Shell") > %temp%\popup.vbs
echo objShell.Popup "Tryck ignorera sedan avbryt ner steam konsolen oppnar", 10, "LÄS MIG!", 64 >> %temp%\popup.vbs
start %temp%\popup.vbs

