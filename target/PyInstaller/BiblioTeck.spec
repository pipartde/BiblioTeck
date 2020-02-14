# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['/Users/denispipart/Desktop/job_etude/biblioteck/src/main/python/main.py'],
             pathex=['/Users/denispipart/Desktop/job_etude/biblioteck/target/PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['/Users/denispipart/Desktop/job_etude/venv/lib/python3.7/site-packages/fbs/freeze/hooks'],
             runtime_hooks=['/Users/denispipart/Desktop/job_etude/biblioteck/target/PyInstaller/fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='BiblioTeck',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='/Users/denispipart/Desktop/job_etude/biblioteck/target/Icon.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               upx_exclude=[],
               name='BiblioTeck')
app = BUNDLE(coll,
             name='BiblioTeck.app',
             icon='/Users/denispipart/Desktop/job_etude/biblioteck/target/Icon.icns',
             bundle_identifier=None)
