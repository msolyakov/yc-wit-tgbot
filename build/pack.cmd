@echo off

set source="..\yc-wit-tgbot\"
set destination="..\yc-wit-tgbot\build"
set %exclus%="..\yc-wit-tgbot\exclus.txt"
set dd=%DATE:~0,2%
set mm=%DATE:~3,2%
set yyyy=%DATE:~6,4%
set curdate=%dd%-%mm%-%yyyy%
set destzip=%destination%\pack_%curdate%.zip

del %destzip%

"C:\Program Files\7-Zip\7z.exe" a -tzip -r0 %destzip% %source%\main.py
"C:\Program Files\7-Zip\7z.exe" a -tzip -r0 -xr!"__pycache__\" %destzip% %source%\telebot\
"C:\Program Files\7-Zip\7z.exe" a -tzip -r0 -xr!"__pycache__\" %destzip% %source%\yacloud\
"C:\Program Files\7-Zip\7z.exe" a -tzip -r0 -xr!"__pycache__\" %destzip% %source%\wit\
