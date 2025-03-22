USE [AdventureWorks2022]
GO
/****** Object:  Schema [Production]    Script Date: 3/20/2025 10:13:39 PM ******/
CREATE SCHEMA [Production]
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Contains objects related to products, inventory, and manufacturing.' , @level0type=N'SCHEMA',@level0name=N'Production'
GO
