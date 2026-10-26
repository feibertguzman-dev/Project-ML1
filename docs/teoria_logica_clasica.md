# Teoría: Lógica Proposicional Clásica

## Introducción

La lógica proposicional clásica (también llamada lógica de enunciados) es un sistema formal que se basa en el **principio de bivalencia**. Según este principio, toda proposición puede ser únicamente verdadera o falsa, sin valores intermedios.

## ¿Qué es una proposición?

Una **proposición** es un enunciado declarativo que puede ser clasificado como verdadero o falso, pero no ambas cosas a la vez.

**Ejemplos:**
- "El sol es una estrella" → Verdadera (V)
- "2 + 2 = 5" → Falsa (F)
- "¿Cómo estás?" → No es una proposición (es una pregunta)

## Conectivos Lógicos

Los conectivos lógicos permiten combinar proposiciones simples para formar proposiciones compuestas.

### 1. Negación (¬p)

La negación invierte el valor de verdad de una proposición. Si p es verdadera, ¬p es falsa, y viceversa.

**Tabla de Verdad:**

| p | ¬p |
|---|---|
| V | F |
| F | V |

**Lectura:** "No p", "Es falso que p"

### 2. Conjunción (p ∧ q)

La conjunción es verdadera únicamente cuando ambas proposiciones son verdaderas. En lenguaje natural se expresa con "y".

**Tabla de Verdad:**

| p | q | p ∧ q |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | F |

**Lectura:** "p y q"

### 3. Disyunción (p ∨ q)

La disyunción es verdadera cuando al menos una de las proposiciones es verdadera. En lenguaje natural se expresa con "o" (en sentido inclusivo).

**Tabla de Verdad:**

| p | q | p ∨ q |
|---|---|---|
| V | V | V |
| V | F | V |
| F | V | V |
| F | F | F |

**Lectura:** "p o q"

### 4. Bicondicional (p ↔ q)

El bicondicional es verdadero únicamente cuando ambas proposiciones tienen el mismo valor de verdad. Se lee como "si y solo si".

**Tabla de Verdad:**

| p | q | p ↔ q |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | V |

**Lectura:** "p si y solo si q"

## Características de la Lógica Clásica

- **Bivalente**: Solo dos valores de verdad
- **Determinista**: Cada proposición tiene un valor definido
- **Precisa**: No admite ambigüedad
- **Formal**: Se basa en reglas matemáticas estrictas

## Aplicaciones

- Diseño de circuitos digitales
- Programación y algoritmos
- Verificación formal de software
- Bases de datos y consultas lógicas
- Inteligencia Artificial (sistemas basados en reglas)

## Referencias

- Copi, I. M., & Cohen, C. (2018). *Introduction to Logic*. Routledge.
- Enderton, H. B. (2001). *A Mathematical Introduction to Logic*. Academic Press.
