CREATE TABLE personas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    documento VARCHAR(20) UNIQUE NOT NULL,
    sexo CHAR(1) CHECK (sexo IN ('M', 'F')) NOT NULL
);

INSERT INTO public.personas (nombre, apellido, documento, sexo) VALUES
('Juan', 'Pérez', '12345678', 'M'),
('María', 'Gómez', '87654321', 'F'),
('Carlos', 'Rodríguez', '23456789', 'M'),
('Laura', 'Fernández', '98765432', 'F'),
('Jorge', 'Martínez', '34567890', 'M'),
('Ana', 'Sánchez', '87651234', 'F'),
('Pedro', 'López', '45678901', 'M'),
('Lucía', 'Ramírez', '10987654', 'F'),
('Raúl', 'García', '56789012', 'M'),
('Elena', 'Díaz', '21098765', 'F');