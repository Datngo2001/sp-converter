USE [AdventureWorks2022]
GO
/****** Object:  Schema [Person]    Script Date: 3/20/2025 10:13:39 PM ******/
CREATE SCHEMA [Person]
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Contains objects related to names and addresses of customers, vendors, and employees' , @level0type=N'SCHEMA',@level0name=N'Person'
GO
