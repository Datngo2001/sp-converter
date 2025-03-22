USE [AdventureWorks2022]
GO
/****** Object:  Schema [Sales]    Script Date: 3/20/2025 10:13:39 PM ******/
CREATE SCHEMA [Sales]
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Contains objects related to customers, sales orders, and sales territories.' , @level0type=N'SCHEMA',@level0name=N'Sales'
GO
