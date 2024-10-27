CREATE TABLE "Cliente" (
    'Cod_Cliente'       VARCHAR(8),
    'Nombre'            VARCHAR(50),
    'Apellido'          VARCHAR(40),
    'Telefono'          VARCHAR(9),
    PRIMARY KEY (Cod_Cliente)
);

CREATE TABLE "Empleado" (
    'Cod_Empleado'      VARCHAR(8),
    'Nombre'            VARCHAR(50),
    'Apellido'          VARCHAR(40),
    'Ocupacion'         VARCHAR(20),
    PRIMARY KEY (Cod_Empleado)
);

CREATE TABLE "Habitaciones" (
    'Cod_Habitacion'    VARCHAR(8),
    'Estado'            VARCHAR(20),
    'Nro_Habitacion'    VARCHAR(8),
    'Capacidad_Habitacion' INT,
    'Tipo_de_Habitacion' VARCHAR(30),
    'Costo_Habitacion'  DECIMAL,
    PRIMARY KEY (Cod_Habitacion)
);

CREATE TABLE "Pagos" (
    'Cod_Pago'          VARCHAR(8),
    'Metodo_Pago'      VARCHAR(20),
    'Total_de_Pago'     DECIMAL,
    'Fecha_de_Pago'     DATE,
    PRIMARY KEY (Cod_Pago)
);

CREATE TABLE "Servicios_Adicionales" (
    'Cod_Servicios'     VARCHAR(8),
    'Descripcion'       VARCHAR(50),
    'Costo_Adicional'   DECIMAL,
    PRIMARY KEY (Cod_Servicios)
);

CREATE TABLE "Reserva" (
    'Cod_Reserva'       VARCHAR(8),
    'Cod_Cliente'       VARCHAR(8),
    'Cod_Pago'          VARCHAR(8),
    'Cod_Habitacion'    VARCHAR(8),
    'Cod_Empleado'      VARCHAR(8),
    'Fecha_de_Ingreso'  DATE,
    'Fecha_de_Salida'   DATE,
    'Cantidad_Dias'     INT,
    PRIMARY KEY (Cod_Reserva),
    FOREIGN KEY (Cod_Cliente) REFERENCES "Cliente" (Cod_Cliente),
    FOREIGN KEY (Cod_Pago) REFERENCES "Pagos" (Cod_Pago),
    FOREIGN KEY (Cod_Habitacion) REFERENCES "Habitaciones" (Cod_Habitacion),
    FOREIGN KEY (Cod_Empleado) REFERENCES "Empleado" (Cod_Empleado)
);

CREATE TABLE "Reserva_de_Servicios_Hotel" (
    'Cod_Reserva'       VARCHAR(8),
    'Cod_Servicio'      VARCHAR(8),
    PRIMARY KEY (Cod_Reserva, Cod_Servicio),
    FOREIGN KEY (Cod_Reserva) REFERENCES "Reserva" (Cod_Reserva),
    FOREIGN KEY (Cod_Servicio) REFERENCES "Servicios_Adicionales" (Cod_Servicios)
);















