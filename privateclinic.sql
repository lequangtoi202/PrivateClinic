-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: privateclinic
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bac_si`
--

DROP TABLE IF EXISTS `bac_si`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bac_si` (
  `maBS` bigint NOT NULL,
  `chungChi` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `chuyenMon` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`maBS`),
  UNIQUE KEY `maBS` (`maBS`),
  CONSTRAINT `bac_si_ibfk_1` FOREIGN KEY (`maBS`) REFERENCES `nhan_vien` (`maNV`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bac_si`
--

LOCK TABLES `bac_si` WRITE;
/*!40000 ALTER TABLE `bac_si` DISABLE KEYS */;
INSERT INTO `bac_si` VALUES (2,'Chứng chỉ tham gia lớp định hướng gia liễu cơ bản khu vực miền Nam','Da liễu');
/*!40000 ALTER TABLE `bac_si` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `benh_nhan`
--

DROP TABLE IF EXISTS `benh_nhan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `benh_nhan` (
  `maBN` bigint NOT NULL AUTO_INCREMENT,
  `hoTen` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dienThoai` varchar(11) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ngaySinh` date NOT NULL,
  `gioiTinh` tinyint(1) NOT NULL,
  `diaChi` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`maBN`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `benh_nhan`
--

LOCK TABLES `benh_nhan` WRITE;
/*!40000 ALTER TABLE `benh_nhan` DISABLE KEYS */;
INSERT INTO `benh_nhan` VALUES (1,'Cao Nguyên Thụy','0928943482','thuy.cn@gmail.com','2003-01-02',0,'Nguyễn Văn Trỗi, Phú Nhuận'),(2,'Đoàn Gia Huy','0872947833','huy.dg@gmail.com','2003-02-05',1,'Nguyễn Thị Thập, Quận 7, TPHCM'),(3,'Ngô Minh Thành','0976264627','thanh.nm@gmail.com','1999-10-03',1,'Phường 6 Nguyễn Kiệm Gò Vấp');
/*!40000 ALTER TABLE `benh_nhan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ct_ds_kham`
--

DROP TABLE IF EXISTS `ct_ds_kham`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ct_ds_kham` (
  `maCTDS` bigint NOT NULL AUTO_INCREMENT,
  `maBN` bigint NOT NULL,
  `maDS` bigint NOT NULL,
  `maTG` bigint NOT NULL,
  PRIMARY KEY (`maCTDS`),
  KEY `maBN` (`maBN`),
  KEY `maDS` (`maDS`),
  KEY `maTG` (`maTG`),
  CONSTRAINT `ct_ds_kham_ibfk_1` FOREIGN KEY (`maBN`) REFERENCES `benh_nhan` (`maBN`),
  CONSTRAINT `ct_ds_kham_ibfk_2` FOREIGN KEY (`maDS`) REFERENCES `ds_kham_benh` (`maDS`) ON DELETE CASCADE,
  CONSTRAINT `ct_ds_kham_ibfk_3` FOREIGN KEY (`maTG`) REFERENCES `thoi_gian` (`maTG`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ct_ds_kham`
--

LOCK TABLES `ct_ds_kham` WRITE;
/*!40000 ALTER TABLE `ct_ds_kham` DISABLE KEYS */;
INSERT INTO `ct_ds_kham` VALUES (1,1,1,2),(2,2,2,13),(3,3,2,9);
/*!40000 ALTER TABLE `ct_ds_kham` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ds_kham_benh`
--

DROP TABLE IF EXISTS `ds_kham_benh`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ds_kham_benh` (
  `maDS` bigint NOT NULL AUTO_INCREMENT,
  `ngayKham` date NOT NULL,
  PRIMARY KEY (`maDS`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ds_kham_benh`
--

LOCK TABLES `ds_kham_benh` WRITE;
/*!40000 ALTER TABLE `ds_kham_benh` DISABLE KEYS */;
INSERT INTO `ds_kham_benh` VALUES (1,'2022-12-02'),(2,'2022-12-03');
/*!40000 ALTER TABLE `ds_kham_benh` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hoa_don`
--

DROP TABLE IF EXISTS `hoa_don`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hoa_don` (
  `maHD` bigint NOT NULL AUTO_INCREMENT,
  `tienThuoc` float NOT NULL,
  `tienKham` float NOT NULL,
  `tongTien` float NOT NULL,
  `created_date` datetime NOT NULL,
  `maPK` bigint NOT NULL,
  PRIMARY KEY (`maHD`),
  UNIQUE KEY `maPK` (`maPK`),
  CONSTRAINT `hoa_don_ibfk_1` FOREIGN KEY (`maPK`) REFERENCES `phieu_kham` (`maPK`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hoa_don`
--

LOCK TABLES `hoa_don` WRITE;
/*!40000 ALTER TABLE `hoa_don` DISABLE KEYS */;
INSERT INTO `hoa_don` VALUES (1,78000,100000,178000,'2022-12-02 00:00:00',1);
/*!40000 ALTER TABLE `hoa_don` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nhan_vien`
--

DROP TABLE IF EXISTS `nhan_vien`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nhan_vien` (
  `maNV` bigint NOT NULL AUTO_INCREMENT,
  `hoTen` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ngaySinh` date NOT NULL,
  `diaChi` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dienThoai` varchar(11) COLLATE utf8mb4_unicode_ci NOT NULL,
  `hinhAnh` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`maNV`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nhan_vien`
--

LOCK TABLES `nhan_vien` WRITE;
/*!40000 ALTER TABLE `nhan_vien` DISABLE KEYS */;
INSERT INTO `nhan_vien` VALUES (1,'Lê Quang Tới','2051052140toi@ou.edu.vn','2022-09-25','54 Dương Cát Lợi, Nhà Bè','0868832530',NULL),(2,'Nguyễn Văn Long','long.nv@gmail.com','1979-12-04','Nguyễn Văn Trỗi, Quận 3, TPHCM','0988969830','https://res.cloudinary.com/dbkikuoyy/image/upload/v1670160372/m37pwfbvjvtsfdqzwrfh.jpg'),(3,'Ngô Thị Kim Tài','kimtai.nt@gmail.com','1977-03-02','Nguyễn Thị Thập, Quận 7','0829174632','https://res.cloudinary.com/dbkikuoyy/image/upload/v1670160487/r1uwtghnteavjbtpbgx7.jpg'),(4,'Lê Thi Loan','loan.lt@gmail.com','1983-12-18','371, Nguyễn Kiệm, Gò Vấp','0284637182','https://res.cloudinary.com/dbkikuoyy/image/upload/v1670159691/swxu3k714ov9onved6bv.jpg');
/*!40000 ALTER TABLE `nhan_vien` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phieu_kham`
--

DROP TABLE IF EXISTS `phieu_kham`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phieu_kham` (
  `maPK` bigint NOT NULL AUTO_INCREMENT,
  `ngayKham` date DEFAULT NULL,
  `trieuChung` text COLLATE utf8mb4_unicode_ci,
  `chuanDoan` text COLLATE utf8mb4_unicode_ci,
  `maBN` bigint DEFAULT NULL,
  PRIMARY KEY (`maPK`),
  KEY `maBN` (`maBN`),
  CONSTRAINT `phieu_kham_ibfk_1` FOREIGN KEY (`maBN`) REFERENCES `benh_nhan` (`maBN`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phieu_kham`
--

LOCK TABLES `phieu_kham` WRITE;
/*!40000 ALTER TABLE `phieu_kham` DISABLE KEYS */;
INSERT INTO `phieu_kham` VALUES (1,'2022-12-02','Ho sốt, chảy nước mũi','Bj cảm thông thường',1),(2,'2022-12-05','Đau bụng, buồn nôn, nhức đầu','trúng thực, ăn phải thực phẩm không an toàn vệ sinh',2);
/*!40000 ALTER TABLE `phieu_kham` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phieu_thuoc`
--

DROP TABLE IF EXISTS `phieu_thuoc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phieu_thuoc` (
  `maPK_Thuoc` bigint NOT NULL AUTO_INCREMENT,
  `soLuong` int DEFAULT NULL,
  `cachDung` varchar(300) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `maThuoc` bigint NOT NULL,
  `maPK` bigint NOT NULL,
  PRIMARY KEY (`maPK_Thuoc`),
  KEY `maThuoc` (`maThuoc`),
  KEY `maPK` (`maPK`),
  CONSTRAINT `phieu_thuoc_ibfk_1` FOREIGN KEY (`maThuoc`) REFERENCES `thuoc` (`maThuoc`) ON DELETE CASCADE,
  CONSTRAINT `phieu_thuoc_ibfk_2` FOREIGN KEY (`maPK`) REFERENCES `phieu_kham` (`maPK`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phieu_thuoc`
--

LOCK TABLES `phieu_thuoc` WRITE;
/*!40000 ALTER TABLE `phieu_thuoc` DISABLE KEYS */;
INSERT INTO `phieu_thuoc` VALUES (1,2,'Xịt ngày 5 lần',3,1),(2,5,'Uống sau bữa ăn sáng, trưa, chiều',14,2);
/*!40000 ALTER TABLE `phieu_thuoc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qui_dinh`
--

DROP TABLE IF EXISTS `qui_dinh`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qui_dinh` (
  `maQD` bigint NOT NULL AUTO_INCREMENT,
  `tenQD` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `giaTri` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`maQD`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qui_dinh`
--

LOCK TABLES `qui_dinh` WRITE;
/*!40000 ALTER TABLE `qui_dinh` DISABLE KEYS */;
INSERT INTO `qui_dinh` VALUES (1,'tiền khám','100000'),(2,'số lượng tối đa','40');
/*!40000 ALTER TABLE `qui_dinh` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tai_khoan`
--

DROP TABLE IF EXISTS `tai_khoan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tai_khoan` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `username` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `avatar` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  `user_role` enum('ADMIN','NURSE','DOCTOR','STAFF') COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `maNV` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `maNV` (`maNV`),
  CONSTRAINT `tai_khoan_ibfk_1` FOREIGN KEY (`maNV`) REFERENCES `nhan_vien` (`maNV`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tai_khoan`
--

LOCK TABLES `tai_khoan` WRITE;
/*!40000 ALTER TABLE `tai_khoan` DISABLE KEYS */;
INSERT INTO `tai_khoan` VALUES (1,'admin','admin','e10adc3949ba59abbe56e057f20f883e','avatar',1,'ADMIN',1),(2,'tai','kimtai','202cb962ac59075b964b07152d234b70','https://res.cloudinary.com/dbkikuoyy/image/upload/v1669949105/ijtfnqsilze94uiyrh99.jpg',1,'NURSE',3),(3,'loan','loanlt','202cb962ac59075b964b07152d234b70','https://res.cloudinary.com/dbkikuoyy/image/upload/v1669949142/ovqd3hfruqykl5a5iike.jpg',1,'STAFF',4),(4,'long','longnv','202cb962ac59075b964b07152d234b70','https://res.cloudinary.com/dbkikuoyy/image/upload/v1669949175/c665ihehbqxeims9m4vu.jpg',1,'DOCTOR',2);
/*!40000 ALTER TABLE `tai_khoan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `thoi_gian`
--

DROP TABLE IF EXISTS `thoi_gian`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `thoi_gian` (
  `maTG` bigint NOT NULL AUTO_INCREMENT,
  `gio` time NOT NULL,
  PRIMARY KEY (`maTG`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `thoi_gian`
--

LOCK TABLES `thoi_gian` WRITE;
/*!40000 ALTER TABLE `thoi_gian` DISABLE KEYS */;
INSERT INTO `thoi_gian` VALUES (1,'08:00:00'),(2,'08:30:00'),(3,'09:00:00'),(4,'09:30:00'),(5,'10:00:00'),(6,'10:30:00'),(7,'11:00:00'),(8,'13:00:00'),(9,'13:30:00'),(10,'14:00:00'),(11,'14:30:00'),(12,'15:00:00'),(13,'15:30:00'),(14,'16:00:00'),(15,'16:30:00'),(16,'17:00:00'),(17,'17:30:00'),(18,'18:00:00'),(19,'18:30:00'),(20,'19:00:00'),(21,'19:30:00');
/*!40000 ALTER TABLE `thoi_gian` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `thuoc`
--

DROP TABLE IF EXISTS `thuoc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `thuoc` (
  `maThuoc` bigint NOT NULL AUTO_INCREMENT,
  `tenThuoc` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `moTa` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `soLuong` int NOT NULL,
  `giaBan` float NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `donVi` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `hinhAnh` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`maThuoc`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `thuoc`
--

LOCK TABLES `thuoc` WRITE;
/*!40000 ALTER TABLE `thuoc` DISABLE KEYS */;
INSERT INTO `thuoc` VALUES (1,'Cao dán Salonpas Hisamitsu','Miếng dán Salonpas là sản phẩm của Dược Phẩm Hisamitsu Việt Nam với thành phần chính là Methyl salicylate, DL-Camphor , L-Menthol, Tocopherol acetate. Thuốc có tác dụng làm giảm đau, kháng viêm trong các cơn đau liên quan đến đau vai, đau lưng, đau cơ, mỏi cơ, bầm tím, bong gân, căng cơ, đau đầu, đau răng.Quy cách đóng gói:Bao 2 miếng (6, 5 cm x 4, 2 cm), bao 10 miếng (6, 5 cm x 4, 2 cm).Hộp 1 bao 10 miếng (6, 5 cm x 4, 2 cm), hộp 1 bao 20 miếng (6, 5 cm x 4, 2 cm).Hộp 2 bao 10 miếng (6, 5 cm x 4, 2 cm), hộp 4 bao 10 miếng (6, 5 cm x 4, 2 cm).',100,12000,1,'Hộp','https://res.cloudinary.com/dbkikuoyy/image/upload/v1669949476/ujqt9d4t82qfhpcoi8xl.webp'),(2,'Dung dịch Danospan Danapha ','Danospan Danapha 100 ml là sản phẩm của công ty cổ phần dược Danapha, thành phần chính là cao khô lá thường xuân. Thuốc được dùng điều trị viêm đường hô hấp cấp tính có kèm ho, điều trị triệu chứng trong bệnh lý viêm phế quản mạn tính.Danospan Danapha 100 ml được bào chế dưới siro. Một chai 100 ml chứa 0, 7 g cao khô lá thường xuân (tương ứng với 4, 55 g lá thường xuân).',100,60000,1,'Chai','https://res.cloudinary.com/dbkikuoyy/image/upload/v1669950361/bfrb4mxmgi2adpib5akr.webp'),(3,'Dung dịch vệ sinh mũi Nasomom Clean&Clear Reliv','Thuốc Nasomom Clean Clear là sản phẩm được sản xuất bởi Công ty Cổ phần Dược phẩm Đồng Nai. Dung dịch vệ sinh mũi Nasomom với thành phần chính từ natri clorid giúp vệ sinh hàng ngày, phòng ngừa viêm mũi, viêm xoang. Giảm các triệu chứng nghẹt mũi, sổ mũi, viêm mũi dị ứng, khò khè, khô rát mũi họng, cảm mạo ở trẻ em, trẻ nhỏ.Thuốc Nasomom Clean Clear được bào chế dưới dạng dung dịch vệ sinh mũi, mỗi chai 70ml chứa 630mg natri clorid, được đóng gói theo quy cách: Hộp 1 chai 70 ml.',100,39000,1,'Hộp','https://res.cloudinary.com/dbkikuoyy/image/upload/v1669950495/kjikywc7hitdlwrec5zp.webp'),(4,'Dung dịch nhỏ mắt Sancoba Santen','Dung dịch nhỏ mắt Sancoba được sản xuất bởi Công ty Santen Pharmaceutical Co, Ltd - Nhật Bản, có thành phần chính là cyanocobalamin. Dung dịch nhỏ mắt Sancoba được sử dụng trong trường hợp cải thiện sự dao động về điều tiết trong chứng mỏi mắt do điều tiết.Dung dịch nhỏ mắt Sancoba được bào chế dưới dạng dung dịch nhỏ mắt với dung dịch thân nước vô khuẩn, trong suốt, màu đỏ. Hộp 1 lọ nhựa 5ml.',100,52000,1,'Chai','https://res.cloudinary.com/dbkikuoyy/image/upload/v1669950593/hybiyz94dirdlls8z2ev.webp'),(5,'Dung dịch Calcium Corbiere Extra Sanofi','Dung dịch uống Calcium Corbiere Extra chỉ định điều trị trong các trường hợp sau:\r\n\r\nTình trạng thiếu canxi, đặc biệt trong các trường hợp có nhu cầu canxi cao như: Phụ nữ mang thai và cho con bú, trẻ em đang lớn,giai đoạn hồi phục, gãy xương, chứng còi xương.\r\nBổ sung canxi trong hỗ trợ điều trị loãng xương',100,195000,1,'Hộp','https://res.cloudinary.com/dbkikuoyy/image/upload/v1669950700/ozeqvteszxp8lohfihz6.webp'),(6,'Dung dịch Milian OPC','Dung dịch Milian bao gồm Xanh Methylen và Tím Genian là một thuốc sát trùng diệt vi sinh vật dùng để bôi ngoài da và niêm mạc.',100,25000,1,'Chai','https://res.cloudinary.com/dbkikuoyy/image/upload/v1669950859/shb0d9xphtgqd28mydhu.webp'),(7,'Gel thuốc Lazanex Adapalene 0.1% Yash','Thuốc bôi Azanex Gel 10g là sản phẩm Yash Medicare (Ấn Độ) chứa hoạt chất Adapalene để điều trị trứng cá từ nhẹ đến trung bình khi có nhiều nhân trứng cá, sẩn và mụn mủ.',100,29000,1,'Tuýp','https://res.cloudinary.com/dbkikuoyy/image/upload/v1669950970/xcfxeo1jlxjz14i62wqc.webp'),(8,'Gel Oxy10 Rohto','Gel Oxy10 Rohto hỗ trợ điều trị mụn trứng cá nặng và mụn trứng cá có mủ (10g)\r\n',100,45000,1,'Tuýp','https://res.cloudinary.com/dbkikuoyy/image/upload/v1669951093/z7q2q5mjfnvwbanysnr5.webp'),(9,'Gel Daivonex LEO','Daivonex là sản phẩm của nhà sản xuất LEO (Ireland), với thành phần chính calcipotriol. Đây là thuốc dùng để điều trị tại chỗ bệnh vẩy nến mảng (vẩy nến thông thường). Thuốc có thể được sử dụng kết hợp với acitretin, cyclosporin hoặc các corticosteroid tại chỗ.',100,38000,1,'Tuýp','https://res.cloudinary.com/dbkikuoyy/image/upload/v1669951230/k6ilbn7ymjlg6an7rxyt.webp'),(10,'Gel thuốc Hiteen Phil','HITEENGEL được sản xuất bởi Công ty TNHH Phil Inter Pharma, với thành phần chính Tretinoin và Erythromycin, là thuốc dùng để điều trị mụn trứng cá dạng vi u nang hoặc kèm viêm, mụn trứng cá mủ sần, mụn trứng cá kết khối (kết hợp với các phương pháp trị liệu đặc biệt khác), mụn trứng cá do dùng thuốc gây ra như corticoid, vitamin B12, vitamin D, isoniazide và các thuốc thuộc nhóm barbituric, iod, brom.',100,42000,1,'Tuýp','https://res.cloudinary.com/dbkikuoyy/image/upload/v1669951305/gbmhjpzus72vcrcrpj39.webp'),(11,'Gel Metrogyl Denta Unique Pharma','Metrogyl Denta của công ty Unique Pharmaceutical Labs, thành phần chính là metronidazole benzoate BP. Thuốc được dùng trong điều trị các bệnh nha chu mãn tính để hỗ trợ cho các điều trị truyền thống.Metrogyl Denta được bào chế dưới dạng gel dùng bôi lợi. Hộp 01 tuýp 10 g hoặc 20 g.',100,39000,1,'Tuýp','https://res.cloudinary.com/dbkikuoyy/image/upload/v1669951370/xx6gv5i5sxbvcn13grww.webp'),(12,'Hỗn dịch uống Mutecium-M Mekophar','Hỗn dịch uống Mutecium-M Mekophar điều trị triệu chứng nôn, buồn nôn (30ml)',100,48000,1,'Chai','https://res.cloudinary.com/dbkikuoyy/image/upload/v1669951477/k4fvnjsdnsmaa9hbhk1h.webp'),(13,'Hoạt huyết dưỡng não Cerecaps Mediplantex','Thuốc Hoạt Huyết Dưỡng Não Cerecaps là dược phẩm của Công ty Cổ phần Dược Trung Ương Mediplantex, có thành phần chính cao khô hỗn hợp các dược liệu, giúp điều trị hiệu quả các trường hợp như: Suy giảm trí nhớ, đau đầu, hoa mắt chóng mặt, hay cáu gắt ở người có tuổi, thiếu máu, căng thẳng, mệt mỏi, mất tập trung, chứng tê bì, nhức mỏi chân tay (do thiểu năng tuần hoàn ngoại vi)...',100,71000,1,'Hộp','https://res.cloudinary.com/dbkikuoyy/image/upload/v1669951561/gkebczusjnq7torfjxa4.webp'),(14,'Hỗn dịch uống Gellux 1g Đạt Vi Phú','Gellux 1g của Công ty Cổ phần Dược Phẩm Đạt Vi Phú, thành phần chính sucralfat là một muối nhôm của sulfat disaccarid, dùng điều trị ngắn ngày loét tá tràng, dạ dày lành tính, viêm dạ dày mạn tính; phòng chảy máu dạ dày, ruột do stress; viêm loét miệng do hóa trị liệu ung thư hoặc nguyên nhân khác do thực quản, dạ dày; viêm thực quản và dự phòng loét dạ dày tá tràng tái phát.',100,64000,1,'Hộp','https://res.cloudinary.com/dbkikuoyy/image/upload/v1669951637/w1a4cy6y2pr6jb6qzd46.webp'),(15,'Kem bôi da Soslac G3 Ampharco','Thuốc Soslac G3 được sản xuất bởi Công ty cổ phần dược phẩm Ampharco U.S.A – Việt Nam, có thành phần chính là gentamycin, betamethason và clotrimazol. Thuốc Soslac G3 được chỉ định trong điều trị viêm da dị ứng, lang ben, hăm da, viêm da nhiễm nấm như nấm da đầu, da tay, Eczema, ....Thuốc Soslac G3 được bào chế dưới dạng kem bôi ngoài da. Hộp 1 tuýp 15 g.',100,26000,1,'Tuýp','https://res.cloudinary.com/dbkikuoyy/image/upload/v1669951728/hflmhgdevzbukkjzxcyv.webp'),(16,'Kem bôi Panthenol Pharmedic','Thuốc Panthenol là sản phẩm của Công ty Cổ phần Dược phẩm dược liệu Pharmedic, có thành phần là D – Panthenol với hàm lượng 0, 5 g. Thuốc được chỉ định trong các trường hợp: Điều trị tổn thương da, nứt da chân, nứt đầu vú, rạn da bụng do mang thai, hăm đỏ vùng mông của trẻ sơ sinh.Thuốc Panthenol được bào chế dạng kem bôi da, kem màu trắng đến trắng ngà, có mùi thơm, không tách lớp, dính vào da khi bôi. Quy cách đóng gói là hộp 1 tuýp 10 g.',100,18000,1,'Tuýp','https://res.cloudinary.com/dbkikuoyy/image/upload/v1669951807/ufbhev0pvwt19g1yju9d.webp'),(17,'Nước súc miệng Medoral Merap','Súc Miệng Họng Medoral Merap của Công ty cổ phần tập đoàn Merap, thành phần chính chlorhexidin digluconat. Thuốc được sử dụng để hỗ trợ điều trị và ngăn ngừa bệnh viêm nhiễm khuẩn ở họng miệng (như viêm họng, viêm amidan, viêm lợi, viêm miệng); sát khuẩn, ức chế sự hình thành mảng bám trên răng; vệ sinh răng miệng; đẩy mạnh làm lành vết thương sau phẫu thuật hoặc điều trị nha khoa; kiểm soát loét miệng tái phát; kiểm soát răng giả gây viêm miệng và nhiễm nấm Candida miệng.',100,91000,1,'Hộp','https://res.cloudinary.com/dbkikuoyy/image/upload/v1669951866/btzi8rfsthbafolljmeq.webp'),(18,'Nước Oxy Già OPC','Nước oxy già VP 3% được chỉ định dùng trong các trường hợp sau:\r\nDùng để diệt khuẩn dụng cụ y tế, bề mặt trong y tế.',100,15000,1,'Hộp','https://res.cloudinary.com/dbkikuoyy/image/upload/v1669951940/lepzcmjqt4elg7j5hf7c.webp');
/*!40000 ALTER TABLE `thuoc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `yta`
--

DROP TABLE IF EXISTS `yta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `yta` (
  `maYT` bigint NOT NULL,
  `bangCap` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`maYT`),
  UNIQUE KEY `maYT` (`maYT`),
  CONSTRAINT `yta_ibfk_1` FOREIGN KEY (`maYT`) REFERENCES `nhan_vien` (`maNV`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `yta`
--

LOCK TABLES `yta` WRITE;
/*!40000 ALTER TABLE `yta` DISABLE KEYS */;
INSERT INTO `yta` VALUES (3,'Cử nhân điều dưỡng');
/*!40000 ALTER TABLE `yta` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-05 20:25:22
