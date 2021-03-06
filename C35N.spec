# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

SETUP_DIR = 'C:\\MyProject\\C35N\\'

a = Analysis(['C35N.py',
              'DBDocument.py',
              'img_rc.py',
              'PDFWidget.py',
              'ComicBook.py',
              'DBView.py',
              'C:\\MyProject\\C35N\\UI\\UI_BookDetail.py',
              'C:\\MyProject\\C35N\\UI\\UI_ComicBook.py',
              'C:\\MyProject\\C35N\\UI\\UI_ConferencePaperDetail.py',
              'C:\\MyProject\\C35N\\UI\\UI_DBSourceWindow.py',
              'C:\\MyProject\\C35N\\UI\\UI_DBTreeMain.py',
              'C:\\MyProject\\C35N\\UI\\UI_DissertationDetail.py',
              'C:\\MyProject\\C35N\\UI\\UI_Dlgabout.py',
              'C:\\MyProject\\C35N\\UI\\UI_MainWindow.py',
              'C:\\MyProject\\C35N\\UI\\UI_PeriodicalDetail.py',
              'C:\\MyProject\\C35N\\UI\\UI_ReadPDF.py',
              'C:\\MyProject\\C35N\\UI\\UI_SongBook.py',
              'C:\\MyProject\\C35N\\UI\\UI_SouthSoundOperaDetail.py',
              'C:\\MyProject\\C35N\\UI\\UI_TraditionalOperaDetail.py',
              ],
             pathex=['C:\\MyProject\\C35N'],
             binaries=[],
             datas=[(SETUP_DIR+'DB\\','DB\\')],
             hiddenimports=['sys','os','fitz','queue','PyQt5','threading','tempfile','win32api','win32print'],
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
          name='C35N',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,icon='cs2.ico' )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='C35N')
