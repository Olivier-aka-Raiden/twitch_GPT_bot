@echo off

REM Vérifier si Python est déjà installé
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Python est déjà installé.
) else (
	REM Télécharger et décompresser l'installateur Python
	powershell -command "& { Invoke-WebRequest https://www.python.org/ftp/python/3.10.10/python-3.10.10-amd64.exe -OutFile python.exe }"
	python.exe /quiet /norestart TargetDir=C:\Python310

	REM Ajouter Python au PATH système
	setx /M PATH "%PATH%;C:\Python310;C:\Python310\Scripts"
	
	del python.exe
)

where pip >nul 2>&1
if %errorlevel% neq 0 (
    echo La commande pip n'est pas accessible dans le PATH.
    exit /b 1
)

REM Installer les bibliothèques Python listées dans le fichier requirements.txt
if not exist requirements.txt (
    echo Le fichier requirements.txt est introuvable.
    exit /b 1
)
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Une erreur s'est produite lors de l'installation des bibliothèques Python.
    exit /b 1
)

REM Lancer le script mon_programme.py
python twitch_chat_bot.py
