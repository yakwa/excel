@echo off
echo ========================================
echo   Le Robinet des Intelligences
echo   Site Vitrine - Lancement
echo ========================================
echo.

echo Installation des dependances...
pip install -r requirements.txt

echo.
echo Lancement du serveur Flask...
echo Le site sera accessible sur: http://localhost:5000
echo.
echo Appuyez sur Ctrl+C pour arreter le serveur
echo ========================================

python app.py

pause
