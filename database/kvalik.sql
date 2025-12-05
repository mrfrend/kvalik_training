-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 05, 2025 at 07:41 PM
-- Server version: 8.0.30
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kvalik`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts`
--

CREATE TABLE `accounts` (
  `id` int NOT NULL,
  `login` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `type_account_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `accounts`
--

INSERT INTO `accounts` (`id`, `login`, `password`, `type_account_id`) VALUES
(1, 'root', 'root', 1);

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `id` int NOT NULL,
  `category_name` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`id`, `category_name`) VALUES
(31, 'Одноместный стандарт'),
(32, 'Одноместный эконом'),
(33, 'Стандарт двухместный с 2 раздельными кроватями'),
(34, 'Эконом двухместный с 2 раздельными кроватями'),
(35, '3-местный бюджет'),
(36, 'Бизнес с 1 или 2 кроватями'),
(37, 'Двухкомнатный двухместный стандарт с 1 или 2 кроватями'),
(38, 'Студия'),
(39, 'Люкс с 2 двуспальными кроватями');

-- --------------------------------------------------------

--
-- Table structure for table `clients`
--

CREATE TABLE `clients` (
  `id` int NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `middle_name` varchar(50) DEFAULT NULL,
  `account_id` int DEFAULT NULL,
  `passport_series` char(4) NOT NULL,
  `passport_number` char(6) NOT NULL,
  `cause_visit` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `clients`
--

INSERT INTO `clients` (`id`, `first_name`, `last_name`, `middle_name`, `account_id`, `passport_series`, `passport_number`, `cause_visit`) VALUES
(1, 'Шевченко', 'Ольга', 'Викторовна', NULL, '', '', ''),
(2, 'Мазалова', 'Ирина', 'Львовна', NULL, '', '', ''),
(3, 'Семеняка', 'Юрий', 'Геннадьевич', NULL, '', '', ''),
(4, 'Савельев', 'Олег', 'Иванович', NULL, '', '', ''),
(5, 'Бунин', 'Эдуард', 'Михайлович', NULL, '', '', ''),
(6, 'Бахшиев', 'Павел', 'Иннокентьевич', NULL, '', '', ''),
(7, 'Тюренкова', 'Наталья', 'Сергеевна', NULL, '', '', ''),
(8, 'Любяшева', 'Галина', 'Аркадьевна', NULL, '', '', ''),
(9, 'Александров', 'Петр', 'Константинович', NULL, '', '', ''),
(10, 'Мазалова', 'Ольга', 'Николаевна', NULL, '', '', ''),
(11, 'Лапшин', 'Виктор', 'Романович', NULL, '', '', ''),
(12, 'Гусев', 'Семен', 'Петрович', NULL, '', '', ''),
(13, 'Гладилина', 'Вера', 'Михайловна', NULL, '', '', ''),
(14, 'Масюк', 'Динара', 'Викторовна', NULL, '', '', ''),
(15, 'Лукин', 'Илья', 'Федорович', NULL, '', '', ''),
(16, 'Петров', 'Станислав', 'Игоревич', NULL, '', '', ''),
(17, 'Филь', 'Марина', 'Федоровна', NULL, '', '', ''),
(18, 'Михайлов', 'Игорь', 'Вадимович', NULL, '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `reservation`
--

CREATE TABLE `reservation` (
  `id` int NOT NULL,
  `room_id` int NOT NULL,
  `client_id` int NOT NULL,
  `check_in` date NOT NULL,
  `check_out` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `reservation`
--

INSERT INTO `reservation` (`id`, `room_id`, `client_id`, `check_in`, `check_out`) VALUES
(1, 1, 1, '2025-02-14', '2025-03-02'),
(2, 1, 1, '2025-02-14', '2025-03-02'),
(3, 2, 2, '2025-02-28', NULL),
(4, 4, 3, '2025-02-23', '2025-02-02'),
(5, 5, 4, '2025-03-01', '2025-03-07'),
(6, 7, 5, '2025-02-27', '2025-04-22'),
(7, 7, 6, '2025-02-24', '2025-03-17'),
(8, 8, 7, '2025-02-15', '2025-03-20'),
(9, 9, 8, '2025-02-27', '2025-03-12'),
(10, 10, 9, '2025-02-14', '2025-02-02'),
(11, 11, 10, '2025-02-24', '2025-03-17'),
(12, 13, 11, '2025-02-25', '2025-03-07'),
(13, 15, 12, '2025-03-01', '2025-03-04'),
(14, 16, 13, '2025-02-02', '2025-02-02'),
(15, 17, 14, '2025-02-25', '2025-03-04'),
(16, 18, 15, '2025-02-25', '2025-03-04'),
(17, 19, 16, '2025-02-27', NULL),
(18, 23, 17, '2025-02-28', '2025-03-15'),
(19, 25, 18, '2025-02-11', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `rooms`
--

CREATE TABLE `rooms` (
  `id` int NOT NULL,
  `floor` int NOT NULL,
  `number` int NOT NULL,
  `category_id` int NOT NULL,
  `status_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `rooms`
--

INSERT INTO `rooms` (`id`, `floor`, `number`, `category_id`, `status_id`) VALUES
(1, 1, 101, 31, 1),
(2, 1, 102, 31, 1),
(3, 1, 103, 32, 2),
(4, 1, 104, 32, 1),
(5, 1, 105, 33, 1),
(6, 1, 106, 33, 2),
(7, 1, 107, 34, 1),
(8, 1, 108, 34, 1),
(9, 1, 109, 35, 1),
(10, 1, 110, 35, 1),
(11, 2, 201, 36, 1),
(12, 2, 202, 36, 2),
(13, 2, 203, 36, 1),
(14, 2, 204, 37, 3),
(15, 2, 205, 37, 1),
(16, 2, 206, 37, 1),
(17, 2, 207, 31, 1),
(18, 2, 208, 31, 1),
(19, 2, 209, 31, 1),
(20, 3, 301, 38, 2),
(21, 3, 302, 38, 2),
(22, 3, 303, 38, 1),
(23, 3, 304, 39, 1),
(24, 3, 305, 39, 2),
(25, 3, 306, 39, 2);

-- --------------------------------------------------------

--
-- Table structure for table `room_status`
--

CREATE TABLE `room_status` (
  `id` int NOT NULL,
  `status_name` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `room_status`
--

INSERT INTO `room_status` (`id`, `status_name`) VALUES
(1, 'Занят'),
(2, 'Чистый'),
(3, 'Назначен к уборке'),
(4, 'Грязный');

-- --------------------------------------------------------

--
-- Table structure for table `type_accounts`
--

CREATE TABLE `type_accounts` (
  `id` int NOT NULL,
  `role` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `type_accounts`
--

INSERT INTO `type_accounts` (`id`, `role`) VALUES
(1, 'admin'),
(2, 'chief'),
(3, 'client');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`id`),
  ADD KEY `type_acc_idx` (`type_account_id`);

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `clients`
--
ALTER TABLE `clients`
  ADD PRIMARY KEY (`id`),
  ADD KEY `acc_idx` (`account_id`);

--
-- Indexes for table `reservation`
--
ALTER TABLE `reservation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `room_id_idx` (`room_id`),
  ADD KEY `client_id_idx` (`client_id`);

--
-- Indexes for table `rooms`
--
ALTER TABLE `rooms`
  ADD PRIMARY KEY (`id`),
  ADD KEY `category_id_index` (`category_id`),
  ADD KEY `status_idx` (`status_id`);

--
-- Indexes for table `room_status`
--
ALTER TABLE `room_status`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `type_accounts`
--
ALTER TABLE `type_accounts`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts`
--
ALTER TABLE `accounts`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- AUTO_INCREMENT for table `clients`
--
ALTER TABLE `clients`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `reservation`
--
ALTER TABLE `reservation`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `rooms`
--
ALTER TABLE `rooms`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `room_status`
--
ALTER TABLE `room_status`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `type_accounts`
--
ALTER TABLE `type_accounts`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accounts`
--
ALTER TABLE `accounts`
  ADD CONSTRAINT `accounts_ibfk_1` FOREIGN KEY (`type_account_id`) REFERENCES `type_accounts` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `clients`
--
ALTER TABLE `clients`
  ADD CONSTRAINT `clients_ibfk_1` FOREIGN KEY (`account_id`) REFERENCES `accounts` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `reservation`
--
ALTER TABLE `reservation`
  ADD CONSTRAINT `reservation_ibfk_1` FOREIGN KEY (`room_id`) REFERENCES `rooms` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `reservation_ibfk_2` FOREIGN KEY (`client_id`) REFERENCES `clients` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `rooms`
--
ALTER TABLE `rooms`
  ADD CONSTRAINT `rooms_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `rooms_ibfk_2` FOREIGN KEY (`status_id`) REFERENCES `room_status` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
