**Nombre:** Marco Fabricio Cervantes Cadenas  
**Correo:** 19121009@morelia.tecnm.mx  
**Matrícula:** 19121009

# Proyectos de Inteligencia Artificial

Este repositorio contiene varios proyectos desarrollados para la materia de Inteligencia Artificial. Los proyectos incluyen dos juegos desarrollados con Phaser y redes neuronales, un modelo de CNN para la detección de robos, incendios, robos a casa habitación, incendios e inundaciones, un sistema de reconocimiento de emociones usando LBPH y un proyecto de "Buscando a Wally" utilizando Haar Cascade.

Enlace a la carpeta con los archivos: [Carpeta de Proyectos de Inteligencia Artificial](https://drive.google.com/drive/folders/1i2y4aBbO-j0Q8QjTYZg3OW6puGhXqCZE?usp=sharing)

## Contenidos

- [Proyectos de Inteligencia Artificial](#proyectos-de-inteligencia-artificial)
  - [Contenidos](#contenidos)
  - [Phaser con 3 balas](#phaser-con-3-balas)
    - [`preload`](#preload)
    - [`create`](#create)
    - [`update`](#update)
    - [`pausa`](#pausa)
    - [`mPausa`](#mpausa)
    - [`enRedNeural`](#enredneural)
    - [`datosDeEntrenamiento`](#datosdeentrenamiento)
  - [Phaser con rebote](#phaser-con-rebote)
    - [`preload`](#preload-1)
    - [`create`](#create-1)
    - [`update`](#update-1)
    - [`adjustBallAngle`](#adjustballangle)
    - [`reiniciarPelotas`](#reiniciarpelotas)
  - [Detección de Eventos con CNN](#detección-de-eventos-con-cnn)
    - [Cargar las Imágenes de Entrenamiento y Pruebas](#cargar-las-imágenes-de-entrenamiento-y-pruebas)
    - [Preprocesamiento de Imágenes](#preprocesamiento-de-imágenes)
    - [Construcción del Modelo](#construcción-del-modelo)
    - [Compilación del Modelo](#compilación-del-modelo)
    - [Ajuste del Modelo](#ajuste-del-modelo)
    - [Evaluación del Modelo](#evaluación-del-modelo)
    - [Función de Clasificación](#función-de-clasificación)
    - [Prueba con Nuevas Imágenes](#prueba-con-nuevas-imágenes)
    - [Visualización de Resultados](#visualización-de-resultados)
    - [Ejemplos de Clasificación](#ejemplos-de-clasificación)
  - [Reconocimiento de Emociones con LBPH](#reconocimiento-de-emociones-con-lbph)
    - [Configuración de la Cámara](#configuración-de-la-cámara)
    - [Carga y Preprocesamiento de Datos](#carga-y-preprocesamiento-de-datos)
      - [Carga de Imágenes de Entrenamiento](#carga-de-imágenes-de-entrenamiento)
      - [Preprocesamiento de Imágenes](#preprocesamiento-de-imágenes-1)
    - [Entrenamiento del Modelo LBPH](#entrenamiento-del-modelo-lbph)
      - [Creación del Modelo](#creación-del-modelo)
      - [Entrenamiento del Modelo](#entrenamiento-del-modelo)
    - [Detección de Emociones en Tiempo Real](#detección-de-emociones-en-tiempo-real)
      - [Captura de Imágenes en Tiempo Real](#captura-de-imágenes-en-tiempo-real)
      - [Detección de Caras](#detección-de-caras)
      - [Predicción de Emociones](#predicción-de-emociones)
    - [Visualización de Resultados](#visualización-de-resultados-1)
      - [Mostrar Resultados en Tiempo Real](#mostrar-resultados-en-tiempo-real)
      - [Ejemplos de Detección](#ejemplos-de-detección)
  - [Buscando a Wally con Haar Cascade](#buscando-a-wally-con-haar-cascade)
    - [Creación del Archivo de Negativos](#creación-del-archivo-de-negativos)
    - [Creación del Archivo de Positivos](#creación-del-archivo-de-positivos)
    - [Creación de Muestras y Entrenamiento del Clasificador](#creación-de-muestras-y-entrenamiento-del-clasificador)
    - [Prueba del Clasificador](#prueba-del-clasificador)
    - [Evaluación en un Conjunto de Datos](#evaluación-en-un-conjunto-de-datos)

## Phaser con 3 balas

### `preload`

**Descripción:**
La función `preload` se encarga de cargar todos los recursos gráficos necesarios para el juego, como imágenes de fondo, sprites del personaje y de la nave, y otros elementos. 

### `create`

    function  create()  {
    
    juego.physics.startSystem(Phaser.Physics.ARCADE);
    
    juego.physics.arcade.gravity.y =  800;
    
    juego.time.desiredFps =  30;
    
      
    
    fondo  =  juego.add.tileSprite(0,  0,  w,  h,  "fondo");
    
    nave  =  juego.add.sprite(w  -  100,  h  -  70,  "nave");
    
    bala  =  juego.add.sprite(w  -  100,  h,  "bala");
    
    balaFall =  juego.add.sprite(50,  h  -  500,  "bala");
    
    balaDiagonal =  juego.add.sprite(w  -  300,  10,  "bala");
    
      
    
    naveFall =  juego.add.sprite(50,  0,  "nave");
    
    jugador  =  juego.add.sprite(50,  h,  "mono");
    
      
    
    juego.physics.enable(jugador);
    
    jugador.body.collideWorldBounds =  true;
    
    var  corre  =  jugador.animations.add("corre", [8,  9,  10,  11]);
    
    jugador.animations.play("corre",  10,  true);
    
      
    
    juego.physics.enable(bala);
    
    juego.physics.enable(balaFall);
    
    juego.physics.enable(naveFall);
    
    juego.physics.enable(balaDiagonal);
    
    naveFall.body.collideWorldBounds =  true;
    
    bala.body.collideWorldBounds =  true;
    
    balaFall.body.collideWorldBounds =  true;
    
    naveFall.body.allowGravity =  false;
    
      
    
    naveDiagonal =  juego.add.sprite(w  -  100,  5,  "nave");
    
    balaDiagonal.body.collideWorldBounds =  true;
    
    balaDiagonal.body.allowGravity =  false;
    
      
    
    moveLeft  =  juego.input.keyboard.addKey(Phaser.Keyboard.LEFT);
    
    moveRight  =  juego.input.keyboard.addKey(Phaser.Keyboard.RIGHT);
    
      
    
    pausaL =  juego.add.text(w  -  100,  20,  "Pausa",  {
    
    font:  "20px Arial",
    
    fill:  "#fff",
    
    });
    
    pausaL.inputEnabled =  true;
    
    pausaL.events.onInputUp.add(pausa,  self);
    
    juego.input.onDown.add(mPausa,  self);
    
      
    
    salto  =  juego.input.keyboard.addKey(Phaser.Keyboard.UP);
    
      
    
    nnNetwork  =  new synaptic.Architect.Perceptron(4,  8,  8,  2);
    
    nnEntrenamiento  =  new synaptic.Trainer(nnNetwork);
    
    }

**Descripción:**
La función `create` inicializa el sistema de física del juego, configura la gravedad y los frames por segundo deseados. También crea y posiciona los sprites del fondo, las naves, las balas y el jugador. Configura las animaciones del jugador y define los controles del teclado para moverse y saltar. Además, inicializa la red neuronal que se utilizará para el modo automático del juego.

### `update`
    function update() {
    fondo.tilePosition.x -= 1;

    juego.physics.arcade.collide(bala, jugador, colisionH, null, this);
    juego.physics.arcade.collide(balaFall, jugador, colisionH, null, this);
    juego.physics.arcade.collide(balaDiagonal, jugador, colisionH, null, this);
    estatusSalto = 0;
    estatusAdelante = 0;

    if (!jugador.body.onFloor()) {
        estatusSalto = 1;
    }

    if (balaDiagonal.body.onFloor()) {
        resetBalaDiagonal();
    } else if (!balaDiagonalD) {
        launchBalaDiagonal();
    }

    despBala = Math.floor(jugador.position.x - bala.position.x);
    despBalaY = Math.floor(jugador.position.y - balaFall.position.y);
    difBalaY = Math.floor(jugador.position.x - balaFall.position.x);

    if (!isFalling) {
        resetFall(jugador.position.x);
    }

    if (!balaDiagonal.body.velocity.y) {
        balaDiagonal.body.velocity.x = -200;
        balaDiagonal.body.velocity.y = 200;
    }

    naveFall.position.x = balaFall.position.x;
    naveFall.position.y = 0;

    if (modoAuto == false && moveRight.isDown) {
        jugador.body.velocity.x = 200;
        estatusAdelante = 1;
        moveBack++;
    } else if (modoAuto == false && moveBack > 0) {
        jugador.body.velocity.x = -200;
        moveBack--;
    } else if (modoAuto == false) {
        jugador.body.velocity.x = 0;
    } else {
        if (modoAuto == true) {
        var bot = datosDeEntrenamiento([
            despBala,
            velocidadBala,
            despBalaY,
            difBalaY,
        ]);
        if (bot[0] > 0.6 && jugador.body.onFloor()) {
            saltar();
        }
        if (Math.abs(bot[1]) > 0.6) {
            jugador.body.velocity.x = 200;
            moveBack++;
            console.log("moveback->", moveBack);
        } else if (moveBack > 0) {
            jugador.body.velocity.x = -200;
            moveBack--;
            console.log("moveback<-", moveBack);
        } else {
            jugador.body.velocity.x = 0;
            console.log("moveback", moveBack);
        }
        }
    }

    if (modoAuto == false && salto.isDown && jugador.body.onFloor()) {
        saltar();
    }

    if (balaD == false) {
        disparo();
    }

    if (bala.position.x <= 0) {
        resetVariables();
    }

    if (balaFall.body.onFloor()) {
        isFalling = false;
    }

    if (modoAuto == false && bala.position.x > 0) {
        datosEntrenamiento.push({
        input: [despBala, velocidadBala, despBalaY, difBalaY],
        output: [estatusSalto, estatusAdelante],
        });
    }
    }

**Descripción:**
La función `update` es llamada en cada frame del juego y se encarga de actualizar el estado del juego. Gestiona el movimiento de los sprites, detecta colisiones y maneja la lógica del movimiento automático del jugador utilizando la red neuronal. También recopila datos de entrenamiento durante el juego manual para mejorar la precisión del modo automático.

### `pausa`

    function pausa() {
    juego.paused = true;
    menu = juego.add.sprite(w / 2, h / 2, "menu");
    menu.anchor.setTo(0.5, 0.5);
    }
**Descripción:**
La función `pausa` detiene el juego y muestra un menú de pausa en la pantalla. Esta función permite cambiar entre el modo manual y el modo automático 

### `mPausa`
    function mPausa(event) {
    if (juego.paused) {
        var menu_x1 = w / 2 - 270 / 2,
        menu_x2 = w / 2 + 270 / 2,
        menu_y1 = h / 2 - 180 / 2,
        menu_y2 = h / 2 + 180 / 2;

        var mouse_x = event.x,
        mouse_y = event.y;

        if (
        mouse_x > menu_x1 &&
        mouse_x < menu_x2 &&
        mouse_y > menu_y1 &&
        mouse_y < menu_y2
        ) {
        if (
            mouse_x >= menu_x1 &&
            mouse_x <= menu_x2 &&
            mouse_y >= menu_y1 &&
            mouse_y <= menu_y1 + 90
        ) {
            eCompleto = false;
            datosEntrenamiento = [];
            modoAuto = false;
        } else if (
            mouse_x >= menu_x1 &&
            mouse_x <= menu_x2 &&
            mouse_y >= menu_y1 + 90 &&
            mouse_y <= menu_y2
        ) {
            if (!eCompleto) {
            console.log(
                "",
                "Entrenamiento " + datosEntrenamiento.length + " valores"
            );
            enRedNeural();
            eCompleto = true;
            }
            modoAuto = true;
        }

        menu.destroy();
        resetFall(50);
        resetVariables();
        juego.paused = false;
    }
  }
}

**Descripción:**
La función `mPausa` maneja la lógica para reanudar el juego desde el estado de pausa. Detecta la posición del clic del mouse y determina si el juego debe reiniciar el entrenamiento de la red neuronal o activar el modo automático, basándose en la interacción del usuario con el menú de pausa.

### `enRedNeural`

    function enRedNeural() {
    nnEntrenamiento.train(datosEntrenamiento, {
        rate: 0.0003,
        iterations: 10000,
        shuffle: true,
    });
    }

**Descripción:**
La función `enRedNeural` entrena la red neuronal utilizando los datos recopilados durante el juego. Configura los parámetros de entrenamiento, como la tasa de aprendizaje y el número de iteraciones, para mejorar la capacidad de la red neuronal de predecir las acciones del jugador en el modo automático.

### `datosDeEntrenamiento`

    function datosDeEntrenamiento(param_entrada) {
    console.log(
        "Entrada",
        param_entrada[0] +
        " " +
        param_entrada[1] +
        " " +
        param_entrada[2] +
        " " +
        param_entrada[3]
    );
    nnSalida = nnNetwork.activate(param_entrada);
    var salto = Math.round(nnSalida[0] * 100);
    var adelante = Math.round(nnSalida[1] * 100);
    console.log("Valor ", "En el salto %: " + salto);
    console.log("Valor ", " Adelante %: " + adelante);
    var salidas = [];
    salidas[0] = nnSalida[0];
    salidas[1] = nnSalida[1];
    return salidas;
    }

**Descripción:**
La función `datosDeEntrenamiento` toma un conjunto de parámetros de entrada y los pasa a través de la red neuronal, devolviendo las salidas correspondientes.

## Phaser con rebote



### `preload`

La función preload en ambos códigos carga los recursos gráficos necesarios, pero en este caso específico, se carga una imagen para las pelotas rebotantes en lugar de balas y naves.

    function preload() {
    juego.load.image("fondo", "assets/game/fondo.jpg");
    juego.load.spritesheet("mono", "assets/sprites/altair.png", 32, 48);
    juego.load.image("pelota", "assets/sprites/purple_ball.png");
    juego.load.image("menu", "assets/game/menu.png");
    }

### `create`

La función create en este código no configura la gravedad ya que las pelotas rebotan en todas las direcciones sin caer hacia abajo. Además, se crean múltiples pelotas que rebotan dentro de los límites del juego. Aquí se detallan las configuraciones específicas para las pelotas:

- Gravedad: No se utiliza gravedad (juego.physics.arcade.gravity.y = 0).
- Pelotas rebotantes: Se crean y configuran varias pelotas que rebotan dentro de los límites del juego con pelota.body.bounce.set(1).

        function create() {
        juego.physics.startSystem(Phaser.Physics.ARCADE);
        juego.physics.arcade.gravity.y = 0;

        fondo = juego.add.tileSprite(0, 0, w, h, "fondo");
        jugador = juego.add.sprite(w / 2, h / 2, "mono");
        jugador.anchor.setTo(0.5, 0.5);

        juego.physics.enable(jugador);
        jugador.body.collideWorldBounds = true;

        var corre = jugador.animations.add("corre", [8, 9, 10, 11]);
        jugador.animations.play("corre", 10, true);

        moveUp = juego.input.keyboard.addKey(Phaser.Keyboard.UP);
        moveDown = juego.input.keyboard.addKey(Phaser.Keyboard.DOWN);
        moveLeft = juego.input.keyboard.addKey(Phaser.Keyboard.LEFT);
        moveRight = juego.input.keyboard.addKey(Phaser.Keyboard.RIGHT);

        pausaL = juego.add.text(w - 100, 20, "Pausa", {
            font: "20px Arial",
            fill: "#fff",
        });
        pausaL.inputEnabled = true;
        pausaL.events.onInputUp.add(pausa, self);
        juego.input.onDown.add(mPausa, self);

        nnNetwork = new synaptic.Architect.Perceptron(4, 8, 8, 4);
        nnEntrenamiento = new synaptic.Trainer(nnNetwork);

        for (var i = 0; i < numPelotas; i++) {
            var pelota = juego.add.sprite(
            Math.random() * w,
            Math.random() * h,
            "pelota"
            );
            juego.physics.enable(pelota);
            pelota.body.collideWorldBounds = true;
            pelota.body.bounce.set(1);
            pelota.body.velocity.setTo(
            velocidadRandom(velocidadPelotas, velocidadPelotas + 200),
            velocidadRandom(velocidadPelotas, velocidadPelotas + 200)
            );
            pelota.body.onCollide = new Phaser.Signal();
            pelota.body.onCollide.add(adjustBallAngle, this);
            pelotas.push(pelota);
        }
        }

### `update`

La función update gestiona el movimiento del jugador y las colisiones con las pelotas. En comparación con el código de las balas, este código no maneja la lógica de diferentes tipos de balas (caídas, diagonales, etc.). En su lugar, maneja múltiples pelotas rebotando y recoge datos de entrenamiento diferentes:


    function update() {
    fondo.tilePosition.x -= 1;

    if (modoAuto) {
        jugador.body.velocity.x = 0;
        jugador.body.velocity.y = 0;

        var datosEntrada = [];
        pelotas.forEach(function (pelota) {
        datosEntrada.push(jugador.position.x - pelota.position.x);
        datosEntrada.push(jugador.position.y - pelota.position.y);
        datosEntrada.push(pelota.body.velocity.x);
        datosEntrada.push(pelota.body.velocity.y);
        });
        datosEntrada.push(jugador.position.x);
        datosEntrada.push(jugador.position.y);
        datosEntrada.push(jugador.body.velocity.x);
        datosEntrada.push(jugador.body.velocity.y);

        if (pelotas.length > 0) {
        var salidas = datosDeEntrenamiento(datosEntrada);
        var movimientoY = salidas[0] > 0.7 ? -200 : salidas[1] > 0.7 ? 200 : 0;
        var movimientoX = salidas[2] > 0.7 ? -200 : salidas[3] > 0.7 ? 200 : 0;

        jugador.body.velocity.y = movimientoY;
        jugador.body.velocity.x = movimientoX;

        console.log("Modo Automático - Movimiento: ", {
            arriba: movimientoY === -200,
            abajo: movimientoY === 200,
            izquierda: movimientoX === -200,
            derecha: movimientoX === 200,
        });
        }
    } else {
        jugador.body.velocity.x = 0;
        jugador.body.velocity.y = 0;

        if (moveUp.isDown) {
        jugador.body.velocity.y = -200;
        }
        if (moveDown.isDown) {
        jugador.body.velocity.y = 200;
        }
        if (moveLeft.isDown) {
        jugador.body.velocity.x = -200;
        }
        if (moveRight.isDown) {
        jugador.body.velocity.x = 200;
        }

        var datosEntrada = [];
        pelotas.forEach(function (pelota) {
        datosEntrada.push(jugador.position.x - pelota.position.x);
        datosEntrada.push(jugador.position.y - pelota.position.y);
        datosEntrada.push(pelota.body.velocity.x);
        datosEntrada.push(pelota.body.velocity.y);
        });
        datosEntrada.push(jugador.position.x);
        datosEntrada.push(jugador.position.y);
        datosEntrada.push(jugador.body.velocity.x);
        datosEntrada.push(jugador.body.velocity.y);

        if (pelotas.length > 0) {
        var output = [
            moveUp.isDown ? 1 : 0,
            moveDown.isDown ? 1 : 0,
            moveLeft.isDown ? 1 : 0,
            moveRight.isDown ? 1 : 0,
        ];

        if (output.some((v) => v !== 0)) {
            datosEntrenamiento.push({
            input: datosEntrada,
            output: output,
            });
        }
        }
    }

    pelotas.forEach(function (pelota) {
        juego.physics.arcade.collide(jugador, pelota, colisionH, null, this);
    });
    }

### `adjustBallAngle`

La función adjustBallAngle ajusta el ángulo de rebote de las pelotas después de una colisión. Esta función es específica para el comportamiento de rebote y asegura que las pelotas cambien su dirección al chocar.


    function adjustBallAngle(pelota) {
        var angle = Phaser.Math.angleBetween(
            0,
            0,
            pelota.body.velocity.x,
            pelota.body.velocity.y
        );
        angle += Phaser.Math.degToRad(velocidadRandom(200, 600));
        var speed = Math.sqrt(
            pelota.body.velocity.x * pelota.body.velocity.x +
            pelota.body.velocity.y * pelota.body.velocity.y
        );
        pelota.body.velocity.x = 400 * Math.cos(angle);
        pelota.body.velocity.y = 400 * Math.sin(angle);
    }

### `reiniciarPelotas`

La función reiniciarPelotas restablece las posiciones y velocidades de las pelotas a valores aleatorios dentro del rango especificado. Esta función asegura que las pelotas se comporten de manera impredecible y reinicien su movimiento cuando sea necesario.

    function reiniciarPelotas() {
        pelotas.forEach(function (pelota) {
            pelota.position.x = Math.random() * w;
            pelota.position.y = Math.random() * h;
            pelota.body.velocity.setTo(
            velocidadRandom(velocidadPelotas, velocidadPelotas + 600),
            velocidadRandom(velocidadPelotas, velocidadPelotas + 600)
            );
        });
        console.log("Posición de las pelotas reiniciada");
    }


## Detección de Eventos con CNN

Este proyecto utiliza una red neuronal convolucional (CNN) para detectar cinco tipos de eventos peligrosos:
- Asalto
- Robo a casa habitación
- Tornados
- Inundaciones
- Incendios

### Cargar las Imágenes de Entrenamiento y Pruebas

Se define una función para cargar las imágenes desde las carpetas especificadas. Las imágenes se etiquetan automáticamente según la estructura de directorios, donde cada subcarpeta representa una clase diferente.

### Preprocesamiento de Imágenes

Se realiza el preprocesamiento de las imágenes cargadas, como el cambio de tamaño y la normalización. Esto es crucial para asegurar que todas las imágenes tengan el mismo tamaño y que los valores de los píxeles estén dentro del rango apropiado para el entrenamiento del modelo.

### Construcción del Modelo

Se define la arquitectura de la red neuronal convolucional utilizando la API de Keras. La red incluye varias capas convolucionales, capas de pooling y capas densamente conectadas (fully connected).

### Compilación del Modelo

Se compila el modelo especificando el optimizador, la función de pérdida y las métricas que se utilizarán para evaluar el rendimiento del modelo durante el entrenamiento.


### Ajuste del Modelo

El modelo se entrena utilizando los datos de entrenamiento y se valida con los datos de prueba. Durante el entrenamiento, se registran las métricas de rendimiento como la precisión y la pérdida para ambas etapas (entrenamiento y validación).

### Evaluación del Modelo

Después del entrenamiento, se evalúa el rendimiento del modelo utilizando el conjunto de datos de prueba. Esto proporciona una medida objetiva de la capacidad del modelo para generalizar a nuevos datos no vistos durante el entrenamiento.

### Función de Clasificación

Se define una función para clasificar nuevas imágenes utilizando el modelo entrenado. La función carga una imagen, la preprocesa de la misma manera que se hizo durante el entrenamiento, y luego predice la clase de evento correspondiente.

### Prueba con Nuevas Imágenes

Se prueba la función de clasificación con un conjunto de imágenes nuevas para verificar el rendimiento del modelo en datos reales. Los resultados de la clasificación se muestran junto con las imágenes correspondientes.


### Visualización de Resultados

Se presentan gráficos que muestran la precisión y la pérdida del modelo durante el entrenamiento y la validación. Estos gráficos ayudan a entender cómo ha evolucionado el modelo durante el proceso de entrenamiento.

### Ejemplos de Clasificación

Se muestran ejemplos de imágenes clasificadas junto con las etiquetas predichas por el modelo. Esto permite una evaluación visual del rendimiento del modelo.



## Reconocimiento de Emociones con LBPH

Este proyecto utiliza Local Binary Patterns Histograms (LBPH) para el reconocimiento de emociones a través de la cámara. Las emociones reconocidas incluyen:
- Felicidad
- Tristeza
- Sorpresa

### Configuración de la Cámara

Se configura la cámara para capturar imágenes en tiempo real. Esto incluye la inicialización del dispositivo de captura de video y la configuración de los parámetros de captura.

### Carga y Preprocesamiento de Datos

#### Carga de Imágenes de Entrenamiento

Se cargan las imágenes etiquetadas de distintas emociones desde el sistema de archivos. Cada imagen está asociada a una etiqueta que representa una emoción específica.

#### Preprocesamiento de Imágenes

Las imágenes cargadas se preprocesan para asegurar un formato consistente. Esto incluye el cambio de tamaño, conversión a escala de grises y normalización.

### Entrenamiento del Modelo LBPH

#### Creación del Modelo

Se crea un modelo de reconocimiento de patrones locales (LBPH) utilizando la biblioteca OpenCV.

#### Entrenamiento del Modelo

El modelo LBPH se entrena utilizando las imágenes preprocesadas y las etiquetas correspondientes. Este proceso implica el análisis de las características de textura de las imágenes para crear un histograma de patrones binarios locales.

### Detección de Emociones en Tiempo Real

#### Captura de Imágenes en Tiempo Real

Se captura un flujo de video en tiempo real desde la cámara. Cada fotograma se procesa para detectar caras y predecir la emoción.

#### Detección de Caras

Se utilizan algoritmos de detección de caras para identificar la posición de las caras en cada fotograma.

#### Predicción de Emociones

El modelo LBPH predice la emoción basada en la región de la imagen que contiene la cara. La emoción predicha se muestra en la pantalla en tiempo real.

### Visualización de Resultados

#### Mostrar Resultados en Tiempo Real

Los resultados de la predicción se superponen en el video en tiempo real, mostrando la emoción detectada junto con un rectángulo alrededor de la cara.

#### Ejemplos de Detección

Se muestran ejemplos de detección de emociones con capturas de pantalla del flujo de video en tiempo real.


## Buscando a Wally con Haar Cascade

Este proyecto es un sistema de detección basado en Haar Cascade para encontrar a Wally en diversas imágenes.

### Creación del Archivo de Negativos

Se crea un archivo `negatives.txt` que contiene las rutas de todas las imágenes negativas (imágenes que no contienen a Wally) en la carpeta especificada. Este archivo es esencial para indicar al algoritmo de entrenamiento cuáles imágenes no deben contener al objeto de interés.

### Creación del Archivo de Positivos

Se crea un archivo `positives.txt` que contiene las rutas de todas las imágenes positivas (imágenes que contienen a Wally) y las coordenadas de los cuadros delimitadores (bounding boxes) en la carpeta especificada. Este archivo es fundamental para proporcionar ejemplos al algoritmo de entrenamiento sobre cómo y dónde aparece Wally en las imágenes.

### Creación de Muestras y Entrenamiento del Clasificador

Se utilizan las herramientas de OpenCV para crear muestras a partir de las imágenes positivas y negativas. Estas muestras se utilizan para entrenar el clasificador Haar Cascade. Durante el entrenamiento, el algoritmo aprende a diferenciar entre las imágenes que contienen a Wally y las que no, utilizando los ejemplos proporcionados en los archivos de positivos y negativos.

### Prueba del Clasificador

El clasificador Haar Cascade entrenado se prueba para detectar a Wally en nuevas imágenes. El clasificador se carga y se aplica a las imágenes, y se dibujan cuadros delimitadores alrededor de las detecciones. Esta fase es crucial para evaluar la precisión y efectividad del modelo entrenado.

### Evaluación en un Conjunto de Datos

El clasificador se evalúa en un conjunto de datos específico. Se procesan todas las imágenes en una carpeta y se detecta la presencia de Wally. Esta fase ayuda a entender cómo se desempeña el clasificador en un entorno más amplio y con datos no vistos durante el entrenamiento.

