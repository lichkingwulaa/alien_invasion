# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['D:\\Python\\Python_work\\alien_invasion\\alien_invasion.py'],
             pathex=['alien.py', 'bullet.py', 'button.py', 'game_functions.py', 'game_stats.py', 'scoreboard.py', 'settings.py', 'ship.py', 'D:\\Python\\Python_work\\alien_invasion'],
             binaries=[],
             datas=[],
             hiddenimports=['pygame'],
             hookspath=[],
             runtime_hooks=[],
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
          name='alien_invasion',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='alien_invasion')
