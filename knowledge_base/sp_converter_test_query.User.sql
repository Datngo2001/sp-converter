CREATE USER [sp_converter_test_query] FOR LOGIN [sp_converter_test_query] WITH DEFAULT_SCHEMA=[dbo]
GO
ALTER ROLE [db_datareader] ADD MEMBER [sp_converter_test_query]
GO
