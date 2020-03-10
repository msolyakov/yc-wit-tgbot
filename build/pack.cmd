@echo off

set dd=%DATE:~0,2%
set mm=%DATE:~3,2%
set yyyy=%DATE:~6,4%
set curdate=%dd%-%mm%-%yyyy%

rd /s /q dist
mkdir dist

rem Coping project dependencies
pipenv lock -r > dist\reqs.txt
pip3 install -r dist\reqs.txt --target dist\ 

rem Coping project files and folders
copy main.py dist\ /y
xcopy telebot dist\telebot\ /s /e /y /exclude:build\xcld.txt
xcopy yacloud dist\yacloud\ /s /e /y /exclude:build\xcld.txt
xcopy wit dist\wit\ /s /e /y /exclude:build\xcld.txt

rem Delete existing zip
set destzip=build\pack_%curdate%.zip
del %destzip%

rem Create output zip
cd dist
"C:\Program Files\7-Zip\7z.exe" a -tzip -r0 ..\%destzip% *.*

rem "C:\Program Files\7-Zip\7z.exe" a -tzip -r0 %destzip% %source%main.py
rem "C:\Program Files\7-Zip\7z.exe" a -tzip -r0 -xr!"__pycache__\" %destzip% %source%telebot\
rem "C:\Program Files\7-Zip\7z.exe" a -tzip -r0 -xr!"__pycache__\" %destzip% %source%yacloud\
rem "C:\Program Files\7-Zip\7z.exe" a -tzip -r0 -xr!"__pycache__\" %destzip% %source%wit\
