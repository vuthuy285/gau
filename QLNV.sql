USE QLNV
drop table Thong_tin
 ----------------------------
﻿
CREATE TABLE PHONG_BAN
(
	MaPB int PRIMARY KEY,
	TenPB nvarchar(30) NOT NULL,
	SDTPB varchar (20),
	DiaChi nvarchar(30) NOT NULL,
	CONSTRAINT UNQ_SDTPB UNIQUE (SDTPB)
);

INSERT INTO PHONG_BAN (MaPB, TenPB, SDTPB, DiaChi)
VALUES 
(1001, N'Kế toán', '086574283150', 'P401 Tòa B'),
(1002, N'Marketing', '014438533088', 'P402 Tòa B'),
(1003, N'Kỹ thuật', '020084642282', 'P305 Tòa A'),
(1004, N'Hành chính', '015670436628', 'P306 Tòa A')
--select * from PHONG_BAN
--drop table PHONG_BAN
--------------------------------
CREATE TABLE CHUC_VU
(
	MaCV int PRIMARY KEY,
	TenCV nvarchar(30) NOT NULL
);

INSERT INTO CHUC_VU (MaCV, TenCV)
VALUES 
(2001, N'Trưởng phòng'),
(2002, N'Nhân viên')
--select * from CHUC_VU
--drop table CHUC_VU

----------------------------------------------------------
CREATE TABLE TRINH_DO_HOC_VAN
(
	MaTDHV int PRIMARY KEY,
	TenTDHV nvarchar(30) NOT NULL,
	ChuyenNganh nvarchar(30) NOT NULL
)

INSERT INTO TRINH_DO_HOC_VAN (MaTDHV, TenTDHV, ChuyenNganh)
VALUES 
(3001, N'Cao học', N'Kinh tế'),
(3002, N'Cao học', N'CNTT'),
(3003, N'Đại học', N'Kinh tế'),
(3004, N'Đại học', N'CNTT'),
(3005, N'Đại học', N'Văn thư'),
(3006, N'Đại học', N'Marketing'),
(3007, N'Cao đẳng', N'Kinh tế'),
(3008, N'Cao đẳng', N'CNTT'),
(3009, N'Cao đẳng', N'Văn thư'),
(3010, N'Cao đẳng', N'Marketing')

--select * from TRINH_DO_HOC_VAN
--drop table TRINH_DO_HOC_VAN
-----------------------------------------
CREATE TABLE HOP_DONG_LAO_DONG
(
	MaHD int,
	MaNV int,
	LoaiHD nvarchar(30) NOT NULL,
	NgayBD date,
	NgayKT date,
	CONSTRAINT PK_HDLD PRIMARY KEY (MaHD, MaNV),
	CONSTRAINT CK_HDLD CHECK(NgayBD < NgayKT)
)

--select * from HOP_DONG_LAO_DONG
--drop table HOP_DONG_LAO_DONG
------------------------------------------
CREATE TABLE LUONG
(
	BacLuong int PRIMARY KEY,
	LuongCB int NOT NULL,
	HSL float NOT NULL
)

INSERT INTO LUONG (BacLuong, LuongCB, HSL)
VALUES 
(1, 3000000, 1.35),
(2, 3000000, 1.5),
(3, 5000000, 1.35),
(4, 5000000, 1.5),
(5, 8000000, 1.5),
(6, 8000000, 1.68),
(7, 8000000, 1.86),
(8, 10000000, 1.5),
(9, 10000000, 1.68),
(10, 10000000, 1.86)

--select * from LUONG
--drop table LUONG
------------------------------------------------
CREATE TABLE NHAN_VIEN 
(
	ID int PRIMARY KEY,
	UserName varchar(30) NOT NULL,
	Pass varchar(50) NOT NULL,
	Email varchar(50),
	HoTen nvarchar(100) NOT NULL,
	SDT varchar (20),
	NgaySinh date CHECK (NgaySinh < GETDATE()),
	MaPB int,
	MaCV int,
	MaTDHV int,
	BacLuong int,
	CONSTRAINT FK1_NV FOREIGN KEY (MaPB) REFERENCES PHONG_BAN (MaPB),
	CONSTRAINT FK2_NV FOREIGN KEY (MaCV) REFERENCES CHUC_VU (MaCV),
	CONSTRAINT FK3_NV FOREIGN KEY (MaTDHV) REFERENCES TRINH_DO_HOC_VAN (MaTDHV),
	CONSTRAINT FK4_NV FOREIGN KEY (BacLuong) REFERENCES LUONG (BacLuong),
	CONSTRAINT UNQ_UserName UNIQUE (UserName),
	CONSTRAINT UNQ_SDT UNIQUE (SDT)
)

INSERT INTO NHAN_VIEN (ID, UserName, Pass, Email, HoTen, SDT, NgaySinh, MaPB, MaCV, MaTDHV, BacLuong)
VALUES 
(0001, 'admin', 'poH', 'support@gmail.com', N'Trịnh Đình Hợp', '0945928535', '1982/12/14', NULL, NULL, NULL, NULL),
(0002, 'Trong', 'gnorT', 'trong1214@gmail.com', N'Trần Bảo Trọng', '0639768345', '1995/12/14', 1001, 2001, 3001, 9),
(0003, 'Duong', 'ngouD', 'duong0512@gmail.com', N'Lê Thùy Dương', '0952148077', '1997/05/12', 1002, 2001, 3006, 4),
(0004, 'Thao', 'Thao123', 'thao1120@gmail.com', N'Trần Phương Thảo', '0910466947', '1995/11/20', 1003, 2001, 3002, 7),
(0005, 'An', 'An123', 'an1214@gmail.com', N'TLê Trường An', '0166490621', '1995/12/14', 1004, 2001, 3005, 2),

(0006, 'Giang', 'ngaiG', 'giang0221@gmail.com', N'Phạm Thị Hương Giang', '0703811508', '1999/02/21', 1001, 2002, 3003, 9),
(0007, 'Bao', 'Bao123', 'bao1214@gmail.com', N'Trần Anh Bảo', '0391683288', '1995/12/14', 1002, 2002, 3010, 3),
(0008, 'Dung', 'Dung123', 'dung0512@gmail.com', N'Lê Thùy Dung', '0471913201', '1997/05/12', 1003, 2002, 3004, 6),
(0009, 'Tinh', 'Tinh123', 'tinh0330@gmail.com', N'TPhạm Trung Tính', '0445774393', '1996/03/30', 1004, 2002, 3009, 1),

(0010, 'Hai', 'Hai123', 'hai1120@gmail.com', N'Lê An Hải', '0516331082', '1995/11/20', 1001, 2002, 3007, 8),
(0011, 'Huong', 'gnouH', 'huong0221@gmail.com', N'Phạm Thị Giang Hương', '0616184898', '1999/02/21', 1002, 2002, 3010, 3),
(0012, 'Thuc', 'Thuc123', 'thuc0412@gmail.com', N'Đoàn Duy Thức', '0786597265', '1994/04/12', 1003, 2002, 3008, 5),
(0013, 'Thong', 'gnohT', 'thong0412@gmail.com', N'Dương Tuấn Thông', '0503979074', '1991/04/12', 1004, 2002, 3009, 1)

--select * from NHAN_VIEN
--drop table NHAN_VIEN



SELECT ID, USERNAME, PASS, HOTEN, EMAIL, SDT, TENPB, TENCV, CHUYENNGANH, LUONGCB*HSL AS LUONG
FROM (NHAN_VIEN JOIN LUONG ON NHAN_VIEN.BacLuong=LUONG.BacLuong) JOIN PHONG_BAN ON NHAN_VIEN.MaPB=PHONG_BAN.MaPB 
																	JOIN CHUC_VU ON NHAN_VIEN.MaCV=CHUC_VU.MaCV
																	JOIN TRINH_DO_HOC_VAN ON TRINH_DO_HOC_VAN.MaTDHV=NHAN_VIEN.MaTDHV
WHERE USERNAME='TRONG' and pass='gnorT'