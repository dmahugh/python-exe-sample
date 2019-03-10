# -*- mode: python -*-

block_cipher = None


a = Analysis(['cli.py'],
             pathex=['C:\\Users\\dmahugh\\Dropbox\\Python\\python-exe-sample'],
             binaries=[],
             datas=[('venv\\Lib\\site-packages\\importlib_resources\\version.txt', 'importlib_resources'), ('opcreader\\config.json', 'opcreader')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['pytest'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='opcinfo',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
