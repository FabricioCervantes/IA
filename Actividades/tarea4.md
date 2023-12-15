## Introducción

En la fascinante esfera de la programación informática, las computadoras poseen una notable capacidad para procesar y analizar una amplia gama de conjuntos de datos. Estos conjuntos de datos son interpretados a través de una base binaria, constituida por ceros y unos, que forman el núcleo de su lógica operativa. El entendimiento profundo de este sistema se cimienta en el concepto fundamental de las matrices. En este marco conceptual, las computadoras son capaces de discernir y procesar combinaciones complejas de elementos, que representan diversas dimensiones, desde la simplicidad de vectores unidimensionales hasta matrices de dimensiones extensas y casi infinitas. A través de este mecanismo, las computadoras son capaces de interpretar y navegar por estos espacios multidimensionales, que, aunque no son inherentes a su naturaleza básica, se han convertido en un campo esencial de su funcionamiento. En la computación, lo que se asume como "natural" es aquello que una computadora puede comprender de manera innata o para lo cual ha sido específicamente programada y diseñada. Este principio abre la puerta al desarrollo de programas y representaciones capaces de analizar estas estructuras matriciales, permitiendo así la resolución de problemas complejos asociados con espacios de esta índole. Concretamente, el desafío es crear un programa sofisticado que tenga la habilidad única de identificar y contar los elementos diferenciados dentro de un espacio bidimensional, representado por una matriz, considerada en este contexto como un vector de dos dimensiones.


## Desarrollo

El programa específico que buscamos desarrollar tiene el objetivo de contar islas dentro de una imagen dada. Para lograr este fin, se pueden utilizar las avanzadas librerías de Python, las cuales facilitan enormemente la tarea. Sin embargo, el desafío principal radica en la deducción lógica que se requiere previo a la implementación del programa. Este reto no implica un esfuerzo insuperable, ya que en esencia se trata de observar y analizar meticulosamente el espacio en el que se desenvuelven los problemas o, en este contexto particular, un juego. Esta tarea puede implicar la creación de una ruta específica, proporcionar instrucciones detalladas sobre cómo moverse dentro del espacio, o simplemente llevar a cabo un recuento preciso de los elementos presentes en él. Este proceso conlleva la habilidad de distinguir con claridad y eficiencia unos elementos de otros, incluso en escenarios donde estos presenten patrones, texturas o colores variados y complejos. La razón fundamental de nuestra destreza en esta capacidad radica en cómo los seres humanos estamos intrínsecamente "programados" o diseñados. De manera natural y casi instintiva, estamos equipados para diferenciar entre distintos elementos y reconocer colores, e incluso detalles finos que, en ciertas circunstancias, pueden representar un desafío considerable, incluso entre individuos de la misma especie. Esta capacidad nos otorga una habilidad notable para realizar distinciones y contar elementos, una habilidad que fue crucial para la supervivencia en comunidades antiguas y, más específicamente, para nuestros ancestros que dependían de esta habilidad de manera vital para su supervivencia y desarrollo.

Aunque en la actualidad seguimos utilizando esta habilidad innata, resulta aún más fascinante y desafiante desarrollar un enfoque lógico para enseñar a una entidad no biológica, es decir, una computadora, a contar elementos en un espacio bidimensional. Este desafío transforma un problema aparentemente sencillo en una tarea no tan instintiva de abordar para una máquina. Para ello, se hace necesario comprender en profundidad cómo la computadora interpreta y procesa el espacio que se le presenta o que simula, para así llegar a una deducción lógica sobre la resolución efectiva del ejercicio o problema en cuestión. Para abordar la solución de este desafío, es esencial considerar el uso de un enfoque iterativo y recursivo. Esto implica que el mismo modelo o instrucción para resolver el problema debe ser capaz de repetirse y utilizar sus propias instancias previas para abordar y solucionar el problema de manera efectiva. Por ejemplo, una instrucción tan simple como "dar un paso" puede convertirse en un proceso iterativo y recursivo al indicar a alguien que mueva primero el pie derecho y luego el izquierdo, repitiendo este proceso cada vez que se alterne, logrando así un avance constante y eficiente en línea recta. Esta misma lógica puede ser aplicada de manera análoga al programa de computadora que estamos desarrollando. Inicialmente, el programa recorrerá la matriz examinando cada uno de sus espacios y analizando detenidamente sus contenidos. La información a analizar en estos espacios puede ser de cualquier tipo, aunque, por conveniencia y simplicidad, en este caso la trataremos predominantemente como valores binarios (cero o uno). Bajo este enfoque, todos los espacios en la matriz tendrán un valor predeterminado de cero, mientras que aquellos con un valor de uno podrán formar "islas" dentro del contexto de la matriz. Las islas, en este caso, consistirán en valores que se encuentran próximos en el espacio bidimensional, conectados al menos por una de sus aristas. Desde la lógica más elemental y fundamental, es posible diseñar un programa que simplemente recorra la matriz y, al encontrar valores de cero, los ignore, mientras que, al hallar valores de uno, los contabilice y registre. Esto nos permitiría contar cuántos espacios en la matriz están ocupados, por ejemplo, por "tierra" dentro del contexto de una representación gráfica o simbólica.

Sin embargo, nuestro objetivo principal no es simplemente contar espacios individuales, sino identificar y contabilizar islas dentro del espacio bidimensional de la matriz. Esto implica, como se mencionó anteriormente, identificar espacios que están unidos al menos por una arista. Esta necesidad añade una capa significativa de complejidad al problema y exige aplicar otra capa de lógica en la resolución previamente desarrollada, para ser capaces de ignorar los elementos adyacentes al primero contado y continuar la exploración y el conteo sin importar la forma específica que pueda tener esa isla dentro del contexto de la matriz. Para abordar eficazmente esta segunda capa lógica, es crucial tener en cuenta el entorno de cada espacio contado dentro de la matriz. Podemos imaginarnos recorriendo la matriz sin ser capaces de visualizar los espacios circundantes hasta que efectivamente los pisamos o exploramos. En este escenario hipotético, sabemos la dirección que debemos tomar, pero desconocemos el color o el valor del espacio que vamos a pisar hasta que efectivamente lo hacemos. Para determinar la existencia de islas en este espacio bidimensional, podríamos adoptar la estrategia de, cada vez que encontramos un espacio con un valor específico (por ejemplo, un espacio negro que simboliza una isla), explorar los espacios adyacentes a este. Al hallar una isla negra, nos moveríamos alrededor de ella para verificar si hay otra isla negra adyacente o conectada. En cada desplazamiento a una isla, sería necesario revisar nuevamente los alrededores para asegurarnos de no pasar por alto ningún espacio sin examinar. Avanzaríamos en los ejes principales del espacio, buscando cada vez que nos movemos que no haya más islas en los mismos ejes del nuevo espacio al que nos trasladamos. Este proceso eventualmente nos llevaría a completar la evaluación exhaustiva de todas las islas presentes en la matriz. Una vez que hayamos evaluado todos los espacios, deberíamos registrar cuáles espacios ya fueron ocupados o tenidos en cuenta como parte de una isla y aumentar el contador de islas en consecuencia. Finalmente, regresaríamos al punto de partida. Sin embargo, en este punto, necesitaríamos una herramienta adicional: una lista o registro de los espacios que ya hemos cruzado o explorado. Anteriormente, simplemente contábamos cada vez que pisábamos un espacio con el valor o color que buscábamos, sin considerar su ubicación específica dentro de la matriz. Pero en la nueva implementación de la resolución del problema, esto ya no sería completamente útil o eficiente, ya que perderíamos la capacidad de saber con certeza qué espacios ya hemos tenido en cuenta, lo que resultaría en el recuento repetido de islas en cada avance, con pasos adicionales y redundantes. 

<!-- linea de codigo -->
```
import cv2
import numpy as np

def contar_islas(imagen_path, umbral_diferencia=50):
    imagen = cv2.imread(imagen_path)
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Aplicar umbral para obtener una imagen binaria
    _, umbral = cv2.threshold(gris, 128, 255, cv2.THRESH_BINARY)

    # Dilatar la imagen en la dirección horizontal
    kernel_horizontal = np.ones((1, 5), np.uint8)
    dilatacion_horizontal = cv2.dilate(umbral, kernel_horizontal, iterations=1)

    # Detección de bordes
    bordes = cv2.Canny(dilatacion_horizontal, 50, 150, apertureSize=3)

    # Detectar líneas horizontales
    lineas_horizontales = cv2.HoughLines(bordes, 1, np.pi / 180, threshold=100,
                                        min_theta=np.pi / 4, max_theta=3 * np.pi / 4)

    # Detectar líneas verticales
    lineas_verticales = cv2.HoughLines(bordes, 1, np.pi / 180, threshold=100,
                                      min_theta=-np.pi / 4, max_theta=np.pi / 4)

    # Contar cruces de líneas para determinar el número de islas
    if lineas_horizontales is not None and lineas_verticales is not None:
        contador_islas =-2+len(lineas_horizontales)*len(lineas_verticales)
    else:
        contador_islas = 0

    return contador_islas

ruta_imagen = r'C:\xampp\htdocs\IA\imagentarea2\cap.png'

islas_contadas = contar_islas(ruta_imagen)

print(f'Número de islas: {islas_contadas}')
```