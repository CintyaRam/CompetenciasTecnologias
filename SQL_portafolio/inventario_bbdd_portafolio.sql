-- ========================================================
-- SISTEMA DE INVENTARIO - STAR WARS EDITION
-- Proyecto de Portafolio - Gestión de Bases de Datos
-- Cumple con todos los requerimientos de evaluación
-- ========================================================

-- ========================================================
-- LENGUAJE DE DEFINICIÓN DE DATOS (DDL)
-- Creación de esquema, tablas, claves, índices y restricciones
-- Cumple con 3NF y buenas prácticas de modelado relacional
-- ========================================================


-- Creación del esquema (base de datos)
CREATE SCHEMA IF NOT EXISTS `sistema_inventario_portafolio` DEFAULT CHARACTER SET utf8;
USE `sistema_inventario_portafolio`;

-- Tabla: proveedores
-- Propósito: Almacena información de proveedores galácticos
-- Clave primaria: id
-- Relación: 1 a muchos con productos
CREATE TABLE IF NOT EXISTS `sistema_inventario_portafolio`.`proveedores` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `direccion` VARCHAR(100) NOT NULL,
  `telefono` VARCHAR(15) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE
) ENGINE = InnoDB;

-- Tabla: productos
-- Propósito: Almacena productos con su precio, stock y proveedor
-- Clave primaria: id
-- Clave foránea: proveedor_id → proveedores.id
CREATE TABLE IF NOT EXISTS `sistema_inventario_portafolio`.`productos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` TEXT NOT NULL,
  `precio` INT NOT NULL CHECK (precio >= 0),
  `cantidad_inventario` INT NOT NULL CHECK (cantidad_inventario >= 0),
  `proveedor_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_productos_proveedores1_idx` (`proveedor_id` ASC) VISIBLE,
  CONSTRAINT `fk_productos_proveedores1`
    FOREIGN KEY (`proveedor_id`)
    REFERENCES `sistema_inventario_portafolio`.`proveedores` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- Tabla: tipo
-- Propósito: Catálogo de tipos de transacción (Compra, Venta)
-- Clave primaria: id
-- Cumple con 3NF
CREATE TABLE IF NOT EXISTS `sistema_inventario_portafolio`.`tipo` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tipo_transaccion` VARCHAR(45) NOT NULL UNIQUE,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;

-- Tabla: transacciones
-- Propósito: Registro histórico de compras y ventas
-- Clave primaria: id
-- Claves foráneas: tipo_id, proveedor_id, producto_id
-- Guarda precio_unitario para mantener historial (cumple 3NF)
CREATE TABLE IF NOT EXISTS `sistema_inventario_portafolio`.`transacciones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `fecha` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `tipo_id` INT NOT NULL,
  `proveedor_id` INT DEFAULT NULL,
  `producto_id` INT NOT NULL,
  `cantidad` INT NOT NULL CHECK (cantidad > 0),
  `precio_unitario` INT NOT NULL CHECK (precio_unitario >= 0),
  PRIMARY KEY (`id`),
  INDEX `fk_transacciones_tipo_idx` (`tipo_id` ASC) VISIBLE,
  INDEX `fk_transacciones_proveedores1_idx` (`proveedor_id` ASC) VISIBLE,
  INDEX `fk_transacciones_productos1_idx` (`producto_id` ASC) VISIBLE,
  CONSTRAINT `fk_transacciones_tipo`
    FOREIGN KEY (`tipo_id`)
    REFERENCES `sistema_inventario_portafolio`.`tipo` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_transacciones_proveedores1`
    FOREIGN KEY (`proveedor_id`)
    REFERENCES `sistema_inventario_portafolio`.`proveedores` (`id`)
    ON DELETE SET NULL
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_transacciones_productos1`
    FOREIGN KEY (`producto_id`)
    REFERENCES `sistema_inventario_portafolio`.`productos` (`id`)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION
) ENGINE = InnoDB;


-- Ejemplo de ALTER TABLE (no ejecutar en este script, solo para demostración)
-- ALTER TABLE productos ADD COLUMN sku VARCHAR(20) NULL AFTER nombre;


-- ========================================================
-- LENGUAJE DE MANIPULACIÓN DE DATOS (DML) - INSERT
-- Inserción de datos de prueba (Star Wars Edition)
-- ========================================================

-- Insertar tipos de transacción
INSERT INTO tipo (tipo_transaccion) VALUES
('Compra'),
('Venta');

-- Insertar proveedores galácticos
INSERT INTO proveedores (nombre, direccion, telefono, email) VALUES
('Sienar Fleet Systems', 'Coruscant Sector 7', '+1800STARDEST', 'ventas@sienarfleet.com'),
('Watto’s Junk Shop', 'Mos Espa, Tatooine', '+555JUNKBOT', 'watto@tatooine.blackmarket'),
('Kuat Drive Yards', 'Kuat Orbital', '+1800KDYSTAR', 'orders@kuatdriveyards.com'),
('Baktoid Armor Workshop', 'Geonosis Foundry', '+555BEDROID', 'sales@baktoid.com'),
('Czerka Corporation', 'Corellia HQ', '+1800CZERKA', 'weapons@czerka.corp');

-- Insertar productos
INSERT INTO productos (nombre, descripcion, precio, cantidad_inventario, proveedor_id) VALUES
('Blaster DL-44', 'Pistola de Han Solo. Alta precisión, daño letal.', 150000, 25, 2),
('Lightsaber Azul', 'Sable de luz Jedi. Cristal kyber incluido.', 500000, 5, 1),
('TIE Fighter', 'Caza estelar del Imperio. Rápido y letal.', 2000000, 3, 1),
('Droid R2-D2 (réplica funcional)', 'Asistente astromecánico. ¡Chispas garantizadas!', 800000, 2, 4),
('Armor Mandaloriana', 'Blindaje beskar. Resistente a sables de luz.', 1200000, 1, 5),
('Speeder Bike 74-Z', 'Moto de combate imperial. Velocidad máxima 500km/h.', 350000, 8, 3),
('Thermal Detonator', 'Granada de alto poder. ¡Cuidado al manipular!', 75000, 50, 5),
('Protocol Droid C-3PO (réplica)', 'Traductor galáctico. 6 millones de formas de comunicación.', 450000, 3, 4);
