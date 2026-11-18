@echo off
echo ============================================================
echo  DRONEHUB BRASIL - Liberar Porta 8080 no Firewall
echo ============================================================
echo.

REM Remove regra antiga se existir
netsh advfirewall firewall delete rule name="DroneHub 8080" >nul 2>&1

REM Cria regra nova permitindo entrada na porta 8080
netsh advfirewall firewall add rule name="DroneHub 8080" dir=in action=allow protocol=TCP localport=8080

if %errorlevel% == 0 (
    echo.
    echo [OK] Porta 8080 liberada com sucesso!
    echo Agora o celular pode acessar: http://192.168.1.3:8080/marketplace_app.html
) else (
    echo.
    echo [ERRO] Falhou. Execute este arquivo como ADMINISTRADOR.
    echo Clique com botao direito -> "Executar como administrador"
)
echo.
pause
