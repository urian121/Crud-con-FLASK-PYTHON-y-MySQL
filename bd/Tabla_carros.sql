-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-12-2022 a las 17:18:00
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `node_mysql`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carros`
--

CREATE TABLE `carros` (
  `id` int(11) NOT NULL,
  `marca` varchar(45) NOT NULL,
  `modelo` varchar(45) NOT NULL,
  `year` varchar(45) NOT NULL,
  `color` varchar(45) NOT NULL,
  `puertas` varchar(45) NOT NULL,
  `favorito` varchar(45) NOT NULL,
  `foto` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `carros`
--

INSERT INTO `carros` (`id`, `marca`, `modelo`, `year`, `color`, `puertas`, `favorito`, `foto`) VALUES
(1, 'BMW', 'BMW X7', '2022', 'Gris', '4', 'Si', 'bmw_2022.jpg'),
(2, 'Ford', 'CAMIONETA', '2022', 'Blanco', '4', 'Si', 'ford_camioneta_2020.webp'),
(3, 'Chevrolet', 'Onix Turbo', '2013', 'Blanco', '2', 'No', 'chevrolet.webp'),
(7, 'Toyota', 'Avalon', '2018', 'Gris', '2', 'No', 'toyota_corolla.webp'),
(8, 'Chevrolet', 'Joy HB', '2015', 'Rojo', '4', 'Si', ''),
(10, 'Mercedes-Benz', 'CLA Coupé', '2022', 'Blanco', '4', 'Si', 'CLA_Coupe.jpg');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `carros`
--
ALTER TABLE `carros`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `carros`
--
ALTER TABLE `carros`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
