# -*- coding: utf-8 -*-
import subprocess, time, sys

print("Iniciando Cloudflare Tunnel com Keep-Alive...")
cmd = [r"C:\DRONE\cloudflared.exe", "tunnel", "--protocol", "http2", "--no-autoupdate", "--url", "http://127.0.0.1:8080"]

while True:
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
    for line in iter(p.stdout.readline, ''):
        sys.stdout.write(line)
        sys.stdout.flush()
    p.wait()
    time.sleep(2)
