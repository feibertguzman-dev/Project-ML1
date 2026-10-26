# logica_clasica.py
# Módulo que contiene las funciones para generar tablas de verdad de lógica proposicional clásica

def tabla_negacion():
    """Muestra la tabla de verdad de la negación (¬p)."""
    print("")
    print("=== TABLA DE VERDAD: NEGACIÓN (¬p) ===")
    print("La negación invierte el valor de verdad de la proposición.")
    print("")
    print("p     | ¬p")
    print("-" * 15)
    
    for p in [True, False]:
        not_p = not p
        print(f"{p!s:<6} | {not_p!s:<6}")
    print("")
    print("Interpretación: Si p es verdadero, ¬p es falso. Si p es falso, ¬p es verdadero.")


def tabla_conjuncion():
    """Muestra la tabla de verdad de la conjunción (p ∧ q)."""
    print("")
    print("=== TABLA DE VERDAD: CONJUNCIÓN (p ∧ q) ===")
    print("La conjunción 'p y q' solo es VERDADERA cuando ambas proposiciones lo son.")
    print("")
    print("p     | q     | p ∧ q")
    print("-" * 25)
    
    for p in [True, False]:
        for q in [True, False]:
            resultado = p and q
            print(f"{p!s:<6} | {q!s:<6} | {resultado!s:<6}")
    print("")
    print("Interpretación: (V ∧ V) = V | (V ∧ F)=F | (F ∧ V)=F | (F ∧ F)=F")


def tabla_disyuncion():
    """Muestra la tabla de verdad de la disyunción (p ∨ q)."""
    print("")
    print("=== TABLA DE VERDAD: DISYUNCIÓN (p ∨ q) ===")
    print("La disyunción 'p o q' es VERDADERA cuando al menos una de las proposiciones lo es.")
    print("")
    print("p     | q     | p ∨ q")
    print("-" * 25)
    
    for p in [True, False]:
        for q in [True, False]:
            resultado = p or q
            print(f"{p!s:<6} | {q!s:<6} | {resultado!s:<6}")
    print("")
    print("Interpretación: (V ∨ V)=V | (V ∨ F)=V | (F ∨ V)=V | (F ∨ F)=F")


def tabla_bicondicional():
    """Muestra la tabla de verdad del bicondicional (p ↔ q)."""
    print("")
    print("=== TABLA DE VERDAD: BICONDICIONAL (p ↔ q) ===")
    print("El bicondicional 'p si y solo si q' es VERDADERO cuando p y q tienen el MISMO valor de verdad.")
    print("")
    print("p     | q     | p ↔ q")
    print("-" * 25)
    
    for p in [True, False]:
        for q in [True, False]:
            resultado = (p == q)
            print(f"{p!s:<6} | {q!s:<6} | {resultado!s:<6}")
    print("")
    print("Interpretación: (V ↔ V)=V | (V ↔ F)=F | (F ↔ V)=F | (F ↔ F)=V")


def mostrar_menu_clasica():
    """Muestra el menú de lógica clásica."""
    print("")
    print("=" * 50)
    print("          LÓGICA CLÁSICA - TABLAS DE VERDAD")
    print("=" * 50)
    print("1. Negación (¬p)")
    print("2. Conjunción (p ∧ q)")
    print("3. Disyunción (p ∨ q)")
    print("4. Bicondicional (p ↔ q)")
    print("5. Volver al menú principal")
    return input("\nSeleccione una opción (1-5): ")


def ejecutar_logica_clasica():
    """Ejecuta el menú de lógica clásica."""
    while True:
        opcion = mostrar_menu_clasica()
        
        if opcion == "1":
            tabla_negacion()
            input("\nPresione ENTER para continuar...")
        elif opcion == "2":
            tabla_conjuncion()
            input("\nPresione ENTER para continuar...")
        elif opcion == "3":
            tabla_disyuncion()
            input("\nPresione ENTER para continuar...")
        elif opcion == "4":
            tabla_bicondicional()
            input("\nPresione ENTER para continuar...")
        elif opcion == "5":
            print("\nVolviendo al menú principal...")
            break
        else:
            print("\n[ERROR] Opción no válida. Intente nuevamente.")
            input("Presione ENTER para continuar...")
