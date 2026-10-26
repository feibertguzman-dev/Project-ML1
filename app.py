# app.py
# Calculadora de Tablas de Verdad y Lógica Difusa - Versión Streamlit
# Proyecto educativo para Introducción a la Inteligencia Artificial

import streamlit as st
import pandas as pd
import os
from pathlib import Path

from logica_clasica import (
    tabla_negacion,
    tabla_conjuncion,
    tabla_disyuncion,
    tabla_bicondicional,
)
from logica_difusa import (
    funcion_pertenencia_triangular,
    ejemplo_temperatura,
    ejemplo_operadores_difusos,
    ejemplo_aplicacion_ia,
)

# Configuración de la página
st.set_page_config(
    page_title="Calculadora de Tablas de Verdad y Lógica Difusa",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Estilos CSS personalizados
st.markdown(
    """
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1f4e79;
        text-align: center;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.8rem;
        color: #2c5aa0;
        font-weight: bold;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .info-box {
        background-color: #f0f8ff;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f4e79;
        margin: 1rem 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def mostrar_tabla_negacion():
    """Muestra la tabla de verdad de la negación en Streamlit"""
    st.markdown('<div class="section-header">Tabla de Verdad: Negación (¬p)</div>', unsafe_allow_html=True)
    st.markdown("La negación invierte el valor de verdad de la proposición.")
    
    datos = []
    for p in [True, False]:
        not_p = not p
        datos.append({"p": p, "¬p": not_p})
    
    df = pd.DataFrame(datos)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.markdown('<div class="info-box">Interpretación: Si p es verdadero, ¬p es falso. Si p es falso, ¬p es verdadero.</div>', unsafe_allow_html=True)

def mostrar_tabla_conjuncion():
    """Muestra la tabla de verdad de la conjunción en Streamlit"""
    st.markdown('<div class="section-header">Tabla de Verdad: Conjunción (p ∧ q)</div>', unsafe_allow_html=True)
    st.markdown("La conjunción 'p y q' solo es VERDADERA cuando ambas proposiciones lo son.")
    
    datos = []
    for p in [True, False]:
        for q in [True, False]:
            resultado = p and q
            datos.append({"p": p, "q": q, "p ∧ q": resultado})
    
    df = pd.DataFrame(datos)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.markdown('<div class="info-box">Interpretación: (V ∧ V) = V | (V ∧ F)=F | (F ∧ V)=F | (F ∧ F)=F</div>', unsafe_allow_html=True)

def mostrar_tabla_disyuncion():
    """Muestra la tabla de verdad de la disyunción en Streamlit"""
    st.markdown('<div class="section-header">Tabla de Verdad: Disyunción (p ∨ q)</div>', unsafe_allow_html=True)
    st.markdown("La disyunción 'p o q' es VERDADERA cuando al menos una de las proposiciones lo es.")
    
    datos = []
    for p in [True, False]:
        for q in [True, False]:
            resultado = p or q
            datos.append({"p": p, "q": q, "p ∨ q": resultado})
    
    df = pd.DataFrame(datos)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.markdown('<div class="info-box">Interpretación: (V ∨ V)=V | (V ∨ F)=V | (F ∨ V)=V | (F ∨ F)=F</div>', unsafe_allow_html=True)

def mostrar_tabla_bicondicional():
    """Muestra la tabla de verdad del bicondicional en Streamlit"""
    st.markdown('<div class="section-header">Tabla de Verdad: Bicondicional (p ↔ q)</div>', unsafe_allow_html=True)
    st.markdown("El bicondicional 'p si y solo si q' es VERDADERO cuando p y q tienen el MISMO valor de verdad.")
    
    datos = []
    for p in [True, False]:
        for q in [True, False]:
            resultado = (p == q)
            datos.append({"p": p, "q": q, "p ↔ q": resultado})
    
    df = pd.DataFrame(datos)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.markdown('<div class="info-box">Interpretación: (V ↔ V)=V | (V ↔ F)=F | (F ↔ V)=F | (F ↔ F)=V</div>', unsafe_allow_html=True)

def mostrar_clasificacion_temperatura():
    """Muestra el ejemplo de clasificación difusa de temperatura"""
    st.markdown('<div class="section-header">Ejemplo: Clasificación Difusa de Temperatura</div>', unsafe_allow_html=True)
    st.markdown("Se desea clasificar la sensación térmica según la temperatura (°C).")
    
    with st.expander("Conjuntos difusos considerados"):
        st.write("- **FRÍO**      (0°C a 20°C, pico en 10°C)")
        st.write("- **TEMPLADO**  (15°C a 25°C, pico en 20°C)")
        st.write("- **CALIENTE**  (20°C a 35°C, pico en 30°C)")
    
    temp = st.slider("Seleccione la temperatura en °C", min_value=-5.0, max_value=40.0, value=18.0, step=0.5)
    
    if st.button("Calcular pertenencias", key="temp_btn"):
        mu_frio = funcion_pertenencia_triangular(temp, 0, 10, 20)
        mu_templado = funcion_pertenencia_triangular(temp, 15, 20, 25)
        mu_caliente = funcion_pertenencia_triangular(temp, 20, 30, 35)
        
        st.markdown(f"### Temperatura ingresada: {temp} °C")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("FRÍO", f"{mu_frio:.3f}", f"{mu_frio*100:.1f}%")
        with col2:
            st.metric("TEMPLADO", f"{mu_templado:.3f}", f"{mu_templado*100:.1f}%")
        with col3:
            st.metric("CALIENTE", f"{mu_caliente:.3f}", f"{mu_caliente*100:.1f}%")
        
        max_grado = max(mu_frio, mu_templado, mu_caliente)
        st.markdown("### Interpretación")
        if max_grado < 0.01:
            st.warning("La temperatura se encuentra fuera de los rangos definidos en este ejemplo.")
        else:
            resultado = "FRÍO"
            if mu_templado > mu_frio and mu_templado >= mu_caliente:
                resultado = "TEMPLADO"
            elif mu_caliente > mu_templado and mu_caliente > mu_frio:
                resultado = "CALIENTE"
            elif mu_frio >= mu_templado and mu_frio >= mu_caliente:
                resultado = "FRÍO"
            st.success(f"Predomina la sensación: **{resultado}** (grado {max_grado:.3f})")
        
        if mu_frio > 0 and mu_templado > 0 and min(mu_frio, mu_templado) >= max_grado * 0.3:
            st.info("Existe traslape entre FRÍO y TEMPLADO (característico de lógica difusa).")
        if mu_templado > 0 and mu_caliente > 0 and min(mu_templado, mu_caliente) >= max_grado * 0.3:
            st.info("Existe traslape entre TEMPLADO y CALIENTE (característico de lógica difusa).")

def mostrar_operadores_difusos():
    """Muestra el ejemplo de operadores difusos"""
    st.markdown('<div class="section-header">Ejemplo: Operadores Difusos (AND, OR, NOT)</div>', unsafe_allow_html=True)
    st.markdown("Sean dos proposiciones difusas: A: 'Hace calor' y B: 'Hay humedad'")
    
    col1, col2 = st.columns(2)
    with col1:
        mu_a = st.slider("Grado de pertenencia para A (muA)", min_value=0.0, max_value=1.0, value=0.7, step=0.01)
    with col2:
        mu_b = st.slider("Grado de pertenencia para B (muB)", min_value=0.0, max_value=1.0, value=0.4, step=0.01)
    
    if st.button("Aplicar operadores", key="op_btn"):
        mu_and = min(mu_a, mu_b)
        mu_or = max(mu_a, mu_b)
        mu_not_a = 1.0 - mu_a
        mu_not_b = 1.0 - mu_b
        
        st.markdown("### Valores ingresados")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("mu(A)", f"{mu_a:.3f}", f"{mu_a*100:.1f}%")
        with col2:
            st.metric("mu(B)", f"{mu_b:.3f}", f"{mu_b*100:.1f}%")
        
        st.markdown("### Operadores aplicados")
        datos_op = [
            {"Operador": "A AND B (min)", "Resultado": f"{mu_and:.3f}", "Porcentaje": f"{mu_and*100:.1f}%"},
            {"Operador": "A OR B (max)", "Resultado": f"{mu_or:.3f}", "Porcentaje": f"{mu_or*100:.1f}%"},
            {"Operador": "NOT A (1 - muA)", "Resultado": f"{mu_not_a:.3f}", "Porcentaje": f"{mu_not_a*100:.1f}%"},
            {"Operador": "NOT B (1 - muB)", "Resultado": f"{mu_not_b:.3f}", "Porcentaje": f"{mu_not_b*100:.1f}%"},
        ]
        df_op = pd.DataFrame(datos_op)
        st.dataframe(df_op, use_container_width=True, hide_index=True)
        
        st.markdown("### Interpretación")
        st.write(f'- "Hace calor Y hay humedad": Grado = {mu_and:.3f}')
        st.write(f'- "Hace calor O hay humedad": Grado = {mu_or:.3f}')
        st.write(f'- "NO hace calor": Grado = {mu_not_a:.3f}')

def mostrar_aplicaciones_ia():
    """Muestra aplicaciones de lógica difusa en IA"""
    st.markdown('<div class="section-header">Aplicaciones de Lógica Difusa en Inteligencia Artificial</div>', unsafe_allow_html=True)
    st.markdown("La lógica difusa permite modelar conocimiento experto con términos lingüísticos:")
    
    aplicaciones = [
        {"Aplicación": "Sistemas de Control Difuso", "Descripción": "Aire acondicionado, lavadoras, horno microondas."},
        {"Aplicación": "Sistemas Expertos", "Descripción": "Diagnóstico médico, evaluación crediticia."},
        {"Aplicación": "Vehículos Autónomos", "Descripción": "Toma de decisiones ante situaciones ambiguas."},
        {"Aplicación": "Robótica", "Descripción": "Navegación y evitación de obstáculos."},
        {"Aplicación": "Reconocimiento de Patrones", "Descripción": "Visión por computadora, voz e imágenes."},
        {"Aplicación": "Sistemas de Recomendación", "Descripción": "Sugerencias basadas en preferencias difusas."},
        {"Aplicación": "Predicción y Pronóstico", "Descripción": "Meteorología, mercados financieros."},
    ]
    
    df_app = pd.DataFrame(aplicaciones)
    st.dataframe(df_app, use_container_width=True, hide_index=True)
    
    st.markdown('<div class="info-box">CONCLUSIÓN: La lógica difusa aproxima el razonamiento humano al de las máquinas, permitiendo resolver problemas donde no existe una respuesta binaria clara.</div>', unsafe_allow_html=True)

def mostrar_documentacion_evidencia():
    """Muestra la documentación y evidencias del proyecto"""
    st.markdown('<div class="section-header">Documentación y Evidencia del Proyecto</div>', unsafe_allow_html=True)
    st.markdown("Aquí encontrarás la documentación teórica, manual de uso y evidencias del desarrollo.")
    
    tab1, tab2, tab3, tab4 = st.tabs(["📚 Teoría", "📖 Manual de Uso", "🧾 Evidencia", "📁 Archivos de Docs"])
    
    with tab1:
        st.markdown("### Teoría: Lógica Clásica vs Lógica Difusa")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Lógica Proposicional Clásica")
            st.markdown("""
            - **Principio de bivalencia**: Una proposición solo puede ser Verdadera (True) o Falsa (False)
            - **Conectivos lógicos**: Negación (¬), Conjunción (∧), Disyunción (∨), Bicondicional (↔)
            - **Tablas de verdad**: Método sistemático para determinar el valor de verdad
            - **Aplicación**: Razonamiento deductivo preciso y formal
            """)
        
        with col2:
            st.markdown("#### Lógica Difusa (Fuzzy Logic)")
            st.markdown("""
            - **Grados de verdad**: Valores en el intervalo [0, 1]
            - **Funciones de pertenencia**: Representan conjuntos difusos
            - **Operadores difusos**: MIN (AND), MAX (OR), Complemento (NOT)
            - **Aplicación**: Razonamiento aproximado, sistemas expertos, control difuso
            """)
        
        st.markdown('<div class="info-box">Lotfi A. Zadeh introdujo la teoría de conjuntos difusos en 1965 con su artículo "Fuzzy Sets".</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### Manual de Uso de la Aplicación")
        st.markdown("""
        #### Cómo usar esta aplicación Streamlit:
        
        1. **Inicio**: Vista general del proyecto
        2. **Lógica Clásica**: Genera tablas de verdad para los conectivos lógicos
           - Selecciona el tipo de tabla desde el menú lateral
           - Visualiza los resultados en formato tabular
        3. **Lógica Difusa**: Explora ejemplos prácticos
           - Usa sliders para modificar los valores
           - Observa cómo cambian los grados de pertenencia
        4. **Documentación y Evidencia**: Accede a toda la documentación del proyecto
        5. **Acerca del Proyecto**: Información general y objetivos
        
        #### Ejecución local:
        ```bash
        # Crear entorno virtual
        python -m venv .venv
        
        # Activar entorno virtual
        # Windows
        .venv\\Scripts\\activate
        # Linux/macOS
        source .venv/bin/activate
        
        # Instalar dependencias
        pip install -r requirements.txt
        
        # Ejecutar aplicación
        streamlit run app.py
        ```
        """)
    
    with tab3:
        st.markdown("### Evidencia de Desarrollo")
        st.markdown("Documentación del proceso de desarrollo, pruebas y resultados.")
        
        evidencia_items = [
            {"Fecha": "Desarrollo", "Actividad": "Implementación módulos lógica_clasica.py y logica_difusa.py", "Estado": "Completado"},
            {"Fecha": "Desarrollo", "Actividad": "Creación menú principal CLI (main.py)", "Estado": "Completado"},
            {"Fecha": "Optimización", "Actividad": "Migración a aplicación Streamlit (app.py)", "Estado": "Completado"},
            {"Fecha": "Documentación", "Actividad": "Creación carpeta docs/ con documentación teórica", "Estado": "Completado"},
            {"Fecha": "Despliegue", "Actividad": "Creación landing page index.html para GitHub Pages", "Estado": "Completado"},
            {"Fecha": "Optimización", "Actividad": "Actualización requirements.txt para Streamlit", "Estado": "Completado"},
        ]
        
        df_ev = pd.DataFrame(evidencia_items)
        st.dataframe(df_ev, use_container_width=True, hide_index=True)
        
        st.markdown("#### Capturas y Recursos")
        st.info("Las evidencias visuales se encuentran en la carpeta `docs/evidencia/`. Puedes agregar capturas de pantalla de la aplicación en funcionamiento.")
    
    with tab4:
        st.markdown("### Archivos de Documentación")
        docs_path = Path("docs")
        if docs_path.exists():
            for file in sorted(docs_path.rglob("*")):
                if file.is_file() and file.name != "README.md":
                    rel_path = file.relative_to(docs_path)
                    st.write(f"📄 **{rel_path}**")
                elif file.name == "README.md" and file.parent == docs_path:
                    st.write(f"📖 **{file.name}** (Índice de documentación)")
        else:
            st.warning("La carpeta docs/ no existe aún.")
        
        st.markdown("---")
        st.markdown("**Nota:** Puedes editar los archivos en la carpeta `docs/` para agregar más documentación. Los cambios se reflejarán al recargar la aplicación.")

def main():
    """Función principal de la aplicación Streamlit"""
    
    # Header
    st.markdown('<div class="main-header">🧮 Calculadora de Tablas de Verdad y Lógica Difusa</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Fundamentos de Introducción a la Inteligencia Artificial</div>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.image("https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white", use_container_width=True)
        st.image("https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B?logo=streamlit&logoColor=white", use_container_width=True)
        st.image("https://img.shields.io/badge/Estado-Educativo-brightgreen", use_container_width=True)
        
        st.markdown("---")
        st.markdown("### Navegación")
        pagina = st.radio(
            "Selecciona una sección:",
            ["🏠 Inicio", "📊 Lógica Clásica", "🌊 Lógica Difusa", "📚 Documentación y Evidencia", "ℹ️ Acerca del Proyecto"],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        st.markdown("### Información")
        st.info("Proyecto académico - Introducción a la Inteligencia Artificial")
    
    # Contenido principal
    if pagina == "🏠 Inicio":
        st.markdown("## Bienvenido")
        st.markdown("""
        Esta aplicación interactiva permite explorar y comparar dos enfoques fundamentales del razonamiento en Inteligencia Artificial:
        
        - **Lógica Proposicional Clásica**: Basada en el principio de bivalencia (Verdadero/Falso)
        - **Lógica Difusa**: Permite trabajar con grados de verdad en el intervalo [0, 1]
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🎯 Características")
            st.markdown("""
            - Tablas de verdad interactivas
            - Ejemplos prácticos de lógica difusa
            - Clasificación difusa de temperatura
            - Operadores difusos AND, OR, NOT
            - Aplicaciones reales en IA
            - Documentación completa integrada
            """)
        
        with col2:
            st.markdown("### 🚀 Inicio Rápido")
            st.markdown("""
            1. Selecciona **Lógica Clásica** para generar tablas de verdad
            2. Selecciona **Lógica Difusa** para explorar ejemplos prácticos
            3. Consulta la **Documentación y Evidencia** para aprender más
            4. Revisa **Acerca del Proyecto** para más información
            """)
        
        st.markdown("---")
        st.markdown("### Diferencia Fundamental")
        col1, col2 = st.columns(2)
        with col1:
            st.success("**Lógica Clásica:** Responde con un 'sí' o 'no'")
        with col2:
            st.info("**Lógica Difusa:** Responde con '¿qué tan cierto?'")
    
    elif pagina == "📊 Lógica Clásica":
        st.markdown("## Lógica Proposicional Clásica - Tablas de Verdad")
        st.markdown("Selecciona el conectivo lógico que deseas analizar:")
        
        opcion_clasica = st.selectbox(
            "Conectivo lógico:",
            ["Negación (¬p)", "Conjunción (p ∧ q)", "Disyunción (p ∨ q)", "Bicondicional (p ↔ q)"]
        )
        
        if opcion_clasica == "Negación (¬p)":
            mostrar_tabla_negacion()
        elif opcion_clasica == "Conjunción (p ∧ q)":
            mostrar_tabla_conjuncion()
        elif opcion_clasica == "Disyunción (p ∨ q)":
            mostrar_tabla_disyuncion()
        elif opcion_clasica == "Bicondicional (p ↔ q)":
            mostrar_tabla_bicondicional()
    
    elif pagina == "🌊 Lógica Difusa":
        st.markdown("## Lógica Difusa - Ejemplos Prácticos")
        st.markdown("Explora los conceptos fundamentales de la lógica difusa:")
        
        opcion_difusa = st.selectbox(
            "Ejemplo a visualizar:",
            ["Clasificación difusa de temperatura", "Operadores difusos (AND, OR, NOT)", "Aplicaciones en Inteligencia Artificial"]
        )
        
        if opcion_difusa == "Clasificación difusa de temperatura":
            mostrar_clasificacion_temperatura()
        elif opcion_difusa == "Operadores difusos (AND, OR, NOT)":
            mostrar_operadores_difusos()
        elif opcion_difusa == "Aplicaciones en Inteligencia Artificial":
            mostrar_aplicaciones_ia()
    
    elif pagina == "📚 Documentación y Evidencia":
        mostrar_documentacion_evidencia()
    
    elif pagina == "ℹ️ Acerca del Proyecto":
        st.markdown("## Acerca del Proyecto")
        
        st.markdown("""
        Este programa fue desarrollado con fines educativos para explicar los fundamentos teórico-prácticos de:
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### LÓGICA PROPOSICIONAL CLÁSICA")
            st.markdown("*Valores bivalentes: Verdadero/Falso*")
        with col2:
            st.markdown("### LÓGICA DIFUSA")
            st.markdown("*Grados de verdad en el intervalo [0,1]*")
        
        st.markdown("### Temas Abordados")
        st.markdown("""
        - Negación, Conjunción, Disyunción y Bicondicional
        - Funciones de pertenencia triangulares
        - Operadores difusos: MIN (AND), MAX (OR), Complemento (NOT)
        - Aplicaciones de lógica difusa en IA
        """)
        
        st.markdown("### Base Teórica")
        st.markdown("**Lotfi A. Zadeh** - *\"Fuzzy Sets\"* (1965)")
        
        st.markdown("---")
        st.markdown("### Autor")
        st.markdown("Proyecto académico para la asignatura **Introducción a la Inteligencia Artificial**")
        
        st.markdown("### Tecnologías Utilizadas")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("**Python**")
        with col2:
            st.markdown("**Streamlit**")
        with col3:
            st.markdown("**Pandas**")
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #666;'>Calculadora de Tablas de Verdad y Lógica Difusa | Proyecto Educativo</div>",
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
