@echo off

set dd=%DATE:~0,2%
set mm=%DATE:~3,2%
set yyyy=%DATE:~6,4%
set curdate=%dd%-%mm%-%yyyy%

rd /s /q _dist
mkdir _dist

rem Coping project dependencies
pipenv lock -r > _dist\reqs.txt
pip3 install -r _dist\reqs.txt --target _dist\ 

rem Coping project files and folders
copy main.py _dist\ /y
xcopy telebot _dist\telebot\ /s /e /y /exclude:build\xcld.txt
xcopy yacloud _dist\yacloud\ /s /e /y /exclude:build\xcld.txt
xcopy wit _dist\wit\ /s /e /y /exclude:build\xcld.txt

rem Delete existing zip
set destzip=build\pack_%curdate%.zip
del %destzip%

rem Create output zip
cd _dist
"C:\Program Files\7-Zip\7z.exe" a -tzip -r0 ..\%destzip% *.*

rem "C:\Program Files\7-Zip\7z.exe" a -tzip -r0 %destzip% %source%main.py
rem "C:\Program Files\7-Zip\7z.exe" a -tzip -r0 -xr!"__pycache__\" %destzip% %source%telebot\
rem "C:\Program Files\7-Zip\7z.exe" a -tzip -r0 -xr!"__pycache__\" %destzip% %source%yacloud\
rem "C:\Program Files\7-Zip\7z.exe" a -tzip -r0 -xr!"__pycache__\" %destzip% %source%wit\
