# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_data = [
    ('src/*', 'src'),
    ('img/*', '.'),
    ('sv_ttk/*', 'sv_ttk'),
    ('sv_ttk/theme/*', 'sv_ttk/theme'),
]

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=added_data,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="PythonYouTubeAudioDownloader",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='img\\icon.ico',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="PythonYouTubeAudioDownloader"
)