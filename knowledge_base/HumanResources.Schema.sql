USE [AdventureWorks2022]
GO
/****** Object:  Schema [HumanResources]    Script Date: 3/20/2025 10:13:39 PM ******/
CREATE SCHEMA [HumanResources]
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Contains objects related to employees and departments.' , @level0type=N'SCHEMA',@level0name=N'HumanResources'
GO
