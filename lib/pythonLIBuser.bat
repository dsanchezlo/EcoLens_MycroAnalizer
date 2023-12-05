pip install requests
pip install opencv-python
pip install pyinstaller
pip install serial
cd ..
pyinstaller --onefile --icon=images/icon-simple.ico Ecolens_Mycroanalizer.py
rmdir /s /q build
cd dist
move "Ecolens_Mycroanalizer.exe" "..\"
cd ..
rmdir /s /q dist
del Ecolens_Mycroanalizer.spec
