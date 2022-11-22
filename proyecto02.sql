CREATE TABLE sesion(
    categoria VARCHAR(20),
    duracion VARCHAR(20),
    instructor VARCHAR(20),
    fecha DATE,
    hora TIME,
    id_sesion VARCHAR(20) PRIMARY KEY
);

INSERT INTO sesion(categoria, duracion, instructor, fecha, hora, id_sesion)
VALUES('Resistencia', '2 horas', 'Pedro Ramirez', '2022/01/20', '8:40:00', '30251150')

INSERT INTO sesion(categoria, duracion, instructor, fecha, hora, id_sesion)
VALUES('Resistencia', '3 horas', 'Pedro Ramirez', '2022/02/15', '7:00:00', '11298527')

INSERT INTO sesion(categoria, duracion, instructor, fecha, hora, id_sesion)
VALUES('Fortalecimiento', '1 horas', 'Alejandra Guzman', '2022/03/27', '9:30:00', '40372532')

INSERT INTO sesion(categoria, duracion, instructor, fecha, hora, id_sesion)
VALUES('Fortalecimiento', '2 horas', 'Alejandra Guzman', '2022/04/09', '5:30:00', '27869710')

INSERT INTO sesion(categoria, duracion, instructor, fecha, hora, id_sesion)
VALUES('Fortalecimiento', '3 horas', 'Alejandra Guzman', '2022/05/05', '8:00:00', '18476991')

INSERT INTO sesion(categoria, duracion, instructor, fecha, hora, id_sesion)
VALUES('Equilibrio', '2 horas', 'Rodolfo Gutierrez', '2022/06/11', '10:00:00', '11928176')

INSERT INTO sesion(categoria, duracion, instructor, fecha, hora, id_sesion)
VALUES('Equilibrio', '3 horas', 'Rodolfo Gutierrez', '2022/07/04', '7:30:00', '17565569')

INSERT INTO sesion(categoria, duracion, instructor, fecha, hora, id_sesion)
VALUES('Flexibilidad', '1 hora', 'Fernanda Galindo', '2022/08/12', '9:00:00', '77645853')

INSERT INTO sesion(categoria, duracion, instructor, fecha, hora, id_sesion)
VALUES('Flexibilidad', '2 horas', 'Fernanda Galindo', '2022/09/03', '11:00:00', '93443740')

INSERT INTO sesion(categoria, duracion, instructor, fecha, hora, id_sesion)
VALUES('Flexibilidad', '2 horas', 'Fernanda Galindo', '2022/10/01', '8:00:00', '29961993')

CREATE TABLE registro_peso(
    fecha DATE,
    peso VARCHAR(20),
    id_usuario VARCHAR(20) PRIMARY KEY
);

INSERT INTO registro_peso(fecha, peso, id_usuario)
VALUES('2022/02/02', '180', '30317512')

INSERT INTO registro_peso(fecha, peso, id_usuario)
VALUES('2022/01/15', '200', '87954218')

INSERT INTO registro_peso(fecha, peso, id_usuario)
VALUES('2022/03/01', '140', '93779985')

INSERT INTO registro_peso(fecha, peso, id_usuario)
VALUES('2022/04/20', '175', '11779375')

INSERT INTO registro_peso(fecha, peso, id_usuario)
VALUES('2022/06/17', '130', '92656444')

INSERT INTO registro_peso(fecha, peso, id_usuario)
VALUES('2022/08/08', '160', '46033728')

INSERT INTO registro_peso(fecha, peso, id_usuario)
VALUES('2022/07/23', '220', '57453209')

INSERT INTO registro_peso(fecha, peso, id_usuario)
VALUES('2022/05/31', '195', '63178824')

INSERT INTO registro_peso(fecha, peso, id_usuario)
VALUES('2022/09/11', '210', '60423746')

INSERT INTO registro_peso(fecha, peso, id_usuario)
VALUES('2022/10/01', '190', '16203325')


CREATE TABLE entrenador(
    id_entrenador VARCHAR(20) PRIMARY KEY,
    contrato_horas VARCHAR(20),
    metodo_pago VARCHAR(20),
    nombre VARCHAR(20)
);

INSERT INTO entrenador(id_entrenador, contrato_horas, metodo_pago, nombre)
VALUES('30134901', '30', 'Efectivo', 'Ramiro Carvajal')

INSERT INTO entrenador(id_entrenador, contrato_horas, metodo_pago, nombre)
VALUES('31787945', '30', 'Efectivo', 'Rodolfo Gutierrez')

INSERT INTO entrenador(id_entrenador, contrato_horas, metodo_pago, nombre)
VALUES('19335081', '30', 'Tranferencia', 'Martin Rivera')

INSERT INTO entrenador(id_entrenador, contrato_horas, metodo_pago, nombre)
VALUES('68731572', '30', 'Cheque', 'Mario Lopez')

INSERT INTO entrenador(id_entrenador, contrato_horas, metodo_pago, nombre)
VALUES('04201999', '30', 'Transferencia', 'Andres Galindo')

INSERT INTO entrenador(id_entrenador, contrato_horas, metodo_pago, nombre)
VALUES('19851520', '30', 'Cheque', 'Fernanda Miguel')

INSERT INTO entrenador(id_entrenador, contrato_horas, metodo_pago, nombre)
VALUES('34210785', '30', 'Efectivo', 'Javier Quintero')

INSERT INTO entrenador(id_entrenador, contrato_horas, metodo_pago, nombre)
VALUES('84175519', '30', 'Transferencia', 'Carlos Murillo')

INSERT INTO entrenador(id_entrenador, contrato_horas, metodo_pago, nombre)
VALUES('30261997', '30', 'Cheque', 'Amalia Cabrera')

INSERT INTO entrenador(id_entrenador, contrato_horas, metodo_pago, nombre)
VALUES('92732177', '30', 'Efectivo', 'Daniela Ortiz')

CREATE TABLE iwatch_sesiones(
    id_usuario VARCHAR(20),
    id_sesion VARCHAR(20),
    fecha DATE,
    hora TIME,
    ritmo_cardiaco VARCHAR(20),
    calorias VARCHAR(20),
    tipo_ejercicio VARCHAR(20),
    PRIMARY KEY(id_usuario, id_sesion),
    FOREIGN KEY (id_usuario) REFERENCES registro_peso(id_usuario),
    FOREIGN KEY (id_sesion) REFERENCES sesion(id_sesion)
);

INSERT INTO iwatch_sesiones(id_usuario, id_sesion, fecha, hora, ritmo_cardiaco, calorias, tipo_ejercicio)
VALUES('30317512', '30251150', '2022/03/15', '7:30:00', '60 latidos p/minuto', '40', 'Abdominales');

INSERT INTO iwatch_sesiones(id_usuario, id_sesion, fecha, hora, ritmo_cardiaco, calorias, tipo_ejercicio)
VALUES('87954218', '11298527', '2022/05/07', '8:30:00', '75 latidos p/minuto', '30', 'Flexiones');

INSERT INTO iwatch_sesiones(id_usuario, id_sesion, fecha, hora, ritmo_cardiaco, calorias, tipo_ejercicio)
VALUES('93779985', '40372532', '2022/02/25', '9:00:00', '90 latidos p/minuto', '45', 'Abdominales');

INSERT INTO iwatch_sesiones(id_usuario, id_sesion, fecha, hora, ritmo_cardiaco, calorias, tipo_ejercicio)
VALUES('11779375', '27869710', '2022/07/01', '10:30:00', '100 latidos p/minuto', '50', 'Bicicleta');

INSERT INTO iwatch_sesiones(id_usuario, id_sesion, fecha, hora, ritmo_cardiaco, calorias, tipo_ejercicio)
VALUES('92656444', '18476991', '2022/04/23', '11:00:00', '85 latidos p/minuto', '60', 'Pesas');

INSERT INTO iwatch_sesiones(id_usuario, id_sesion, fecha, hora, ritmo_cardiaco, calorias, tipo_ejercicio)
VALUES('46033728', '11928176', '2022/09/05', '12:30:00', '110 latidos p/minuto', '35', 'Plancha');

INSERT INTO iwatch_sesiones(id_usuario, id_sesion, fecha, hora, ritmo_cardiaco, calorias, tipo_ejercicio)
VALUES('57453209', '17565569', '2022/08/12', '10:00:00', '110 latidos p/minuto', '40', 'Plancha');

INSERT INTO iwatch_sesiones(id_usuario, id_sesion, fecha, hora, ritmo_cardiaco, calorias, tipo_ejercicio)
VALUES('63178824', '77645853', '2022/10/10', '12:00:00', '95 latidos p/minuto', '30', 'Sentadillas');

INSERT INTO iwatch_sesiones(id_usuario, id_sesion, fecha, hora, ritmo_cardiaco, calorias, tipo_ejercicio)
VALUES('60423746', '93443740', '2022/04/17', '9:45:00', '90 latidos p/minuto', '55', 'Pesas');

INSERT INTO iwatch_sesiones(id_usuario, id_sesion, fecha, hora, ritmo_cardiaco, calorias, tipo_ejercicio)
VALUES('16203325', '29961993', '2022/09/30', '8:45:00', '100 latidos p/minuto', '65', 'Bicicleta');

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
    plan VARCHAR(20),
    PRIMARY KEY(id_usuario),
    FOREIGN KEY (id_usuario) REFERENCES registro_peso(id_usuario)
);

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Elvira Sanchez', '31', 'Zona 14', '30317512', '1.75 mts', '160 lbs', '30', 'No', 'Si', 'Activa', 'Efectivo', 'Premium' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Alejandro Cespedes', '35', 'Zona 1', '87954218', '1.90 mts', '140 lbs', '40', 'No', 'Si', 'Activa', 'Efectivo', 'Premium' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Pedro Martinez', '29', 'Zona 11', '93779985', '1.60 mts', '155 lbs', '35', 'Si', 'Si', 'Activa', 'Transferencia', 'Básico' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Amelia Guzman', '33', 'Zona 15', '11779375', '1.50 mts', '130 lbs', '25', 'No', 'No', 'Activa', 'Efectivo', 'Básico' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Juan Perez', '30', 'Zona 5', '92656444', '1.65 mts', '170 lbs', '30', 'No', 'Si', 'Activa', 'Transferencia', 'Premium' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Soraya Mogollon', '37', 'Zona 13', '46033728', '1.60 mts', '145 lbs', '35', 'No', 'No', 'Activa', 'Efectivo', 'Premium' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Pepe Soler', '32', 'Zona 14', '57453209', '1.80 mts', '135 lbs', '20', 'Si', 'Si', 'Activa', 'Efectivo', 'Básico' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Mateo Albin', '34', 'Zona 9', '63178824', '1.55 mts', '130 lbs', '30', 'No', 'No', 'Activa', 'Transferencia', 'Básico' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Natalia Madrid', '33', 'Zona 16', '60423746', '1.70 mts', '145 lbs', '30', 'No', 'Si', 'Activa', 'Efectivo', 'Premium' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Valeria Carrillo', '28', 'Zona 10', '16203325', '1.73 mts', '135 lbs', '25', 'Si', 'Si', 'Activa', 'Transferencia', 'Premium' );
*

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Antonio Sanchez', '31', 'Zona 14', '30317512', '1.75 mts', '160 lbs', '30', 'No', 'Si', 'Activa', 'Efectivo', 'Premium' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Francisco Vega', '35', 'Zona 1', '87954218', '1.90 mts', '140 lbs', '40', 'No', 'Si', 'Activa', 'Efectivo', 'Premium' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Emiliano Cabral', '29', 'Zona 11', '93779985', '1.60 mts', '155 lbs', '35', 'Si', 'Si', 'Activa', 'Transferencia', 'Básico' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Barbara Luzardo', '33', 'Zona 15', '11779375', '1.50 mts', '130 lbs', '25', 'No', 'No', 'Activa', 'Efectivo', 'Básico' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Edith Morales', '30', 'Zona 5', '92656444', '1.65 mts', '170 lbs', '30', 'No', 'Si', 'Activa', 'Transferencia', 'Premium' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Pedro Galante', '37', 'Zona 13', '46033728', '1.60 mts', '145 lbs', '35', 'No', 'No', 'Activa', 'Efectivo', 'Premium' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Alejandro Micheo', '32', 'Zona 14', '57453209', '1.80 mts', '135 lbs', '20', 'Si', 'Si', 'Activa', 'Efectivo', 'Básico' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Javier Moller', '34', 'Zona 9', '63178824', '1.55 mts', '130 lbs', '30', 'No', 'No', 'Activa', 'Transferencia', 'Básico' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Isabel Adames', '33', 'Zona 16', '60423746', '1.70 mts', '145 lbs', '30', 'No', 'Si', 'Activa', 'Efectivo', 'Premium' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Ares Torres', '28', 'Zona 10', '16203325', '1.73 mts', '135 lbs', '25', 'Si', 'Si', 'Activa', 'Transferencia', 'Premium' );
*

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Eric Assa', '31', 'Zona 14', '30317512', '1.75 mts', '160 lbs', '30', 'No', 'Si', 'Activa', 'Efectivo', 'Premium' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Marck Theilheimer', '35', 'Zona 1', '87954218', '1.90 mts', '140 lbs', '40', 'No', 'Si', 'Activa', 'Efectivo', 'Premium' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Tommy Dicker', '29', 'Zona 11', '93779985', '1.60 mts', '155 lbs', '35', 'Si', 'Si', 'Activa', 'Transferencia', 'Básico' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Valeria de Urioste', '33', 'Zona 15', '11779375', '1.50 mts', '130 lbs', '25', 'No', 'No', 'Activa', 'Efectivo', 'Básico' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Jimena Vico', '30', 'Zona 5', '92656444', '1.65 mts', '170 lbs', '30', 'No', 'Si', 'Activa', 'Transferencia', 'Premium' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Valeria Paiz', '37', 'Zona 13', '46033728', '1.60 mts', '145 lbs', '35', 'No', 'No', 'Activa', 'Efectivo', 'Premium' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Maria Naranjo', '32', 'Zona 14', '57453209', '1.80 mts', '135 lbs', '20', 'Si', 'Si', 'Activa', 'Efectivo', 'Básico' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Lucrecia Montesinos', '34', 'Zona 9', '63178824', '1.55 mts', '130 lbs', '30', 'No', 'No', 'Activa', 'Transferencia', 'Básico' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Christian Carden', '33', 'Zona 16', '60423746', '1.70 mts', '145 lbs', '30', 'No', 'Si', 'Activa', 'Efectivo', 'Premium' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Samuel Garcia', '28', 'Zona 10', '16203325', '1.73 mts', '135 lbs', '25', 'Si', 'Si', 'Activa', 'Transferencia', 'Premium' );
*

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Javier Farnes', '31', 'Zona 14', '30317512', '1.75 mts', '160 lbs', '30', 'No', 'Si', 'Activa', 'Efectivo', 'Premium' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Alejandro Castañeda', '35', 'Zona 1', '87954218', '1.90 mts', '140 lbs', '40', 'No', 'Si', 'Activa', 'Efectivo', 'Premium' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Nicolas Bandi', '29', 'Zona 11', '93779985', '1.60 mts', '155 lbs', '35', 'Si', 'Si', 'Activa', 'Transferencia', 'Básico' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Diego Bandi', '33', 'Zona 15', '11779375', '1.50 mts', '130 lbs', '25', 'No', 'No', 'Activa', 'Efectivo', 'Básico' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Andres Mendez', '30', 'Zona 5', '92656444', '1.65 mts', '170 lbs', '30', 'No', 'Si', 'Activa', 'Transferencia', 'Premium' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Monica Valencia', '37', 'Zona 13', '46033728', '1.60 mts', '145 lbs', '35', 'No', 'No', 'Activa', 'Efectivo', 'Premium' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Leonidas Galindo', '32', 'Zona 14', '57453209', '1.80 mts', '135 lbs', '20', 'Si', 'Si', 'Activa', 'Efectivo', 'Básico' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Antonia Mancero', '34', 'Zona 9', '63178824', '1.55 mts', '130 lbs', '30', 'No', 'No', 'Activa', 'Transferencia', 'Básico' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Fidel Pelaez', '33', 'Zona 16', '60423746', '1.70 mts', '145 lbs', '30', 'No', 'Si', 'Activa', 'Efectivo', 'Premium' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Carlos Ortiz', '28', 'Zona 10', '16203325', '1.73 mts', '135 lbs', '25', 'Si', 'Si', 'Activa', 'Transferencia', 'Premium' );
*

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Jorge Rivero', '31', 'Zona 14', '30317512', '1.75 mts', '160 lbs', '30', 'No', 'Si', 'Activa', 'Efectivo', 'Premium' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Rodrigo Velasquez', '35', 'Zona 1', '87954218', '1.90 mts', '140 lbs', '40', 'No', 'Si', 'Activa', 'Efectivo', 'Premium' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Luis Carlos Rosenberg', '29', 'Zona 11', '93779985', '1.60 mts', '155 lbs', '35', 'Si', 'Si', 'Activa', 'Transferencia', 'Básico' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Nicolas Miño', '33', 'Zona 15', '11779375', '1.50 mts', '130 lbs', '25', 'No', 'No', 'Activa', 'Efectivo', 'Básico' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Rafael Contreras', '30', 'Zona 5', '92656444', '1.65 mts', '170 lbs', '30', 'No', 'Si', 'Activa', 'Transferencia', 'Premium' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Enrique Murillo', '37', 'Zona 13', '46033728', '1.60 mts', '145 lbs', '35', 'No', 'No', 'Activa', 'Efectivo', 'Premium' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Claudia Arevalo', '32', 'Zona 14', '57453209', '1.80 mts', '135 lbs', '20', 'Si', 'Si', 'Activa', 'Efectivo', 'Básico' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Juana Estrada', '34', 'Zona 9', '63178824', '1.55 mts', '130 lbs', '30', 'No', 'No', 'Activa', 'Transferencia', 'Básico' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Ambrocio Orellana', '33', 'Zona 16', '60423746', '1.70 mts', '145 lbs', '30', 'No', 'Si', 'Activa', 'Efectivo', 'Premium' );

INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
VALUES('Jaime Robles', '28', 'Zona 10', '16203325', '1.73 mts', '135 lbs', '25', 'Si', 'Si', 'Activa', 'Transferencia', 'Premium' );
