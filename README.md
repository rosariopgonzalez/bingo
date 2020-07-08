[![Build Status](https://travis-ci.org/rosariopgonzalez/bingo.svg?branch=master)](https://travis-ci.org/rosariopgonzalez/bingo)
[![Coverage Status](https://coveralls.io/repos/github/rosariopgonzalez/bingo/badge.svg)](https://coveralls.io/github/rosariopgonzalez/bingo)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/rosariopgonzalez/bingo/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/rosariopgonzalez/bingo/?branch=master)

### Proyecto para Adaptación del Ambiente de Trabajo, Instituto Politécnico Superior. 

# BINGO

## Reglas que hacen que un cartón sea considerado válido:
* Los números del carton se encuentran en el rango 1 a 90.
* Cada columna de un carton (contando de izquierda a derecha) contiene numeros que van del 1 al 9, 10 al 19, 20 al 29 ..., 70 al 79 y 80 al 90.
* No hay números repetidos en el carton.
* Cada fila de un carton tiene exactamente 5 celdas ocupadas.
* Cada carton es una matrix de 3 x 9.
* Cada carton tiene 15 celdas ocupadas.
* Los números de las columnas izquierdas son menores que los de las columnas a la derecha.
* Para una misma columna, sus números están ordenados de menor a mayor de arriba hacia abajo.
* No pueden existir columnas vacias.
* No pueden existir columnas con sus tres celdas ocupadas.
* Cada carton debe tener 3 y solo 3 columas con solo una celda ocupada.
* En una fila no existen más de dos celdas vacías consecutivas.
* En una fila no existen más de dos celdas ocupadas consecutivas.

## Ejemplo de cartón válido
(3,0,0,31,42,0,66,0,89), 
(0,11,0,34,0,53,0,73,90), 
(0,17,29,0,47,0,0,77,0)
