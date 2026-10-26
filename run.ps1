Write-Host "Activando entorno virtual..." -ForegroundColor Green
& ".\.venv\Scripts\Activate.ps1"

Write-Host "Ejecutando Calculadora de Tablas de Verdad y Lógica Difusa..." -ForegroundColor Green
python main.py

Read-Host "Presione ENTER para salir"
