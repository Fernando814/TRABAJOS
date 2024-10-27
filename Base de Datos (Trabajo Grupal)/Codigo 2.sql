INSERT INTO "Cliente" (Cod_Cliente, Nombre, Apellido, Telefono) VALUES
('C001', 'Pedro', 'Ramírez', '987654321'),
('C002', 'Elena', 'Sánchez', '912345678'),
('C003', 'Miguel', 'Díaz', '934567890'),
('C004', 'Laura', 'Romero', '998877665'),
('C005', 'Andrés', 'Molina', '987123456'),
('C006', 'Camila', 'Castro', '965432198'),
('C007', 'Daniel', 'Ortega', '949876543'),
('C008', 'Gabriela', 'Silva', '911223344'),
('C009', 'Roberto', 'García', '943211234'),
('C010', 'Isabel', 'Pérez', '952347890');

INSERT INTO "Empleado" (Cod_Empleado, Nombre, Apellido, Ocupacion) VALUES
('E001', 'Juan', 'Pérez', 'Recepcionista'),
('E002', 'María', 'Gómez', 'Gerente'),
('E003', 'Luis', 'Martínez', 'Cocinero'),
('E004', 'Ana', 'López', 'Limpieza'),
('E005', 'Carlos', 'Rodríguez', 'Mantenimiento'),
('E006', 'Sofía', 'Hernández', 'Camarera'),
('E007', 'Javier', 'Fernández', 'Conserje'),
('E008', 'Lucía', 'Torres', 'Recepcionista'),
('E009', 'Diego', 'Ríos', 'Cocinero'),
('E010', 'Valeria', 'Morales', 'Gerente');

INSERT INTO "Habitaciones" (Cod_Habitacion, Estado, Nro_Habitacion, Capacidad_Habitacion, Tipo_de_Habitacion, Costo_Habitacion) VALUES
('H001', 'Disponible', '101', 2, 'Simple', 100.10),
('H002', 'Disponible', '102', 2, 'Doble', 150.20),
('H003', 'Ocupada', '201', 3, 'Triple', 200.50),
('H004', 'Disponible', '202', 4, 'Suite', 300.30),
('H005', 'Ocupada', '301', 2, 'Simple', 120.40),
('H006', 'Disponible', '302', 2, 'Doble', 180.50),
('H007', 'Ocupada', '401', 1, 'Individual', 90.60),
('H008', 'Disponible', '402', 5, 'Familiar', 250.70),
('H009', 'Ocupada', '501', 3, 'Triple', 220.80),
('H010', 'Disponible', '502', 4, 'Suite', 350.90);

INSERT INTO "Pagos" (Cod_Pago, Metodo_Pago, Total_de_Pago, Fecha_de_Pago) VALUES
('P001', 'Tarjeta de Crédito', 200.00, '2024-11-01'),
('P002', 'Efectivo', 150.00, '2024-11-02'),
('P003', 'Transferencia', 300.00, '2024-11-03'),
('P004', 'Tarjeta de Débito', 400.00, '2024-11-04'),
('P005', 'Efectivo', 180.00, '2024-11-05'),
('P006', 'Tarjeta de Crédito', 220.00, '2024-11-06'),
('P007', 'Transferencia', 350.00, '2024-11-07'),
('P008', 'Efectivo', 500.00, '2024-11-08'),
('P009', 'Tarjeta de Débito', 600.00, '2024-11-09'),
('P010', 'Transferencia', 700.00, '2024-11-10');

INSERT INTO "Servicios_Adicionales" (Cod_Servicios, Descripcion, Costo_Adicional) VALUES
('S001', 'Desayuno', 15.00),
('S002', 'Almuerzo', 25.00),
('S003', 'Cena', 30.00),
('S004', 'Transporte', 10.00),
('S005', 'Guía turístico', 60.00),
('S006', 'Spa', 80.00),
('S007', 'Excursión', 70.00),
('S008', 'Servicio de lavandería', 20.00),
('S009', 'Internet', 50.00),
('S010', 'Estacionamiento', 12.00);

INSERT INTO "Reserva" (Cod_Reserva, Cod_Cliente, Cod_Pago, Cod_Habitacion, Cod_Empleado, Fecha_de_Ingreso, Fecha_de_Salida, Cantidad_Dias) VALUES
('R001', 'C001', 'P001', 'H001', 'E001', '2024-10-01', '2024-10-05', 4),
('R002', 'C002', 'P002', 'H002', 'E002', '2024-10-02', '2024-10-04', 2),
('R003', 'C003', 'P003', 'H003', 'E003', '2024-10-03', '2024-10-06', 3),
('R004', 'C004', 'P004', 'H004', 'E004', '2024-10-04', '2024-10-08', 4),
('R005', 'C005', 'P005', 'H005', 'E005', '2024-10-05', '2024-10-07', 2),
('R006', 'C006', 'P006', 'H006', 'E006', '2024-10-06', '2024-10-10', 4),
('R007', 'C007', 'P007', 'H007', 'E007', '2024-10-07', '2024-10-09', 2),
('R008', 'C008', 'P008', 'H008', 'E008', '2024-10-08', '2024-10-12', 4),
('R009', 'C009', 'P009', 'H009', 'E009', '2024-10-09', '2024-10-11', 2),
('R010', 'C010', 'P010', 'H010', 'E010', '2024-10-10', '2024-10-15', 5);

INSERT INTO "Reserva_de_Servicios_Hotel" (Cod_Reserva, Cod_Servicio) VALUES
('R001', 'S001'),
('R001', 'S003'),
('R002', 'S002'),
('R003', 'S004'),
('R004', 'S005'),
('R005', 'S001'),
('R006', 'S006'),
('R007', 'S007'),
('R008', 'S008'),
('R009', 'S009');














