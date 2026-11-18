# -*- coding: utf-8 -*-
import os, sys, subprocess, winreg, shutil

print("--- INICIANDO OTIMIZAÇÃO DO WINDOWS ---")

# 1. Desativar Hibernação
try:
    res = subprocess.run(["powercfg", "-h", "off"], capture_output=True, text=True)
    if res.returncode == 0:
        print("[OK] Hibernação desativada com sucesso! (hiberfil.sys removido)")
    else:
        print("[INFO] powercfg retorno:", res.stderr.strip() or res.stdout.strip())
except Exception as e:
    print("[ERRO] Falha ao desativar hibernacao:", e)

# 2. Impedir o Windows Update de reiniciar sozinho com usuário logado
try:
    key_path = r"SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU"
    with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
        winreg.SetValueEx(key, "NoAutoRebootWithLoggedOnUsers", 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(key, "AUOptions", 0, winreg.REG_DWORD, 2) # Notificar antes de baixar
    print("[OK] Politica aplicada: Windows NUNCA reiniciara sozinho com usuario conectado!")
except Exception as e:
    print("[INFO] Registro WindowsUpdate:", e)

# 3. Desativar Otimização de Entrega P2P (Não gastar internet nem disco enviando atualizações)
try:
    key_path = r"SOFTWARE\Policies\Microsoft\Windows\DeliveryOptimization"
    with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
        winreg.SetValueEx(key, "DODownloadMode", 0, winreg.REG_DWORD, 0) # 0 = Desativado P2P
    print("[OK] Otimizacao de Entrega P2P desativada (Windows nao usara sua internet para terceiros)!")
except Exception as e:
    print("[INFO] Registro DeliveryOptimization:", e)

# 4. Desativar anúncios e sugestões na tela de bloqueio e menu Iniciar
try:
    cdm_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager"
    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, cdm_path) as key:
        winreg.SetValueEx(key, "SubscribedContent-338387Enabled", 0, winreg.REG_DWORD, 0)
        winreg.SetValueEx(key, "SubscribedContent-338388Enabled", 0, winreg.REG_DWORD, 0)
        winreg.SetValueEx(key, "SubscribedContent-338389Enabled", 0, winreg.REG_DWORD, 0)
        winreg.SetValueEx(key, "SubscribedContent-310093Enabled", 0, winreg.REG_DWORD, 0)
        winreg.SetValueEx(key, "RotatingLockScreenEnabled", 0, winreg.REG_DWORD, 0)
        winreg.SetValueEx(key, "RotatingLockScreenOverlayEnabled", 0, winreg.REG_DWORD, 0)
        winreg.SetValueEx(key, "SystemPaneSuggestionsEnabled", 0, winreg.REG_DWORD, 0)
    print("[OK] Anuncios, dicas e propagandas na tela de bloqueio e Iniciar desativados!")
except Exception as e:
    print("[INFO] Registro ContentDeliveryManager:", e)

# 5. Limpar arquivos temporários com segurança
temp_folders = [
    os.environ.get("TEMP"),
    r"C:\Windows\Temp"
]

cleaned_bytes = 0
for folder in temp_folders:
    if not folder or not os.path.exists(folder):
        continue
    for root, dirs, files in os.walk(folder, topdown=False):
        for name in files:
            p = os.path.join(root, name)
            try:
                sz = os.path.getsize(p)
                os.remove(p)
                cleaned_bytes += sz
            except Exception:
                pass
        for name in dirs:
            p = os.path.join(root, name)
            try:
                shutil.rmtree(p, ignore_errors=True)
            except Exception:
                pass

print(f"[OK] Cache e temporarios limpos: {cleaned_bytes / (1024**2):.1f} MB liberados!")
print("--- OTIMIZACAO CONCLUIDA ---")
