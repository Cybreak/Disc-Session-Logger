@echo off


pip install -r requirements.txt
pyinstaller main.py --onefile
copy dist\main.exe .\
del dist\main.exe
rmdir dist
del /s /q build
rmdir build\main\localpycs
rmdir build\main
rmdir build
del main.spec
ren .\main.exe SL.exe
pause