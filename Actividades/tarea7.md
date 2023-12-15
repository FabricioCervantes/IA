# Tarea 7

En el contexto de abordar problemas complejos, encontrar una solución óptima puede ser un desafío considerable. Las estrategias convencionales para resolver problemas suelen buscar métodos específicos y estructurados, buscando un camino claro y comprensible hacia la solución. No obstante, este enfoque puede incrementar de manera significativa la dificultad de encontrar una solución efectiva, llevando a veces a procesos que son poco prácticos o ineficientes.

Frecuentemente, para un problema dado, existen diversas vías para llegar a una solución. Aunque puede haber un método más eficiente, en ocasiones se pueden adoptar enfoques menos eficaces pero más sencillos y fáciles de entender. Estas soluciones más intuitivas a menudo surgen de la facilidad relativa con la que se pueden idear, aunque existan alternativas más avanzadas.

Es aquí donde las estrategias heurísticas desempeñan un papel crucial. Las heurísticas buscan tomar un problema complejo y desglosarlo en una versión más manejable. Estas estrategias no necesariamente apuntan a encontrar la solución más eficaz, sino que se centran en identificar los componentes clave necesarios para abordar el problema.

Usando heurísticas, es posible alcanzar soluciones satisfactorias que son relativamente fáciles de entender e implementar de manera eficiente, aunque no sean las más óptimas.

Ejemplo de Solución Heurística: Navegación en un Laberinto

Consideremos el desafío de navegar un laberinto con una entrada y salida definidas, evitando atravesar los muros. La estrategia consiste en simplificar el laberinto representándolo como una matriz binaria, donde los unos simbolizan muros y los ceros caminos transitables.

El método inicia en una coordenada específica, que funciona como entrada del laberinto. Se procede a explorar los espacios adyacentes en un plano cartesiano, es decir, moviéndose arriba, abajo, izquierda y derecha, comprobando si esos espacios están disponibles para el tránsito.

Una vez examinados los cuatro espacios adyacentes, se selecciona aquel con el valor más bajo para avanzar hacia él. El espacio previamente ocupado recibe un valor incrementado ligeramente, indicando una prioridad más baja, pero manteniendo la posibilidad de regresar si es necesario.

Así, a medida que se avanza, los caminos explorados adquieren valores incrementales, como 0.1 o 0.2, hasta que se encuentra un muro que obliga a retroceder o se llega a la salida. La salida se identifica buscando coordenadas en los bordes del laberinto que tengan un valor de cero o el valor máximo permitido por la matriz, lo que indica una posición en el borde distinta de la entrada, y por tanto, la salida exitosa del laberinto.

Si la salida no se encuentra, el algoritmo retorna a la entrada original, permitiendo la reevaluación de rutas no exploradas. Esta estrategia heurística, aunque no garantiza la ruta más rápida o eficiente, proporciona una solución viable y comprensible para navegar a través de laberintos complejos.

```

def explorar(laberinto, posicion_actual, entrada):
    fila_actual, columna_actual = posicion_actual
    total_filas, total_columnas = len(laberinto), len(laberinto[0])

    if 0 <= fila_actual < total_filas and 0 <= columna_actual < total_columnas:
        valor_arriba = laberinto[fila_actual - 1][columna_actual] if fila_actual - 1 >= 0 else float('inf')
        valor_abajo = laberinto[fila_actual + 1][columna_actual] if fila_actual + 1 < total_filas else float('inf')
        valor_izquierda = laberinto[fila_actual][columna_actual - 1] if columna_actual - 1 >= 0 else float('inf')
        valor_derecha = laberinto[fila_actual][columna_actual + 1] if columna_actual + 1 < total_columnas else float('inf')

        valor_minimo = min(valor_arriba, valor_abajo, valor_izquierda, valor_derecha)

        if valor_minimo == valor_arriba:
            proxima_posicion = fila_actual - 1, columna_actual
        elif valor_minimo == valor_abajo:
            proxima_posicion = fila_actual + 1, columna_actual
        elif valor_minimo == valor_izquierda:
            proxima_posicion = fila_actual, columna_actual - 1
        elif valor_minimo == valor_derecha:
            proxima_posicion = fila_actual, columna_actual + 1
        
        if proxima_posicion[0] == 0 or proxima_posicion[0] == total_filas - 1:
            if proxima_posicion != entrada:
                return proxima_posicion
        if proxima_posicion[1] == 0 or proxima_posicion[1] == total_columnas - 1:
            if proxima_posicion != entrada:
                return proxima_posicion
        
        laberinto[fila_actual][columna_actual] += 0.1
        
        return explorar(laberinto, proxima_posicion, entrada)

    return None

laberinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
]

posicion_inicial = (7, 0)

final = explorar(laberinto, posicion_inicial, posicion_inicial)
print("Entrada: ", posicion_inicial, "\nSalida:  ", final)

```

El algoritmo diseñado para resolver laberintos utiliza una estrategia recursiva y se implementa como un código ejecutable en Python. Este enfoque algorítmico se basa en la recursión, lo que significa que la función se llama a sí misma cada vez que avanza a un nuevo espacio dentro del laberinto.

Para que el algoritmo funcione eficazmente, necesita información crucial: una matriz que representa el laberinto, una posición actual que indica la ubicación en la matriz, y una coordenada de entrada que se utiliza para diferenciar la salida más tarde en el proceso.