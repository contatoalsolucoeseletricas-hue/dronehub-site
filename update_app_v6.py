# -*- coding: utf-8 -*-
import sys, re

file_path = r'C:\DRONE\marketplace_app.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print(f'Original size: {len(content)} chars')
