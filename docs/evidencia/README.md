# Evidencia del Desarrollo

Esta carpeta contiene las evidencias del proceso de desarrollo de la **Calculadora de Tablas de Verdad y Lógica Difusa**.

## Registro de Actividades

| Fecha | Etapa | Actividad | Resultado |
|-------|-------|-----------|-----------|
| Desarrollo Inicial | Planificación | Análisis de requerimientos del proyecto académico | Completado |
| Desarrollo Inicial | Implementación | Creación de `logica_clasica.py` con tablas de verdad | Completado |
| Desarrollo Inicial | Implementación | Creación de `logica_difusa.py` con ejemplos prácticos | Completado |
| Desarrollo Inicial | Implementación | Creación de `main.py` con menú CLI | Completado |
| Desarrollo Inicial | Documentación | Creación de `README.md` inicial | Completado |
| Optimización | Refactorización | Migración de CLI a aplicación web con Streamlit (`app.py`) | Completado |
| Optimización | UI/UX | Diseño de interfaz con pestañas, sliders y visualizaciones interactivas | Completado |
| Optimización | Integración | Integración de documentación en pestaña "Documentación y Evidencia" | Completado |
| Documentación | Estructuración | Creación carpeta `docs/` con documentación teórica completa | Completado |
| Documentación | Teoría | Documentación de lógica clásica y lógica difusa | Completado |
| Documentación | Manual | Creación de manual de uso detallado | Completado |
| Despliegue | Landing Page | Creación de `index.html` para GitHub Pages en raíz | Completado |
| Despliegue | Dependencias | Actualización de `requirements.txt` para Streamlit | Completado |
| Despliegue | README | Actualización completa del README.md con nueva estructura | Completado |

## Funcionalidades Implementadas

### Lógica Clásica
- [x] Tabla de verdad - Negación (¬p)
- [x] Tabla de verdad - Conjunción (p ∧ q)
- [x] Tabla de verdad - Disyunción (p ∨ q)
- [x] Tabla de verdad - Bicondicional (p ↔ q)

### Lógica Difusa
- [x] Función de pertenencia triangular
- [x] Clasificación difusa de temperatura con sliders
- [x] Operadores difusos (AND con min, OR con max, NOT)
- [x] Aplicaciones de lógica difusa en IA

### Interfaz Streamlit
- [x] Diseño responsive con sidebar
- [x] Pestañas de navegación
- [x] Visualización con DataFrames
- [x] Sliders interactivos
- [x] Métricas y alertas
- [x] Integración de documentación

### Documentación
- [x] Teoría completa de lógica clásica
- [x] Teoría completa de lógica difusa
- [x] Manual de uso
- [x] Landing page para GitHub Pages
- [x] README actualizado

## Capturas de Pantalla

Para agregar capturas de pantalla del funcionamiento de la aplicación:

1. Ejecutar `streamlit run app.py`
2. Tomar capturas de cada sección:
   - Inicio
   - Lógica Clásica
   - Lógica Difusa
   - Documentación y Evidencia
   - Acerca del Proyecto
3. Guardar las imágenes en esta carpeta (`docs/evidencia/`)
4. Nombrarlas descriptivamente (ej: `app_inicio.png`, `logica_clasica.png`, `logica_difusa.png`)

## Pruebas Realizadas

| Prueba | Descripción | Estado |
|--------|-------------|--------|
| Tablas de verdad | Verificación de todas las combinaciones | ✓ Correcto |
| Función triangular | Cálculo de pertenencia en puntos clave | ✓ Correcto |
| Operadores difusos | Validación de min, max y complemento | ✓ Correcto |
| Clasificación temperatura | Pruebas con diferentes valores | ✓ Correcto |
| Interfaz Streamlit | Navegación entre pestañas | ✓ Correcto |
| Importación módulos | Verificación de imports | ✓ Correcto |

## Tecnologías Utilizadas

- **Python 3.x** - Lenguaje de programación
- **Streamlit** - Framework para aplicaciones web interactivas
- **Pandas** - Manipulación y visualización de datos
- **HTML/CSS** - Landing page para GitHub Pages

## Conclusión

El proyecto ha sido optimizado exitosamente para trabajar con Streamlit, se ha actualizado toda la documentación, se ha creado la landing page para GitHub Pages en la raíz del repositorio, se han actualizado los requerimientos y se ha integrado una pestaña de documentación y evidencia dentro de la aplicación.

---

*Evidencia generada como parte del proyecto académico*
