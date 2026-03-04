# Trabajo Práctico 1

## Ejercicio 1

Para este ejercicio el objetivo es leer el código, anotar lo que piensen que los prints vayan a decir y luego correr el código para ver si les dio igual o no.

```python
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

s1, s2, s3 = "Python", " is ", 'awesome'
print(s1 + s2 + s3)

x = y = z = "Naranja"
print("valor de x: " + x + ", valor de y: " + y + ", valor de z: " + z)

z1 = i3 / i2
print(z1)
z2 = i3 % i2
print(z2)
f1 = -.5
f2 = 10
f3 = f1 + f2
i3 = int(f3)
print("entero i3:")
print(i3)
print("variable f3:")
print(f3)
f2 += i1
print("el valor de")
print(f2)
print("más")
print(f1)
print("es:")
print(f2 + f1)

```

## Ejercicio 2 - Math

Escribir un programa dentro de exercise_math.py que dado dos números enteros imprima en pantalla el resultado de las siguientes operaciones: la suma, la diferencia, el producto, el promedio, el cociente entero y el resto de la división entera y el valor real de la división. Para entregar correctamente se deberá imprimir dichos resultados en el orden que fueron pedidos en la consigna. Por ejemplo, primero la suma, despues la diferencia, y asi sucesivamente.

Ejemplo: Para a = 57 y b = 7 el output debera ser:

```python
64
50
399
32.0
8
1
8.142857142857142
```

## Ejercicio 3 - Geometría de Rectángulo

Escribir un programa dentro de `exercise_rectangle.py` que dado un rectángulo con base y altura, imprima en pantalla:
1. El área del rectángulo (base × altura)
2. El perímetro del rectángulo (2 × base + 2 × altura)

Los resultados deben imprimirse en el orden pedido: primero el área, después el perímetro y como números enteros.

Ejemplo: Para base = 10 y altura = 5 el output deberá ser:

```python
50
30
```

## Ejercicio 4 - Conversión de Temperatura

Escribir un programa dentro de `exercise_temperature.py` que dada una temperatura en grados Celsius, imprima:
1. La temperatura convertida a Fahrenheit usando la fórmula: F = C × 9/5 + 32
2. La temperatura original en Celsius (para practicar el uso de variables)

Los resultados deben imprimirse en el orden pedido y como números decimales.

Ejemplo: Para celsius = 25 el output deberá ser:

```python
77.0
25.0
```

**Nota**: La segunda línea debe imprimir el valor original de celsius (25), no el valor convertido.

## Ejercicio 5 - Calculadora de Tiempo

Escribir un programa dentro de `exercise_time.py` que dado un número total de segundos, calcule e imprima:
1. Cuántas horas completas hay (usando división entera)
2. Cuántos minutos completos quedan después de sacar las horas (usando módulo y división entera)
3. Cuántos segundos quedan después de sacar horas y minutos

Los resultados deben imprimirse en el orden pedido: horas, minutos, segundos.

Ejemplo: Para total_segundos = 3665 el output deberá ser:

```python
1
1
5
```

**Explicación**: 3665 segundos = 1 hora (3600 seg) + 1 minuto (60 seg) + 5 segundos

**Pista**: Usá el operador `//` para división entera y `%` para obtener el resto.

## Ejercicio 6 - Estadísticas Simples

Escribir un programa dentro de `exercise_statistics.py` que dados cuatro números, calcule e imprima:
1. El promedio de los cuatro números
2. El máximo de los cuatro números
3. El mínimo de los cuatro números
4. El rango (diferencia entre el máximo y el mínimo)

Los resultados deben imprimirse en el orden pedido.

Ejemplo: Para num1 = 15, num2 = 8, num3 = 23, num4 = 12 el output deberá ser:

```python
14.5
23
8
15
```

**Pista**: Para encontrar el máximo de dos números a y b, recordá que si a > b, entonces el máximo es a. Pero como todavía no vimos condicionales (if), tenés que pensar en cómo combinar comparaciones. Una forma es usar variables intermedias:
- Primero encontrá el máximo entre num1 y num2
- Luego el máximo entre ese resultado y num3
- Finalmente el máximo entre ese resultado y num4

Otra opción más simple: Python tiene funciones integradas `max()` y `min()` que aceptan múltiples argumentos:

```python
maximo = max(num1, num2, num3, num4)
minimo = min(num1, num2, num3, num4)
```


