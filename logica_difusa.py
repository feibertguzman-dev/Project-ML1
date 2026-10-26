# logica_difusa.py
# Módulo con ejemplos prácticos de lógica difusa para Introducción a la IA

def funcion_pertenencia_triangular(x, a, b, c):
    """
    Calcula el grado de pertenencia mediante una función triangular.
    Parámetros:
        x (float): Valor a evaluar
        a (float): Límite izquierdo
        b (float): Pico (máxima pertenencia = 1.0)
        c (float): Límite derecho
    """
    try:
        x = float(x)
    except (ValueError, TypeError):
        return 0.0
    
    if x == b:
        return 1.0
    if x <= a or x >= c:
        return 0.0
    if x < b:
        if (b - a) == 0:
            return 0.0
        return (x - a) / (b - a)
    else:
        if (c - b) == 0:
            return 0.0
        return (c - x) / (c - b)


def ejemplo_temperatura():
    """Ejemplo práctico: Clasificación difusa de temperatura."""
    print("")
    print("=" * 60)
    print("       EJEMPLO 1: CLASIFICACIÓN DIFUSA DE TEMPERATURA")
    print("=" * 60)
    print("")
    print("Se desea clasificar la sensación térmica según la temperatura (°C).")
    print("Conjuntos difusos considerados:")
    print("  - FRÍO      (0°C a 20°C, pico en 10°C)")
    print("  - TEMPLADO  (15°C a 25°C, pico en 20°C)")
    print("  - CALIENTE  (20°C a 35°C, pico en 30°C)")
    print("-" * 60)
    
    try:
        temp = float(input("\nIngrese una temperatura en °C (ej. 18, 22, 28): "))
        
        mu_frio = funcion_pertenencia_triangular(temp, 0, 10, 20)
        mu_templado = funcion_pertenencia_triangular(temp, 15, 20, 25)
        mu_caliente = funcion_pertenencia_triangular(temp, 20, 30, 35)
        
        print("")
        print("Temperatura ingresada: " + str(temp) + " °C")
        print("-" * 40)
        print("Grado de pertenencia a FRÍO:     " + format(mu_frio, '.3f') + "  (" + format(mu_frio * 100, '.1f') + "%)")
        print("Grado de pertenencia a TEMPLADO: " + format(mu_templado, '.3f') + "  (" + format(mu_templado * 100, '.1f') + "%)")
        print("Grado de pertenencia a CALIENTE: " + format(mu_caliente, '.3f') + "  (" + format(mu_caliente * 100, '.1f') + "%)")
        print("-" * 40)
        
        print("")
        print("--- INTERPRETACIÓN ---")
        max_grado = max(mu_frio, mu_templado, mu_caliente)
        
        if max_grado < 0.01:
            print("La temperatura se encuentra fuera de los rangos definidos en este ejemplo.")
        else:
            resultado = "FRÍO"
            if mu_templado > mu_frio:
                resultado = "TEMPLADO"
            if mu_caliente > mu_templado and mu_caliente > mu_frio:
                resultado = "CALIENTE"
            print("Predomina la sensación: " + resultado + " (grado " + format(max_grado, '.3f') + ")")
        
        if mu_frio > 0 and mu_templado > 0 and mu_frio >= max_grado * 0.3 and mu_templado >= max_grado * 0.3:
            print("Existe traslape entre FRÍO y TEMPLADO (carácterístico de lógica difusa).")
        if mu_templado > 0 and mu_caliente > 0 and mu_templado >= max_grado * 0.3 and mu_caliente >= max_grado * 0.3:
            print("Existe traslape entre TEMPLADO y CALIENTE (carácterístico de lógica difusa).")
        
    except ValueError:
        print("")
        print("[ERROR] Debe ingresar un valor numérico válido.")
    except Exception:
        print("")
        print("[ERROR] Ocurrió un error inesperado.")


def ejemplo_operadores_difusos():
    """Ejemplo práctico: Operadores difusos AND, OR y COMPLEMENTO."""
    print("")
    print("=" * 60)
    print("       EJEMPLO 2: OPERADORES DIFUSOS (AND, OR, NO)")
    print("=" * 60)
    print("")
    print("Sean dos proposiciones difusas:")
    print('  A: "Hace calor"')
    print('  B: "Hay humedad"')
    print("-" * 60)
    
    try:
        mu_a = float(input("\nIngrese grado de pertenencia para A (muA) [0.0 - 1.0]: "))
        mu_b = float(input("Ingrese grado de pertenencia para B (muB) [0.0 - 1.0]: "))
        
        if mu_a < 0.0 or mu_a > 1.0 or mu_b < 0.0 or mu_b > 1.0:
            print("")
            print("[ADVERTENCIA] Los valores deben estar entre 0.0 y 1.0. Se ajustarán automáticamente.")
            mu_a = max(0.0, min(1.0, mu_a))
            mu_b = max(0.0, min(1.0, mu_b))
        
        mu_and = min(mu_a, mu_b)
        mu_or = max(mu_a, mu_b)
        mu_not_a = 1.0 - mu_a
        mu_not_b = 1.0 - mu_b
        
        print("")
        print("Valores ingresados:")
        print("  mu(A) = " + format(mu_a, '.3f') + "  (" + format(mu_a * 100, '.1f') + "%)")
        print("  mu(B) = " + format(mu_b, '.3f') + "  (" + format(mu_b * 100, '.1f') + "%)")
        print("-" * 50)
        print("")
        print("--- OPERADORES APLICADOS ---")
        print("1. A AND B (min(muA, muB)) -> mu(A ^ B) = " + format(mu_and, '.3f') + "  (" + format(mu_and * 100, '.1f') + "%)")
        print("2. A OR B  (max(muA, muB)) -> mu(A v B) = " + format(mu_or, '.3f') + "   (" + format(mu_or * 100, '.1f') + "%)")
        print("3. NOT A   (1 - muA)       -> mu(¬A)    = " + format(mu_not_a, '.3f') + "  (" + format(mu_not_a * 100, '.1f') + "%)")
        print("4. NOT B   (1 - muB)       -> mu(¬B)    = " + format(mu_not_b, '.3f') + "  (" + format(mu_not_b * 100, '.1f') + "%)")
        print("-" * 50)
        
        print("")
        print("--- INTERPRETACIÓN ---")
        print('"Hace calor Y hay humedad": Grado = ' + format(mu_and, '.3f'))
        print('"Hace calor O hay humedad": Grado = ' + format(mu_or, '.3f'))
        print('"NO hace calor":            Grado = ' + format(mu_not_a, '.3f'))
        
    except ValueError:
        print("")
        print("[ERROR] Debe ingresar valores numéricos entre 0.0 y 1.0.")
    except Exception:
        print("")
        print("[ERROR] Ocurrió un error inesperado.")


def ejemplo_aplicacion_ia():
    """Muestra aplicaciones reales de lógica difusa en Inteligencia Artificial."""
    print("")
    print("=" * 60)
    print("  EJEMPLO 3: APLICACIONES DE LÓGICA DIFUSA EN IA")
    print("=" * 60)
    print("")
    print("La lógica difusa permite modelar conocimiento experto con términos lingüísticos:")
    print("-" * 60)
    print("")
    
    aplicaciones = [
        ("Sistemas de Control Difuso", "Aire acondicionado, lavadoras, horno microondas."),
        ("Sistemas Expertos", "Diagnóstico médico, evaluación crediticia."),
        ("Vehículos Autónomos", "Toma de decisiones ante situaciones ambiguas."),
        ("Robótica", "Navegación y evitación de obstáculos."),
        ("Reconocimiento de Patrones", "Visión por computadora, voz e imágenes."),
        ("Sistemas de Recomendación", "Sugerencias basadas en preferencias difusas."),
        ("Predicción y Pronóstico", "Meteorología, mercados financieros."),
    ]
    
    for i, (titulo, desc) in enumerate(aplicaciones, 1):
        print(str(i) + ". " + titulo)
        print("   " + desc)
        print("")
    
    print("-" * 60)
    print("CONCLUSIÓN: La lógica difusa aproxima el razonamiento humano")
    print("al de las máquinas, permitiendo resolver problemas donde")
    print("no existe una respuesta binaria clara.")


def mostrar_menu_difusa():
    """Muestra el menú de lógica difusa."""
    print("")
    print("=" * 50)
    print("        LÓGICA DIFUSA - EJEMPLOS PRÁCTICOS")
    print("=" * 50)
    print("1. Ejemplo: Clasificación difusa de temperatura (°C)")
    print("2. Ejemplo: Operadores difusos AND, OR y COMPLEMENTO")
    print("3. Aplicaciones de lógica difusa en Inteligencia Artificial")
    print("4. Volver al menú principal")
    return input("\nSeleccione una opción (1-4): ")


def ejecutar_logica_difusa():
    """Ejecuta el menú de lógica difusa."""
    while True:
        opcion = mostrar_menu_difusa()
        
        if opcion == "1":
            ejemplo_temperatura()
            input("\nPresione ENTER para continuar...")
        elif opcion == "2":
            ejemplo_operadores_difusos()
            input("\nPresione ENTER para continuar...")
        elif opcion == "3":
            ejemplo_aplicacion_ia()
            input("\nPresione ENTER para continuar...")
        elif opcion == "4":
            print("\nVolviendo al menú principal...")
            break
        else:
            print("\n[ERROR] Opción no válida. Intente nuevamente.")
            input("Presione ENTER para continuar...")
