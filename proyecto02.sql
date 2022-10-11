CREATE TABLE sesion(
    categoria VARCHAR(20),
    duracion VARCHAR(20),
    instructor VARCHAR(20),
    fecha DATE,
    hora TIME,
    id_sesion VARCHAR(20)
)

CREATE TABLE registro_peso(
    fecha DATE,
    peso VARCHAR(20),
    id_usuario VARCHAR(20)
)

CREATE TABLE entrenador(
    id_entrenador VARCHAR(20),
    contrato_horas VARCHAR(20),
    metodo_pago VARCHAR(20),
    
)

CREATE TABLE iwatch_sesiones(
    fecha DATE,
    hora TIME,
    ritmo_cardiaco VARCHAR(20),
    calorias VARCHAR(20),
    tipo_ejercicio VARCHAR(20)
)

CREATE TABLE usuario(
    nombre VARCHAR(20),
    edad VARCHAR(20),
    direccion VARCHAR(20),
    id_usuario VARCHAR(20),
    altura VARCHAR(20),
    peso_actual VARCHAR(20),
    calorias_diarias VARCHAR(20),
    administrador VARCHAR(20),
    suscripcion_activa VARCHAR(20),
    estado_cuenta VARCHAR(20),
    pago VARCHAR(20),
    plan VARCHAR(20)
)