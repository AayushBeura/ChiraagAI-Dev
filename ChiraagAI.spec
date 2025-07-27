# -*- mode: python ; coding: utf-8 -*-
import os
from PyInstaller.utils.hooks import collect_submodules

project_dir = os.path.abspath('.')

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[project_dir],
    binaries=[],
    datas=[
        ('Assets/capturing.mp3', 'Assets'),
        ('Assets/ChiraagAI-Icon.ico', 'Assets'),
        ('Assets/ChiraagAI-Icon.png', 'Assets'),
        ('Assets/logo.png', 'Assets'),
        ('Assets/startup.mp3', 'Assets'),
        ('Assets/startup.mp4', 'Assets'),
        ('config/config_manager.py', 'config'),  # your config module
    ],
    hiddenimports=collect_submodules("google.generativeai"),
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ChiraagAI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False  # Set to True if you want to debug errors in console
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ChiraagAI'
)
