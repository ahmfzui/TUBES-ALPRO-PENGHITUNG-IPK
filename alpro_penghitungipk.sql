-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3308
-- Generation Time: Jun 09, 2023 at 06:40 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `alpro_penghitungipk`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id_admin` int(12) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `status` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id_admin`, `nama`, `status`) VALUES
(1001, 'Muhammad Rafi Syihan', 'Team IT'),
(1002, 'Ahmad Fauzi', 'Team IT'),
(1003, 'I Putu Bagus Widya Wijaya Pratama ', 'Team IT');

-- --------------------------------------------------------

--
-- Table structure for table `mahasiswa`
--

CREATE TABLE `mahasiswa` (
  `nim` int(12) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `prodi` varchar(60) NOT NULL,
  `fakultas` varchar(60) NOT NULL,
  `semester1` decimal(3,2) DEFAULT NULL,
  `semester2` decimal(3,2) DEFAULT NULL,
  `semester3` decimal(3,2) DEFAULT NULL,
  `semester4` decimal(3,2) DEFAULT NULL,
  `semester5` decimal(3,2) DEFAULT NULL,
  `semester6` decimal(3,2) DEFAULT NULL,
  `semester7` decimal(3,2) DEFAULT NULL,
  `semester8` decimal(3,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mahasiswa`
--

INSERT INTO `mahasiswa` (`nim`, `nama`, `prodi`, `fakultas`, `semester1`, `semester2`, `semester3`, `semester4`, `semester5`, `semester6`, `semester7`, `semester8`) VALUES
(1202220263, 'Ahmad Fauzi', 'Sistem Informasi', 'Fakultas Rekayasa Industri', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(1202223040, 'I Putu Bagus Widya Wijaya Pratama', 'Sistem Informasi', 'Fakultas Rekayasa Industri', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(1202223384, 'Muhammad Rafi Syihan', 'Sistem Informasi', 'Fakultas Rekayasa Industri', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `nilai`
--

CREATE TABLE `nilai` (
  `nim` varchar(12) NOT NULL,
  `mata_kuliah` varchar(100) NOT NULL,
  `nilai` varchar(3) NOT NULL,
  `sks` int(3) NOT NULL,
  `semester` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `semester1`
--

CREATE TABLE `semester1` (
  `mata_kuliah` varchar(100) NOT NULL,
  `sks` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `semester1`
--

INSERT INTO `semester1` (`mata_kuliah`, `sks`) VALUES
('Literasi Teknologi', 2),
('Pembentukan Karakter', 1),
('Bahasa Inggris', 2),
('Kalkulus', 3),
('Pengantar Sistem Informasi', 3),
('Sistem Enterprise', 3),
('Matematika Diskrit', 3),
('Pengantar Pemrograman dan Logika', 3);

-- --------------------------------------------------------

--
-- Table structure for table `semester2`
--

CREATE TABLE `semester2` (
  `mata_kuliah` varchar(100) NOT NULL,
  `sks` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `semester2`
--

INSERT INTO `semester2` (`mata_kuliah`, `sks`) VALUES
('Probabilitas dan Statistika', 2),
('Matriks dan Ruang Vektor', 3),
('Algoritma dan Pemrograman', 4),
('Dasar Keuangan Sistem Informasi', 3),
('Kepemimpinan dan Komunikasi Interpersonal', 2),
('Sistem Basis Data', 3),
('Bahasa Inggris II', 3);

-- --------------------------------------------------------

--
-- Table structure for table `semester3`
--

CREATE TABLE `semester3` (
  `mata_kuliah` varchar(100) NOT NULL,
  `sks` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `semester3`
--

INSERT INTO `semester3` (`mata_kuliah`, `sks`) VALUES
('Pemrograman Berorientasi Objek', 3),
('Pemodelan Proses Bisnis', 3),
('Perilaku Organisasi', 3),
('Desain Jaringan Komputer dan Komunikasi Data', 3),
('Desain Pengalaman Pengguna', 2),
('Statistika Industri', 3);

-- --------------------------------------------------------

--
-- Table structure for table `semester4`
--

CREATE TABLE `semester4` (
  `mata_kuliah` varchar(100) NOT NULL,
  `sks` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `semester4`
--

INSERT INTO `semester4` (`mata_kuliah`, `sks`) VALUES
('Analisis dan Perancangan Sistem Informasi', 3),
('Perancangan Interaksi', 3),
('Rekayasa Proses Bisnis', 3),
('Manajemen Jaringan Komputer', 3),
('Manajemen Layanan TI', 3),
('Sistem Akuntansi dan Manajemen Keuangan', 3),
('Pengujian Dan Implementasi Sistem', 2);

-- --------------------------------------------------------

--
-- Table structure for table `semester5`
--

CREATE TABLE `semester5` (
  `mata_kuliah` varchar(100) NOT NULL,
  `sks` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `semester5`
--

INSERT INTO `semester5` (`mata_kuliah`, `sks`) VALUES
('Manajemen Rantai Pasok', 3),
('Arsitektur Enterprise', 3),
('Manajemen Proyek Sistem Informasi', 3),
('Pengembangan Aplikasi Website', 3),
('Data Warehouse dan Business Intelligence', 4),
('Dasar Sistem Operasi', 3);

-- --------------------------------------------------------

--
-- Table structure for table `semester6`
--

CREATE TABLE `semester6` (
  `mata_kuliah` varchar(100) NOT NULL,
  `sks` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `semester6`
--

INSERT INTO `semester6` (`mata_kuliah`, `sks`) VALUES
('Kewarganegaraan', 2),
('Keamanan Sistem Informasi', 4),
('Rekayasa Perangkat Lunak: Capstone Project', 4),
('Tata Kelola dan Manajemen Teknologi Informasi', 3),
('Integrasi Aplikasi Enterprise', 3),
('Kerja Praktek dan Pengabdian Masyarakat', 2),
('Etika Profesi, Regulasi Teknologi Informasi dan Properti Intelektual', 2);

-- --------------------------------------------------------

--
-- Table structure for table `semester7`
--

CREATE TABLE `semester7` (
  `mata_kuliah` varchar(100) NOT NULL,
  `sks` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `semester7`
--

INSERT INTO `semester7` (`mata_kuliah`, `sks`) VALUES
('Metode Penelitian dan Penyusunan Karya Ilmiah', 2),
('Pelatihan dan Sertifikasi', 3),
('Kewirausahaan', 2),
('Pendidikan Agama', 2),
('MKPP/MKBM I', 3),
('MKPP/MKBM II', 3);

-- --------------------------------------------------------

--
-- Table structure for table `semester8`
--

CREATE TABLE `semester8` (
  `mata_kuliah` varchar(100) NOT NULL,
  `sks` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `semester8`
--

INSERT INTO `semester8` (`mata_kuliah`, `sks`) VALUES
('Tugas Akhir', 4),
('Pancasila', 2),
('Bahasa Indonesia', 2),
('MKPP/MKBM III', 3),
('MKPP/MKBM IV', 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id_admin`);

--
-- Indexes for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
  ADD PRIMARY KEY (`nim`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
