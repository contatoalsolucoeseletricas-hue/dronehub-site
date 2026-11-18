@echo off
title DroneHub Brasil - Servidor de Testes
cd /d C:\DRONE
echo =======================================================
echo    INICIANDO DRONEHUB BRASIL (PROJETO PILOTO)
echo =======================================================
echo.
start http://localhost:8080/marketplace_app.html
python server.py
pause
