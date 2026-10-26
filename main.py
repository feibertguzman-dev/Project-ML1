# main.py
# Programa principal: Calculadora de Tablas de Verdad y Lógica Difusa
# Destinado a la explicación de fundamentos de Introducción a la Inteligencia Artificial

import sys
import io

# Forzar codificación UTF-8 en la consola para soportar símbolos lógicos (∧ ∨ ↔ ¬)
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
if sys.stderr.encoding and sys.stderr.encoding.lower() != 'utf-8':
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from logica_clasica import ejecutar_logica_clasica
from logica_difusa import ejecutar_logica_difusa

def mostrar_menu_principal():
    """Muestra el menú principal del programa."""
    print('\n' + '=' * 65)
    print('  CALCULADORA DE TABLAS DE VERDAD Y LÓGICA DIFUSA')
    print('     Fundamentos de Introducción a la Inteligencia Artificial')
    print('=' * 65)
    print('\n1. Tablas de Verdad (Lógica Clásica)')
    print('2. Lógica Difusa (Ejemplos Prácticos)')
    print('3. Acerca del proyecto')
    print('4. Salir')
    return input('\nSeleccione una opción (1-4): ')


def mostrar_acerca_de():
    """Muestra información acerca del proyecto."""
    print('\n' + '=' * 60)
    print('                    ACERCA DEL PROYECTO')
    print('=' * 60)
    print('\nEste programa fue desarrollado con fines educativos para')
    print('explicar los fundamentos teórico-prácticos de:')
    print('\n  • LÓGICA PROPOSICIONAL CLÁSICA')
    print('    (Valores bivalentes: Verdadero/Falso)')
    print('\n  • LÓGICA DIFUSA')
    print('    (Grados de verdad en el intervalo [0,1])')
    print('\nTEMAS ABORDADOS:')
    print('  - Negación, Conjunción, Disyunción y Bicondicional')
    print('  - Funciones de pertenencia triangulares')
    print('  - Operadores difusos: MIN (AND), MAX (OR), Complemento (NOT)')
    print('  - Aplicaciones de lógica difusa en IA')
    print('\nBASE TEÓRICA:')
    print('  Lotfi A. Zadeh - "Fuzzy Sets" (1965)')
    print('=' * 60)


def main():
    """Función principal que gestiona el flujo del programa."""
    print('\n¡Bienvenido(a) al simulador educativo!')
    print('Explora y compara lógica clásica vs lógica difusa.')
    
    while True:
        opcion = mostrar_menu_principal()
        
        if opcion == '1':
            ejecutar_logica_clasica()
        elif opcion == '2':
            ejecutar_logica_difusa()
        elif opcion == '3':
            mostrar_acerca_de()
            input('\nPresione ENTER para continuar...')
        elif opcion == '4':
            print('\n' + '=' * 50)
            print('¡Gracias por usar este simulador educativo!')
            print('Sigue aprendiendo fundamentos de Inteligencia Artificial.')
            print('=' * 50)
            break
        else:
            print('\n[ERROR] Opción no válida. Por favor, seleccione 1-4.')
            input('Presione ENTER para continuar...')


if __name__ == '__main__':
    main()
