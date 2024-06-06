var w = 800;
var h = 400;
var jugador;
var pelotas = [];
var numPelotas = 1;
var velocidadPelotas = 200;

var moveUp;
var moveDown;
var moveLeft;
var moveRight;

var nnNetwork,
  nnEntrenamiento,
  nnSalida,
  datosEntrenamiento = [];
var modoAuto = false,
  eCompleto = false;

var juego = new Phaser.Game(w, h, Phaser.CANVAS, "", {
  preload: preload,
  create: create,
  update: update,
  render: render,
});

function preload() {
  juego.load.image("fondo", "assets/game/fondo.jpg");
  juego.load.spritesheet("mono", "assets/sprites/altair.png", 32, 48);
  juego.load.image("pelota", "assets/sprites/purple_ball.png");
  juego.load.image("menu", "assets/game/menu.png");
}

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

function enRedNeural() {
  // console.log(
  //   "Datos de Entrenamiento:",
  //   JSON.stringify(datosEntrenamiento, null, 2)
  // );

  nnEntrenamiento.train(datosEntrenamiento, {
    rate: 0.0003,
    iterations: 10000,
    shuffle: true,

    schedule: {
      every: 100,
      do: function (data) {
        console.log(
          "Entrenando - Iteración:",
          data.iterations,
          "Error:",
          data.error
        );
      },
    },
  });
}

function datosDeEntrenamiento(param_entrada) {
  if (param_entrada.some(isNaN)) {
    console.error("Datos de Entrada no válidos:", param_entrada);
    return [0, 0, 0, 0];
  }

  // console.log("Datos de Entrada al Modelo:", param_entrada);
  try {
    nnSalida = nnNetwork.activate(param_entrada);
  } catch (error) {
    console.error("Error en la activación del modelo:", error);
    nnSalida = [0, 0, 0, 0];
  }
  // console.log("Salida del Modelo:", nnSalida);
  return nnSalida;
}

function pausa() {
  juego.paused = true;
  menu = juego.add.sprite(w / 2, h / 2, "menu");
  menu.anchor.setTo(0.5, 0.5);

  var btnEntrenar = juego.add.text(w / 2, h / 2 - 50, "Entrenar", {
    font: "20px Arial",
    fill: "#fff",
  });
  btnEntrenar.inputEnabled = true;
  btnEntrenar.events.onInputUp.add(() => {
    enRedNeural();
    eCompleto = true;
    menu.destroy();
    btnEntrenar.destroy();
    juego.paused = false;
  });

  var btnModoAuto = juego.add.text(w / 2, h / 2 + 50, "Modo Auto", {
    font: "20px Arial",
    fill: "#fff",
  });
  btnModoAuto.inputEnabled = true;
  btnModoAuto.events.onInputUp.add(() => {
    reiniciarPosicion();
    reiniciarPelotas();
    modoAuto = true;
    menu.destroy();
    btnModoAuto.destroy();
    juego.paused = false;
  });
}

function mPausa(event) {
  if (juego.paused) {
    menu.destroy();
    juego.paused = false;
  }
}

function reiniciarPosicion() {
  jugador.position.x = w / 2;
  jugador.position.y = h / 2;
  jugador.body.velocity.x = 0;
  jugador.body.velocity.y = 0;
  console.log("Posición del jugador reiniciada al centro");
}

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
      // console.log("Datos de Entrada al Modelo:", datosEntrada);
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
        // console.log("Datos de Entrenamiento Recogidos:", {
        //   input: datosEntrada,
        //   output: output,
        // });
      }
    }
  }

  pelotas.forEach(function (pelota) {
    juego.physics.arcade.collide(jugador, pelota, colisionH, null, this);
  });
}

function colisionH() {
  pausa();
}

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

function velocidadRandom(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function render() {}
