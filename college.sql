-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 22, 2021 at 07:23 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `college`
--

-- --------------------------------------------------------

--
-- Table structure for table `marks`
--

CREATE TABLE `marks` (
  `student_no` varchar(10) DEFAULT NULL,
  `module_code` varchar(8) DEFAULT NULL,
  `mark` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `marks`
--

INSERT INTO `marks` (`student_no`, `module_code`, `mark`) VALUES
('20060101', 'CM0001', 80),
('20060101', 'CM0002', 65),
('20060101', 'CM0003', 50),
('20060102', 'CM0001', 75),
('20060102', 'CM0003', 45),
('20060102', 'CM0004', 70),
('20060103', 'CM0001', 60),
('20060103', 'CM0002', 75),
('20060103', 'CM0004', 60),
('20060104', 'CM0001', 55),
('20060104', 'CM0002', 40),
('20060104', 'CM0003', 45),
('20060105', 'CM0001', 55),
('20060105', 'CM0002', 50),
('20060105', 'CM0004', 65),
('1', 'AM99', 90);

-- --------------------------------------------------------

--
-- Table structure for table `modules`
--

CREATE TABLE `modules` (
  `module_code` varchar(8) DEFAULT NULL,
  `module_name` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `modules`
--

INSERT INTO `modules` (`module_code`, `module_name`) VALUES
('CM0001', 'Databases'),
('CM0002', 'Programming Language'),
('CM0003', 'Operating Systems'),
('CM0004', 'Graphics');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `student_no` varchar(10) DEFAULT NULL,
  `surname` varchar(20) DEFAULT NULL,
  `forename` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`student_no`, `surname`, `forename`) VALUES
('20060101', 'Dickens', 'Charles'),
('20060102', 'ApGwilym', 'Dafydd'),
('20060103', 'Zola', 'Emile'),
('20060104', 'Mann', 'Thomas'),
('20060105', 'Stevenson', 'Robert');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
