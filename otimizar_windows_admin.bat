@echo off
chcp 65001 >nul

:: Auto-elevação para Administrador automática
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo ============================================================
    echo   Solicitando permissao de Administrador ao Windows...
    echo ============================================================
    powershell -Command "Start-Process '%~dpnx0' -Verb RunAs"
    exit /b
)

echo ============================================================
echo   OTIMIZADOR DO WINDOWS - DRONEHUB (MODO ADMINISTRADOR)
echo ============================================================
echo.

REM 1. Desativar a Hibernação e apagar hiberfil.sys
echo [*] Desativando Hibernação (apagando hiberfil.sys do SSD)...
powercfg -h off
echo [OK] Hibernacao desativada com sucesso!

REM 2. Impedir o Windows Update de reiniciar sozinho com usuário conectado
echo.
echo [*] Bloqueando reinicio automatico do Windows Update...
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU" /v NoAutoRebootWithLoggedOnUsers /t REG_DWORD /d 1 /f
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU" /v AUOptions /t REG_DWORD /d 2 /f
echo [OK] O Windows NUNCA mais reiniciara sozinho enquanto você estiver usando o PC!

REM 3. Desativar Otimização de Entrega P2P
echo.
echo [*] Desativando envio de atualizacoes para terceiros (P2P)...
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DeliveryOptimization" /v DODownloadMode /t REG_DWORD /d 0 /f
echo [OK] Otimizacao de Entrega P2P desativada. Sua internet nao sera consumida!

echo.
echo ============================================================
echo   SUCESSO! ESPACO LIBERADO E WINDOWS OTIMIZADO!
echo ============================================================
echo.
echo Pode fechar esta janela pressionando qualquer tecla.
pause >nul
