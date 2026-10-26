# Manual de Uso de la Aplicación

## Introducción

Esta guía te ayudará a utilizar tanto la **aplicación web con Streamlit** como la **versión CLI (consola)** de la Calculadora de Tablas de Verdad y Lógica Difusa.

## Opción 1: Aplicación Web con Streamlit (Recomendada)

### Requisitos Previos

- Python 3.8 o superior
- Entorno virtual activado
- Dependencias instaladas (`streamlit`, `pandas`)

### Ejecución

1. Abrir terminal en la carpeta del proyecto
2. Activar entorno virtual
3. Ejecutar el comando:

```bash
streamlit run app.py
```

4. La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

### Navegación por la Aplicación

#### 🏠 Inicio
Vista general con:
- Descripción del proyecto
- Objetivos
- Características principales
- Diferencia entre lógica clásica y lógica difusa

#### 📊 Lógica Clásica
Permite generar tablas de verdad interactivas:

1. Selecciona el conectivo lógico desde el desplegable:
   - Negación (¬p)
   - Conjunción (p ∧ q)
   - Disyunción (p ∨ q)
   - Bicondicional (p ↔ q)
2. La tabla se genera automáticamente mostrando todos los casos posibles
3. Se incluye una interpretación del resultado

#### 🌊 Lógica Difusa
Tres ejemplos interactivos:

**a) Clasificación difusa de temperatura**
1. Usa el slider para seleccionar una temperatura en °C (-5 a 40)
2. Presiona "Calcular pertenencias"
3. Observa los grados de pertenencia a FRÍO, TEMPLADO y CALIENTE
4. Se muestra la sensación predominante y posibles traslapes

**b) Operadores difusos (AND, OR, NOT)**
1. Ajusta los sliders para mu(A) y mu(B) en el rango [0, 1]
2. Presiona "Aplicar operadores"
3. Visualiza los resultados de AND (min), OR (max), NOT A y NOT B
4. Lee las interpretaciones con lenguaje natural

**c) Aplicaciones en Inteligencia Artificial**
Muestra una tabla con aplicaciones reales de lógica difusa en diversos campos.

#### 📚 Documentación y Evidencia
Cuatro pestañas:

- **Teoría**: Comparación entre lógica clásica y lógica difusa
- **Manual de Uso**: Guía rápida de uso
- **Evidencia**: Registro de actividades de desarrollo
- **Archivos de Docs**: Listado de archivos en la carpeta docs/

#### ℹ️ Acerca del Proyecto
Información sobre:
- Fundamentos teóricos
- Temas abordados
- Base teórica (Lotfi A. Zadeh)
- Autor y tecnologías utilizadas

## Opción 2: Versión CLI (Consola)

### Ejecución en Windows

**Con run.bat:**
```cmd
run.bat
```

**Con run.ps1 (PowerShell):**
```powershell
.\run.ps1
```

**Manual:**
```bash
python main.py
```

### Menú Principal

```
=== CALCULADORA DE TABLAS DE VERDAD Y LÓGICA DIFUSA ===
     Fundamentos de Introducción a la Inteligencia Artificial
===============================================================

1. Tablas de Verdad (Lógica Clásica)
2. Lógica Difusa (Ejemplos prácticos)
3. Acerca del proyecto
4. Salir

Seleccione una opción (1-4):
```

### Submenús

**Lógica Clásica (Opción 1):**
1. Negación (¬p)
2. Conjunción (p ∧ q)
3. Disyunción (p ∨ q)
4. Bicondicional (p ↔ q)
5. Volver al menú principal

**Lógica Difusa (Opción 2):**
1. Ejemplo: Clasificación difusa de temperatura (°C)
2. Ejemplo: Operadores difusos AND, OR y COMPLEMENTO
3. Aplicaciones de lógica difusa en Inteligencia Artificial
4. Volver al menú principal

## Consejos de Uso

### Para aprender lógica clásica
- Comienza con la negación para entender el principio básico
- Practica con conjunción y disyunción
- El bicondicional es el más sutil, presta especial atención

### Para aprender lógica difusa
- Experimenta con diferentes temperaturas para ver los traslapes
- Prueba diferentes valores de mu(A) y mu(B) en los operadores
- Observa cómo con valores intermedios se obtienen resultados más realistas
- Lee las aplicaciones para entender la utilidad práctica

## Solución de Problemas

### Error al ejecutar streamlit
```bash
pip install --upgrade streamlit pandas
```

### Error de codificación en Windows
La aplicación ya incluye manejo de codificación UTF-8. Si persiste, usa PowerShell o Windows Terminal.

### Puerto ocupado
Si el puerto 8501 está ocupado:
```bash
streamlit run app.py --server.port 8502
```

## Recursos Adicionales

- [Documentación oficial de Streamlit](https://docs.streamlit.io/)
- [Teoría de Lógica Difusa - Zadeh](https://doi.org/10.1016/S0019-9958(65)90241-X)
- [Landing Page del Proyecto](../index.html)
- [Repositorio GitHub](#)

---

*Proyecto académico - Introducción a la Inteligencia Artificial*
