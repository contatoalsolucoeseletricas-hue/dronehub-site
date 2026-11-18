@echo off
net session >nul 2>&1
if %errorLevel% neq 0 (
    powershell -Command "Start-Process 'C:\DRONE\otimizar.bat' -Verb RunAs"
    exit /b
)

echo Executando otimizacao como Administrador...
powercfg -h off
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU" /v NoAutoRebootWithLoggedOnUsers /t REG_DWORD /d 1 /f
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU" /v AUOptions /t REG_DWORD /d 2 /f
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DeliveryOptimization" /v DODownloadMode /t REG_DWORD /d 0 /f

echo SUCESSO > C:\DRONE\otimizado_status.txt
echo ============================================================
echo   TUDO CONCLUIDO! ESPACO LIBERADO NO SSD COM SUCESSO!
echo ============================================================
pause
