pip install requests
pip install opencv-python
pip install pyinstaller
pip install serial
cd ..
pyinstaller --onefile prueba.py
rmdir /s /q build
cd dist
move "prueba.exe" "..\"
cd ..
rmdir /s /q dist
del prueba.spec
