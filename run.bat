@echo off
echo Activando entorno virtual...
call .venv\Scripts\activate

echo Ejecutando Calculadora de Tablas de Verdad y Lógica Difusa...
python main.py

pause
