# Trabajo Práctico 1 - Fundamentos de Python

## 📋 Introducción

Este trabajo práctico tiene como objetivo introducir los conceptos básicos de Python: variables, tipos de datos, operadores aritméticos y entrada/salida. Los ejercicios están diseñados para practicar operaciones sin usar estructuras de control (if, while, for).

## 🎯 Objetivos de Aprendizaje

Al completar este TP, deberías ser capaz de:
- Declarar y asignar valores a variables
- Utilizar operadores aritméticos básicos (+, -, *, /, //, %)
- Trabajar con diferentes tipos de datos (int, float, string)
- Imprimir resultados en consola con `print()`
- Convertir entre tipos de datos (int, float, str)
- Realizar cálculos matemáticos simples

## 🚀 Instrucciones de Ejecución

### Ejecutar un ejercicio individual

Para ejecutar cada ejercicio desde la terminal:

```bash
python exercise_math.py
```

### Verificar tus resultados

Cada ejercicio incluye valores de ejemplo y el output esperado. Compará tu resultado con el ejemplo proporcionado.

### Estructura de los archivos

Cada archivo de ejercicio contiene:
- Una función con el nombre del ejercicio
- Variables ya inicializadas con valores de ejemplo
- Comentarios indicando qué debes calcular
- El output esperado en el README

Tu tarea es completar el código dentro de cada función para que imprima los resultados correctos.

---

## 📚 Ejercicios

### Ejercicio 0 - Lectura de Código

**Archivo:** No requiere archivo (ejercicio de lectura)

**Objetivo:** Aprender a leer código Python y predecir su comportamiento antes de ejecutarlo.

Para este ejercicio, el objetivo es **leer el código**, anotar en un papel lo que pienses que los prints van a mostrar, y **luego** ejecutar el código para verificar si acertaste.

```python
# Operaciones con enteros
i1 = 3
i2 = 5
i3 = i2 + i1
print("valor de i1:")
print(i1)
print("valor de i2:")
print(i2)
print("valor de i3:")
print(i3)
print(i1 + i2 + i3)

# Concatenación de strings
s1, s2, s3 = "Python", " is ", 'awesome'
print(s1 + s2 + s3)

# Asignación múltiple
x = y = z = "Naranja"
print("valor de x: " + x + ", valor de y: " + y + ", valor de z: " + z)

# División y módulo
z1 = i3 / i2
print(z1)
z2 = i3 % i2
print(z2)

# Conversión de tipos
f1 = -.5
f2 = 10
f3 = f1 + f2
i3 = int(f3)
print("entero i3:")
print(i3)
print("variable f3:")
print(f3)

# Operadores de asignación compuestos
f2 += i1
print("el valor de")
print(f2)
print("más")
print(f1)
print("es:")
print(f2 + f1)
```

**Conceptos clave:**
- Tipos de datos: `int`, `float`, `str`
- Operadores: `+`, `/`, `%`, `+=`
- Asignación múltiple: `x = y = z = valor`
- Conversión de tipos: `int()`, `float()`
- Concatenación de strings con `+`

---

### Ejercicio 1 - Math (Operaciones Matemáticas)

**Archivo:** `exercise_math.py`

**Objetivo:** Practicar operadores aritméticos básicos y diferentes tipos de división.

Dado dos números enteros `a` y `b`, imprimir en pantalla:
1. La suma (a + b)
2. La diferencia (a - b)
3. El producto (a × b)
4. El promedio ((a + b) / 2)
5. El cociente entero (a // b)
6. El resto de la división entera (a % b)
7. El valor real de la división (a / b)

**Importante:** Los resultados deben imprimirse en el orden pedido.

**Ejemplo:** Para `a = 57` y `b = 7` el output deberá ser:

```
64
50
399
32.0
8
1
8.142857142857142
```

**Conceptos clave:**
- Operador `+`: suma
- Operador `-`: resta
- Operador `*`: multiplicación
- Operador `/`: división decimal (float)
- Operador `//`: división entera (descarta decimales)
- Operador `%`: módulo (resto de la división)

---

### Ejercicio 2 - Geometría de Rectángulo

**Archivo:** `exercise_rectangle.py`

**Objetivo:** Aplicar fórmulas geométricas básicas.

Dado un rectángulo con `base` y `altura`, calcular e imprimir:
1. El área del rectángulo: `área = base × altura`
2. El perímetro del rectángulo: `perímetro = 2 × base + 2 × altura`

Los resultados deben imprimirse como números enteros en el orden pedido.

**Ejemplo:** Para `base = 10` y `altura = 5` el output deberá ser:

```
50
30
```

**Conceptos clave:**
- Aplicación de fórmulas matemáticas
- Operaciones con variables
- Múltiples cálculos relacionados

---

### Ejercicio 3 - Conversión de Temperatura

**Archivo:** `exercise_temperature.py`

**Objetivo:** Practicar conversiones con fórmulas y manejo de decimales.

Dada una temperatura en grados Celsius, imprimir:
1. La temperatura convertida a Fahrenheit usando: `F = C × 9/5 + 32`
2. La temperatura original en Celsius (para practicar el uso de variables)

Los resultados deben imprimirse como números decimales en el orden pedido.

**Ejemplo:** Para `celsius = 25` el output deberá ser:

```
77.0
25.0
```

**Nota:** La segunda línea debe imprimir el valor original de celsius (25), no el valor convertido.

**Conceptos clave:**
- Aplicación de fórmulas de conversión
- Orden de operaciones (precedencia de operadores)
- Trabajo con números decimales (float)

---

### Ejercicio 4 - Calculadora de Tiempo

**Archivo:** `exercise_time.py`

**Objetivo:** Practicar división entera y módulo para conversiones de unidades.

Dado un número total de segundos, calcular e imprimir:
1. Cuántas horas completas hay (división entera por 3600)
2. Cuántos minutos completos quedan después de sacar las horas
3. Cuántos segundos quedan después de sacar horas y minutos

Los resultados deben imprimirse en el orden pedido: horas, minutos, segundos.

**Ejemplo:** Para `total_segundos = 3665` el output deberá ser:

```
1
1
5
```

**Explicación:** 3665 segundos = 1 hora (3600 seg) + 1 minuto (60 seg) + 5 segundos

**Pistas:**
- Usá `//` (división entera) para obtener las horas: `total_segundos // 3600`
- Usá `%` (módulo) para obtener el resto después de las horas: `total_segundos % 3600`
- Aplicá la misma lógica para obtener minutos y segundos del resto

**Conceptos clave:**
- Operador `//` (división entera)
- Operador `%` (módulo/resto)
- Conversión de unidades
- Cálculos secuenciales con resultados intermedios

---

### Ejercicio 5 - Estadísticas Simples

**Archivo:** `exercise_statistics.py`

**Objetivo:** Realizar cálculos estadísticos básicos usando funciones integradas.

Dados cuatro números, calcular e imprimir:
1. El promedio de los cuatro números
2. El máximo de los cuatro números
3. El mínimo de los cuatro números
4. El rango (diferencia entre el máximo y el mínimo)

Los resultados deben imprimirse en el orden pedido.

**Ejemplo:** Para `num1 = 15`, `num2 = 8`, `num3 = 23`, `num4 = 12` el output deberá ser:

```
14.5
23
8
15
```

**Pistas:**
- Para el promedio: sumá los 4 números y dividí por 4
- Python tiene funciones integradas `max()` y `min()` que aceptan múltiples argumentos:
  ```python
  maximo = max(num1, num2, num3, num4)
  minimo = min(num1, num2, num3, num4)
  ```
- El rango es simplemente: `rango = maximo - minimo`

**Conceptos clave:**
- Funciones integradas: `max()`, `min()`
- Cálculo de promedio
- Operaciones con múltiples variables

---

## 🆕 Ejercicios Adicionales

Los siguientes ejercicios son opcionales pero recomendados para practicar más:

### Ejercicio 6 - Geometría de Círculo

**Archivo:** `exercise_circle.py`

**Objetivo:** Trabajar con constantes y la biblioteca `math`.

Dado el radio de un círculo, calcular e imprimir:
1. El área del círculo: `π × radio²`
2. La circunferencia: `2 × π × radio`

**Ejemplo:** Para `radio = 5` el output deberá ser (aproximado):

```
78.53981633974483
31.41592653589793
```

**Pistas:**
- Importá la constante PI desde la biblioteca math: `from math import pi`
- Usá `radio ** 2` o `radio * radio` para calcular el cuadrado

---

### Ejercicio 7 - Conversión de Unidades de Longitud

**Archivo:** `exercise_length.py`

**Objetivo:** Practicar conversiones con múltiples unidades.

Dada una distancia en metros, convertir e imprimir:
1. La distancia en kilómetros (1 km = 1000 m)
2. La distancia en millas (1 milla ≈ 1609.34 m)
3. La distancia en pies (1 pie ≈ 0.3048 m)
4. La distancia en pulgadas (1 pulgada ≈ 0.0254 m)

**Ejemplo:** Para `metros = 1000` el output deberá ser (aproximado):

```
1.0
0.6213711922373339
3280.839895013123
39370.07874015748
```

---

### Ejercicio 8 - Cálculo de Precio Final

**Archivo:** `exercise_price.py`

**Objetivo:** Aplicar múltiples porcentajes en secuencia.

Dado un precio base, calcular e imprimir:
1. El monto del impuesto (21% del precio base)
2. El subtotal (precio base + impuesto)
3. El monto de la propina (10% del subtotal)
4. El precio final (subtotal + propina)

**Ejemplo:** Para `precio_base = 100` el output deberá ser:

```
21.0
121.0
12.1
133.1
```

**Pistas:**
- Para calcular el 21%: `precio_base * 0.21`
- Recordá ir guardando los resultados intermedios en variables

---

### Ejercicio 9 - Intercambio de Variables

**Archivo:** `exercise_swap.py`

**Objetivo:** Aprender a intercambiar valores sin usar variable temporal (usando asignación múltiple de Python).

Dados dos valores `x` e `y`, intercambiar sus valores e imprimir:
1. Los valores originales de x e y
2. Los valores después del intercambio

**Ejemplo:** Para `x = 10` y `y = 20` el output deberá ser:

```
10
20
20
10
```

**Pistas:**
- Python permite asignación múltiple: `a, b = b, a`
- Imprimí primero los valores originales, luego intercambialos, luego imprimí nuevamente

---

### Ejercicio 10 - Conversión de Edad a Tiempo

**Archivo:** `exercise_age.py`

**Objetivo:** Realizar múltiples conversiones de unidades de tiempo.

Dada una edad en años, calcular e imprimir:
1. La edad en meses (aproximado: 1 año = 12 meses)
2. La edad en días (aproximado: 1 año = 365 días)
3. La edad en horas (1 día = 24 horas)
4. La edad en minutos (1 hora = 60 minutos)

**Ejemplo:** Para `edad_anos = 25` el output deberá ser:

```
300
9125
219000
13140000
```

---

### Ejercicio 11 - Promedio de Calificaciones

**Archivo:** `exercise_grades.py`

**Objetivo:** Trabajar con promedios y diferencias.

Dadas tres calificaciones (notas), calcular e imprimir:
1. El promedio de las tres notas
2. La nota máxima
3. La nota mínima
4. Cuántos puntos le faltan al promedio para llegar a 10 (nota máxima)

**Ejemplo:** Para `nota1 = 8`, `nota2 = 7`, `nota3 = 9` el output deberá ser:

```
8.0
9
7
2.0
```

---

### Ejercicio 12 - Área de Triángulo

**Archivo:** `exercise_triangle.py`

**Objetivo:** Aplicar fórmula geométrica del triángulo.

Dados la base y la altura de un triángulo, calcular e imprimir:
1. El área del triángulo: `(base × altura) / 2`

**Ejemplo:** Para `base = 10` y `altura = 6` el output deberá ser:

```
30.0
```

---

### Ejercicio 13 - Conversión de Moneda

**Archivo:** `exercise_currency.py`

**Objetivo:** Practicar conversiones con tasas de cambio.

Dado un monto en pesos argentinos, convertir e imprimir:
1. El monto en dólares (usando una tasa de cambio)
2. El monto en euros (usando una tasa de cambio)
3. El monto en reales brasileños (usando una tasa de cambio)

**Ejemplo:** Para `pesos = 10000`, `tasa_dolar = 350`, `tasa_euro = 380`, `tasa_real = 70` el output deberá ser (aproximado):

```
28.571428571428573
26.31578947368421
142.85714285714286
```

---

## 💡 Tips y Buenas Prácticas

### Nombres de Variables
- Usá nombres descriptivos: `precio_total` es mejor que `pt`
- Usá snake_case para nombres de variables: `numero_total` en lugar de `numeroTotal`
- Evitá nombres de una sola letra excepto para contadores o coordenadas (x, y, i, j)

### Comentarios
- Agregá comentarios para explicar cálculos complejos
- No comentes cosas obvias: `x = 5  # asigno 5 a x` ❌
- Comentá el "por qué", no el "qué": `# Convertimos a Fahrenheit para el reporte` ✅

### Formato del Código
- Dejá espacios alrededor de operadores: `a + b` en lugar de `a+b`
- Dejá una línea en blanco entre secciones lógicas del código
- Usá 4 espacios para indentación (Python es estricto con esto)

### Debugging
- Si tu output no coincide con el esperado, verificá:
  1. El orden de las operaciones (paréntesis si es necesario)
  2. El tipo de división: `/` vs `//`
  3. El orden de los prints
  4. Los nombres de las variables

### Testing Manual
Antes de ejecutar tu código:
1. Leé el código línea por línea
2. Anotá en papel qué valor tendrá cada variable
3. Predicí el output
4. Ejecutá y compará con tu predicción
5. Si no coincide, revisá tu razonamiento

---

## 📦 Estructura del Proyecto

```
POC/
├── README.md                    # Este archivo
├── exercise_math.py             # Ejercicio 1
├── exercise_rectangle.py        # Ejercicio 2
├── exercise_temperature.py      # Ejercicio 3
├── exercise_time.py             # Ejercicio 4
├── exercise_statistics.py       # Ejercicio 5
├── exercise_circle.py           # Ejercicio 6 (adicional)
├── exercise_length.py           # Ejercicio 7 (adicional)
├── exercise_price.py            # Ejercicio 8 (adicional)
├── exercise_swap.py             # Ejercicio 9 (adicional)
├── exercise_age.py              # Ejercicio 10 (adicional)
├── exercise_grades.py           # Ejercicio 11 (adicional)
├── exercise_triangle.py         # Ejercicio 12 (adicional)
└── exercise_currency.py         # Ejercicio 13 (adicional)
```

---

## 🤔 Preguntas Frecuentes

**P: ¿Puedo usar funciones como `max()`, `min()`, `abs()`?**
R: Sí, podés usar todas las funciones integradas de Python que no requieran estructuras de control.

**P: ¿Cómo imprimo varios valores en una misma línea?**
R: Podés usar: `print(valor1, valor2, valor3)` o concatenar: `print(str(valor1) + " " + str(valor2))`

**P: ¿Puedo crear mis propias variables auxiliares?**
R: ¡Sí! De hecho, es una buena práctica para hacer el código más legible.

**P: Mi resultado tiene muchos decimales, ¿está bien?**
R: Sí, Python muestra todos los decimales por defecto. Si querés redondear, podés usar `round(numero, decimales)`.

**P: ¿Qué hago si mi código no funciona?**
R:
1. Leé el mensaje de error completo
2. Verificá que todas las variables estén bien escritas
3. Verificá los paréntesis y operadores
4. Ejecutá el código línea por línea mentalmente
5. Agregá prints intermedios para ver valores

---

## 📚 Recursos Adicionales

- [Documentación oficial de Python (en español)](https://docs.python.org/es/3/)
- [Python para principiantes](https://www.python.org/about/gettingstarted/)
- [Real Python - Basic Data Types](https://realpython.com/python-data-types/)

---

## ✅ Checklist de Entrega

Antes de entregar, verificá que:
- [ ] Todos los ejercicios requeridos están completos
- [ ] El output de cada ejercicio coincide con el ejemplo
- [ ] El código está correctamente indentado
- [ ] No hay errores de sintaxis
- [ ] Los nombres de variables son descriptivos
- [ ] Agregaste comentarios donde sea necesario

---

**¡Buena suerte con el TP! 🚀**

Si tenés dudas, consultá con tus docentes o compañeros de clase.
