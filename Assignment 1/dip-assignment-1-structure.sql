-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 21, 2021 at 09:38 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dip-assignment-1`
--

-- --------------------------------------------------------

--
-- Table structure for table `aankoop`
--

CREATE TABLE `aankoop` (
  `klant_idklant` int(11) NOT NULL,
  `filiaal_idfiliaal` int(11) NOT NULL,
  `product_idproduct` int(11) NOT NULL,
  `datum` datetime NOT NULL,
  `aantal` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `eenheid`
--

CREATE TABLE `eenheid` (
  `ideenheid` int(11) NOT NULL,
  `omschrijving` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `filiaal`
--

CREATE TABLE `filiaal` (
  `idfiliaal` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `klant`
--

CREATE TABLE `klant` (
  `idklant` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `idproduct` int(11) NOT NULL,
  `omschrijving` varchar(45) DEFAULT NULL,
  `inhoudaantal` varchar(45) DEFAULT NULL,
  `eenheid_ideenheid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `aankoop`
--
ALTER TABLE `aankoop`
  ADD PRIMARY KEY (`klant_idklant`,`filiaal_idfiliaal`,`product_idproduct`,`datum`),
  ADD KEY `fk_aankoop_filiaal1_idx` (`filiaal_idfiliaal`),
  ADD KEY `fk_aankoop_product1_idx` (`product_idproduct`);

--
-- Indexes for table `eenheid`
--
ALTER TABLE `eenheid`
  ADD PRIMARY KEY (`ideenheid`),
  ADD UNIQUE KEY `omschrijving_UNIQUE` (`omschrijving`);

--
-- Indexes for table `filiaal`
--
ALTER TABLE `filiaal`
  ADD PRIMARY KEY (`idfiliaal`);

--
-- Indexes for table `klant`
--
ALTER TABLE `klant`
  ADD PRIMARY KEY (`idklant`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`idproduct`),
  ADD KEY `fk_product_eenheid1_idx` (`eenheid_ideenheid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `eenheid`
--
ALTER TABLE `eenheid`
  MODIFY `ideenheid` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `aankoop`
--
ALTER TABLE `aankoop`
  ADD CONSTRAINT `fk_aankoop_filiaal1` FOREIGN KEY (`filiaal_idfiliaal`) REFERENCES `filiaal` (`idfiliaal`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_aankoop_product1` FOREIGN KEY (`product_idproduct`) REFERENCES `product` (`idproduct`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_table1_klant` FOREIGN KEY (`klant_idklant`) REFERENCES `klant` (`idklant`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `product`
--
ALTER TABLE `product`
  ADD CONSTRAINT `fk_product_eenheid1` FOREIGN KEY (`eenheid_ideenheid`) REFERENCES `eenheid` (`ideenheid`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
