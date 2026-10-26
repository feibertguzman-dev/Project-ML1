# Calculadora de Tablas de Verdad y Lógica Difusa

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B?logo=streamlit&logoColor=white)
![Estado](https://img.shields.io/badge/Estado-Educativo-brightgreen)
![IA](https://img.shields.io/badge/Fundamentos-IA-orange)
![Lógica](https://img.shields.io/badge/Lógica-Clásica%20%7C%20Difusa-blueviolet)
![Plataforma](https://img.shields.io/badge/Plataforma-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![Licencia](https://img.shields.io/badge/Licencia-MIT-informational)

## ENTREGABLES:

1. Enlace a Landing Page: https://feibertguzman-dev.github.io/Project-ML1/
2. Enlace a Streamlit: https://project-ml1.streamlit.app/
3. Enlace a la documentación: https://github.com/feibertguzman-dev/Project-ML1/tree/main/docs

## Descripción

Este proyecto tiene como objetivo explicar, de manera práctica e interactiva, dos fundamentos básicos de la **Introducción a la Inteligencia Artificial**:

- **Lógica Proposicional Clásica**: Se basa en el principio de bivalencia, donde una proposición solo puede ser **Verdadera (True)** o **Falsa (False)**.
- **Lógica Difusa (Fuzzy Logic)**: Permite trabajar con grados de verdad en el intervalo **[0, 1]**, lo cual resulta útil para representar conceptos imprecisos propios del razonamiento humano.

Mediante esta aplicación web interactiva desarrollada con **Streamlit**, se pueden generar tablas de verdad y visualizar ejemplos sencillos de **conjuntos difusos** y **operadores difusos**.

## 🎯 Objetivos

- Comprender el funcionamiento de las tablas de verdad.
- Diferenciar entre lógica clásica y lógica difusa.
- Aplicar los conectivos lógicos: Negación (¬), Conjunción (∧), Disyunción (∨) y Bicondicional (↔).
- Entender el concepto de función de pertenencia y los operadores MIN, MAX y complemento.
- Identificar la utilidad de la lógica difusa en sistemas de Inteligencia Artificial.

## 🚀 Demo en Vivo

- **Aplicación Streamlit**: [Ejecutar localmente con `streamlit run app.py`](#cómo-ejecutar)
- **Landing Page (GitHub Pages)**: [Ver landing page](index.html)

## 📁 Estructura del Proyecto

```text
Calculadora_Tablas_Verdad_Logica_Difusa/
├── app.py                    # Aplicación principal con Streamlit
├── index.html                # Landing page para GitHub Pages
├── main.py                   # Versión CLI (consola) - Mantenida para referencia
├── logica_clasica.py         # Módulo con tablas de verdad
├── logica_difusa.py          # Módulo con ejemplos de lógica difusa
├── requirements.txt          # Dependencias del proyecto
├── README.md                 # Documentación del proyecto
├── .gitignore                # Archivos a ignorar por Git
├── run.bat                   # Script para ejecutar CLI en Windows (CMD)
├── run.ps1                   # Script para ejecutar CLI en Windows (PowerShell)
└── docs/                     # Documentación complementaria
    ├── README.md             # Índice de documentación
    ├── teoria_logica_clasica.md
    ├── teoria_logica_difusa.md
    ├── uso_aplicacion.md
    └── evidencia/            # Evidencias del desarrollo
```

## 📋 Requisitos

- **Python 3.8+** (Recomendado: 3.10 o superior)
- **Streamlit** >= 1.28.0
- **Pandas** >= 2.0.0

## 🔧 Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/Calculadora_Tablas_Verdad_Logica_Difusa.git
cd Calculadora_Tablas_Verdad_Logica_Difusa
```

### 2. Crear y activar entorno virtual

**Windows (CMD):**
```cmd
python -m venv .venv
.venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux/macOS:**
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Desactivar entorno virtual

```bash
deactivate
```

## ▶️ Cómo ejecutar

### Opción 1: Aplicación Web con Streamlit (Recomendada)

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

### Opción 2: Versión CLI (Consola)

#### Con script automático (Windows CMD)
```cmd
run.bat
```

#### Con script automático (Windows PowerShell)
```powershell
.\run.ps1
```

#### Manualmente (con entorno virtual activado)
```bash
python main.py
```

## 💡 Características de la Aplicación Streamlit

- **🏠 Inicio**: Vista general del proyecto con objetivos y características
- **📊 Lógica Clásica**: Tablas de verdad interactivas para Negación, Conjunción, Disyunción y Bicondicional
- **🌊 Lógica Difusa**: 
  - Clasificación difusa de temperatura con sliders interactivos
  - Operadores difusos AND, OR, NOT con valores personalizables
  - Aplicaciones reales de lógica difusa en IA
- **📚 Documentación y Evidencia**: Pestaña integrada con teoría, manual de uso y evidencias del desarrollo
- **ℹ️ Acerca del Proyecto**: Información teórica, autor y tecnologías utilizadas

## 📚 Documentación

La carpeta [`docs/`](docs/) contiene documentación complementaria:

- **[Teoría Lógica Clásica](docs/teoria_logica_clasica.md)**: Fundamentos y conectivos lógicos
- **[Teoría Lógica Difusa](docs/teoria_logica_difusa.md)**: Conjuntos difusos, funciones de pertenencia y operadores
- **[Manual de Uso](docs/uso_aplicacion.md)**: Guía detallada de uso de la aplicación
- **[Evidencia](docs/evidencia/)**: Capturas y registros del desarrollo

## 🌐 Despliegue

### GitHub Pages (Landing Page)
La landing page `index.html` se encuentra en la raíz del repositorio y está lista para ser publicada en GitHub Pages.

Para publicar:
1. Ir a Settings > Pages en tu repositorio
2. Seleccionar Source: "Deploy from a branch"
3. Seleccionar Branch: `main` / `master` y carpeta `/ (root)`
4. Guardar y esperar el despliegue

### Streamlit Community Cloud
Para desplegar la aplicación Streamlit:

1. Subir el repositorio a GitHub
2. Ir a [share.streamlit.io](https://share.streamlit.io)
3. Conectar con GitHub y seleccionar el repositorio
4. Configurar: Main file path = `app.py`
5. Desplegar

## 🎓 Conclusión

Este proyecto permite visualizar la diferencia fundamental entre ambos enfoques: **la lógica clásica responde con un "sí" o "no"**, mientras que **la lógica difusa responde con "¿qué tan cierto?"**. Esta distinción es clave para entender por qué la lógica difusa se ha vuelto una herramienta importante en el desarrollo de sistemas inteligentes más cercanos al razonamiento humano.

## 👨‍💻 Autor

Proyecto académico para la asignatura **Introducción a la Inteligencia Artificial**.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
