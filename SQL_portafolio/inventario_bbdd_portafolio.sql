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


-- ========================================================
-- LENGUAJE DE MANIPULACIÓN DE DATOS (DML) - UPDATE + PROCEDIMIENTO
-- Procedimiento almacenado para registrar transacciones
-- Maneja transacciones atómicas, validación y actualización de stock
-- ========================================================

DELIMITER //

CREATE PROCEDURE RegistrarTransaccion(
    IN p_tipo_transaccion VARCHAR(15),     
    IN p_proveedor_id INT,
    IN p_producto_id INT,
    IN p_cantidad INT
)
BEGIN
    DECLARE v_tipo_id INT;
    DECLARE v_precio_actual INT;
    DECLARE v_stock_actual INT;
    DECLARE v_operacion VARCHAR(10);

    -- Iniciar transacción manual
    SET autocommit = 0;
    START TRANSACTION;

    -- Validar tipo de transacción
    SELECT id INTO v_tipo_id
    FROM tipo
    WHERE tipo_transaccion = p_tipo_transaccion;

    IF v_tipo_id IS NULL THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Tipo de transacción no válido. Use "Compra" o "Venta".';
    END IF;

    -- Obtener precio y stock actual del producto
    SELECT precio, cantidad_inventario
    INTO v_precio_actual, v_stock_actual
    FROM productos
    WHERE id = p_producto_id
    FOR UPDATE; 

    IF v_precio_actual IS NULL THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Producto no encontrado.';
    END IF;

    -- Validar proveedor según tipo
    IF p_tipo_transaccion = 'Compra' AND p_proveedor_id IS NULL THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Debe especificar proveedor_id para una compra.';
    END IF;

    IF p_tipo_transaccion = 'Venta' AND p_proveedor_id IS NOT NULL THEN
        SET p_proveedor_id = NULL; -- Forzar NULL en ventas
    END IF;

    -- Validar stock y determinar operación
    IF p_tipo_transaccion = 'Venta' THEN
        SET v_operacion = 'salida';
        IF p_cantidad > v_stock_actual THEN
            ROLLBACK;
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Stock insuficiente para realizar la venta.';
        END IF;
    ELSEIF p_tipo_transaccion = 'Compra' THEN
        SET v_operacion = 'entrada';
    ELSE
        ROLLBACK;
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Tipo de transacción no soportado.';
    END IF;

    -- Registrar transacción (precio histórico)
    INSERT INTO transacciones (
        tipo_id,
        proveedor_id,
        producto_id,
        cantidad,
        precio_unitario
    ) VALUES (
        v_tipo_id,
        p_proveedor_id,
        p_producto_id,
        p_cantidad,
        v_precio_actual
    );

    -- Actualizar inventario
    IF v_operacion = 'salida' THEN
        UPDATE productos
        SET cantidad_inventario = cantidad_inventario - p_cantidad
        WHERE id = p_producto_id;
    ELSE
        UPDATE productos
        SET cantidad_inventario = cantidad_inventario + p_cantidad
        WHERE id = p_producto_id;
    END IF;

    -- Confirmar transacción
    COMMIT;
    SET autocommit = 1;

    SELECT 'Transacción registrada exitosamente.' AS mensaje;

END //

DELIMITER ;

-- ========================================================
-- CONSULTAS DE SELECCIÓN (SELECT, JOIN, GROUP BY, SUBQUERIES)
-- Demuestra dominio de SQL para obtención de información
-- ========================================================

-- Consulta 1: Productos disponibles en inventario
SELECT * FROM productos WHERE cantidad_inventario > 0;

-- Consulta 2: Proveedores de un producto específico
SELECT productos.nombre AS producto, p.nombre AS proveedor, cantidad_inventario 
FROM productos
JOIN proveedores p ON p.id = proveedor_id
WHERE productos.id = 2;

-- Consulta 3: Transacciones en una fecha específica
SELECT * FROM transacciones WHERE DATE(fecha) = "2025-09-08";

-- Consulta 4: Total de compras (conteo y valor)
SELECT COUNT(*) AS cantidad_compras, SUM(cantidad) AS productos_comprados 
FROM transacciones
WHERE tipo_id = 1;

SELECT SUM(cantidad) AS cantidad_vendida 
FROM transacciones
WHERE tipo_id = 2;

SELECT SUM(cantidad * precio_unitario) AS total_compras
FROM transacciones t
WHERE tipo_id = 1;

-- Consulta 5: Ventas de un producto en septiembre 2025
SELECT p.nombre AS producto, SUM(t.cantidad) AS unidades_vendidas, SUM(t.cantidad * t.precio_unitario) AS total_ventas
FROM transacciones t
JOIN productos p ON t.producto_id = p.id
WHERE t.tipo_id = 2 
  AND t.producto_id = 7
  AND t.fecha >= '2025-09-01'
  AND t.fecha < '2025-10-01'
GROUP BY p.id, p.nombre;

-- Consulta 6: JOINs para información completa de transacciones
SELECT 
    t.id AS transaccion_id,
    tp.tipo_transaccion,
    t.fecha,
    p.id AS producto_id,
    p.nombre AS producto_nombre,
    p.descripcion AS producto_descripcion,
    p.precio AS precio_actual_producto,
    t.cantidad,
    t.precio_unitario AS precio_en_transaccion,
    (t.cantidad * t.precio_unitario) AS total_linea,
    pr.id AS proveedor_id,
    pr.nombre AS proveedor_nombre,
    pr.telefono AS proveedor_telefono,
    pr.email AS proveedor_email
FROM transacciones t
INNER JOIN tipo tp ON t.tipo_id = tp.id
INNER JOIN productos p ON t.producto_id = p.id
LEFT JOIN proveedores pr ON t.proveedor_id = pr.id
ORDER BY t.fecha DESC, t.id DESC;

-- Consulta 7: Subconsulta - Productos no vendidos en septiembre 2025
SELECT 
    p.id,
    p.nombre,
    p.descripcion,
    p.precio,
    p.cantidad_inventario,
    pr.nombre AS proveedor
FROM productos p
JOIN proveedores pr ON p.proveedor_id = pr.id
WHERE p.id NOT IN (
    SELECT DISTINCT t.producto_id
    FROM transacciones t
    JOIN tipo tp ON t.tipo_id = tp.id
    WHERE tp.tipo_transaccion = 'Venta'
      AND t.fecha >= '2025-09-01'
      AND t.fecha < '2025-10-01'
);

-- ========================================================
-- LENGUAJE DE MANIPULACIÓN DE DATOS (DML) - DELETE
-- Ejemplo de eliminación (comentado por seguridad)
-- Se respeta ON DELETE RESTRICT para integridad
-- ========================================================

-- EJEMPLO EDUCATIVO DELETE
-- Eliminar un proveedor SOLO si no tiene productos ni transacciones
-- Se asigna id no existente para evitar inconvenientes
-- DELETE FROM proveedores WHERE id = 999;

-- Eliminar un producto SOLO si no tiene transacciones (gracias a ON DELETE RESTRICT)
-- Se asigna id no existente para evitar accidentes
-- DELETE FROM productos WHERE id = 999;


-- ========================================================
-- Verificación final - Ejecutar transacciones de prueba
-- ========================================================

CALL RegistrarTransaccion('Venta', NULL, 5, 1);
CALL RegistrarTransaccion('Venta', NULL, 2, 1);
CALL RegistrarTransaccion('Venta', NULL, 7, 3);

SELECT * FROM productos; -- Verificar actualización de stock

CALL RegistrarTransaccion('Compra', 3, 6, 2);

SELECT * FROM transacciones; -- Verificar registro histórico