USE [master]
GO
/****** Object:  Database [AdventureWorks2022]    Script Date: 3/20/2025 10:13:39 PM ******/
CREATE DATABASE [AdventureWorks2022]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'AdventureWorks2022', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\AdventureWorks2022.mdf' , SIZE = 204800KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'AdventureWorks2022_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\AdventureWorks2022_log.ldf' , SIZE = 73728KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO
ALTER DATABASE [AdventureWorks2022] SET COMPATIBILITY_LEVEL = 160
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [AdventureWorks2022].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [AdventureWorks2022] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [AdventureWorks2022] SET ANSI_NULLS ON 
GO
ALTER DATABASE [AdventureWorks2022] SET ANSI_PADDING ON 
GO
ALTER DATABASE [AdventureWorks2022] SET ANSI_WARNINGS ON 
GO
ALTER DATABASE [AdventureWorks2022] SET ARITHABORT ON 
GO
ALTER DATABASE [AdventureWorks2022] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [AdventureWorks2022] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [AdventureWorks2022] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [AdventureWorks2022] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [AdventureWorks2022] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [AdventureWorks2022] SET CONCAT_NULL_YIELDS_NULL ON 
GO
ALTER DATABASE [AdventureWorks2022] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [AdventureWorks2022] SET QUOTED_IDENTIFIER ON 
GO
ALTER DATABASE [AdventureWorks2022] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [AdventureWorks2022] SET  DISABLE_BROKER 
GO
ALTER DATABASE [AdventureWorks2022] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [AdventureWorks2022] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [AdventureWorks2022] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [AdventureWorks2022] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [AdventureWorks2022] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [AdventureWorks2022] SET READ_COMMITTED_SNAPSHOT ON 
GO
ALTER DATABASE [AdventureWorks2022] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [AdventureWorks2022] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [AdventureWorks2022] SET  MULTI_USER 
GO
ALTER DATABASE [AdventureWorks2022] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [AdventureWorks2022] SET DB_CHAINING OFF 
GO
ALTER DATABASE [AdventureWorks2022] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [AdventureWorks2022] SET TARGET_RECOVERY_TIME = 0 SECONDS 
GO
ALTER DATABASE [AdventureWorks2022] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [AdventureWorks2022] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'AdventureWorks2022', N'ON'
GO
ALTER DATABASE [AdventureWorks2022] SET QUERY_STORE = OFF
GO
USE [AdventureWorks2022]
GO
EXEC [AdventureWorks2022].sys.sp_addextendedproperty @name=N'MS_Description', @value=N'AdventureWorks 2016 Sample OLTP Database' 
GO
USE [master]
GO
ALTER DATABASE [AdventureWorks2022] SET  READ_WRITE 
GO
