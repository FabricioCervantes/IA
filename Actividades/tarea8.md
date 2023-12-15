# Tarea 8

## Ranas

En el juego de las ranas, el objetivo es reorganizar tres ranas verdes y tres ranas marrones en un tablero de siete posiciones, moviéndolas hacia la derecha y la izquierda respectivamente. Las ranas pueden saltar a una piedra vacía adyacente o sobre otra rana si hay una piedra vacía en el medio. La representación del estado se realiza mediante una cadena de caracteres que indica la posición de las ranas y las piedras vacías. El desafío consiste en encontrar una secuencia de movimientos que cumpla con el objetivo final, respetando las reglas establecidas.

| R | R | R |   | V | V | V |
|---|---|---|---|---|---|---|
| R | R |   | R | V | V | V |
| R | R | V | R |   | V | V |
| R | R | V | R | V |   | V |
| R | R | V |   | V | R | V |
| R |   | V | R | V | R | V |
|   | R | V | R | V | R | V |
| V | R |   | R | V | R | V |
| V | R | V | R |   | R | V |
| V | R | V | R | V | R |   |
| V | R | V | R | V |   | R |
| V | R | V |   | V | R | R |
| V |   | V | R | V | R | R |
| V | V |   | R | V | R | R |
| V | V | V | R |   | R | R |
| V | V | V |   | R | R | R |

## Misioneros y caníbales

En el problema de los tres misioneros y tres caníbales, el objetivo es cruzar un río utilizando un bote con capacidad para dos personas. Los misioneros no deben quedar en minoría en ninguna orilla con los caníbales, ya que en ese caso los caníbales los devorarían. La tarea es encontrar una secuencia de movimientos que lleve a todos al otro lado del río sin violar esta condición. La complejidad radica en planificar movimientos cuidadosos para evitar situaciones peligrosas mientras se cruza el río. Este problema es un clásico ejemplo de juego estratégico y se aborda comúnmente con algoritmos de búsqueda para encontrar la solución óptima.

1. Inician con dos caníbales cruzando el río (quedando 1 misionero y 1 caníbal en la orilla inicial, y 2 caníbales en la orilla opuesta).

2. Un caníbal regresa a la orilla inicial (quedando 1 misionero, 2 caníbales en la orilla inicial, y 1 caníbal en la orilla opuesta).

3. Dos caníbales cruzan el río (quedando 1 misionero en la orilla inicial, y 3 caníbales en la orilla opuesta).

4. Un caníbal regresa a la orilla inicial (quedando 1 misionero, 1 caníbal en la orilla inicial, y 2 caníbales en la orilla opuesta).

5. Dos misioneros cruzan el río (quedando 1 caníbal en la orilla inicial, y 2 misioneros y 2 caníbales en la orilla opuesta).

6. Un caníbal regresa a la orilla inicial (quedando 2 caníbales en la orilla inicial, y 2 misioneros y 1 caníbal en la orilla opuesta).

7. Dos misioneros cruzan el río (quedando 2 caníbales en la orilla inicial, y 4 misioneros y 1 caníbal en la orilla opuesta).

8. Un caníbal regresa a la orilla inicial (quedando 3 caníbales en la orilla inicial, y 4 misioneros en la orilla opuesta).

9. Dos caníbales cruzan el río (quedando 1 caníbal en la orilla inicial, y 4 misioneros y 3 caníbales en la orilla opuesta).

10. Un caníbal regresa a la orilla inicial (quedando 2 caníbales en la orilla inicial, y 4 misioneros y 2 caníbales en la orilla opuesta).

11. Dos caníbales cruzan el río (quedando 0 caníbales en la orilla inicial, y 4 misioneros y 4 caníbales en la orilla opuesta).
