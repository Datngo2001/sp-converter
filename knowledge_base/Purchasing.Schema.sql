USE [AdventureWorks2022]
GO
/****** Object:  Schema [Purchasing]    Script Date: 3/20/2025 10:13:39 PM ******/
CREATE SCHEMA [Purchasing]
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Contains objects related to vendors and purchase orders.' , @level0type=N'SCHEMA',@level0name=N'Purchasing'
GO
