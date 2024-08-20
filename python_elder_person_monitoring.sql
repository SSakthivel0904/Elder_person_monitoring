-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 04, 2023 at 03:26 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `python_elder_person_monitoring`
--

-- --------------------------------------------------------

--
-- Table structure for table `care_taker_details`
--

CREATE TABLE `care_taker_details` (
  `id` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `care_taker_details`
--

INSERT INTO `care_taker_details` (`id`, `name`, `contact`, `email`, `address`, `username`, `password`, `status`, `report`) VALUES
(1, 'arun', '987543210', 'arun@gmail.com', 'trichy', 'arun', '123', '0', '0');

-- --------------------------------------------------------

--
-- Table structure for table `query_details`
--

CREATE TABLE `query_details` (
  `id` int(100) NOT NULL,
  `query` varchar(100) NOT NULL,
  `answer` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `query_details`
--

INSERT INTO `query_details` (`id`, `query`, `answer`, `status`, `report`) VALUES
(1, 'i am sad', 'whats your problem', 'Sad', '0'),
(2, 'feel alone', 'why are you feel alone', 'Sad', '0');
