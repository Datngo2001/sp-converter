SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [Product](
	[ProductID] [int] IDENTITY(1,1) NOT NULL,
	[Name] [dbo].[Name] NOT NULL,
	[ProductNumber] [nvarchar](25) NOT NULL,
	[MakeFlag] [dbo].[Flag] NOT NULL,
	[FinishedGoodsFlag] [dbo].[Flag] NOT NULL,
	[Color] [nvarchar](15) NULL,
	[SafetyStockLevel] [smallint] NOT NULL,
	[ReorderPoint] [smallint] NOT NULL,
	[StandardCost] [money] NOT NULL,
	[ListPrice] [money] NOT NULL,
	[Size] [nvarchar](5) NULL,
	[SizeUnitMeasureCode] [nchar](3) NULL,
	[WeightUnitMeasureCode] [nchar](3) NULL,
	[Weight] [decimal](8, 2) NULL,
	[DaysToManufacture] [int] NOT NULL,
	[ProductLine] [nchar](2) NULL,
	[Class] [nchar](2) NULL,
	[Style] [nchar](2) NULL,
	[ProductSubcategoryID] [int] NULL,
	[ProductModelID] [int] NULL,
	[SellStartDate] [datetime] NOT NULL,
	[SellEndDate] [datetime] NULL,
	[DiscontinuedDate] [datetime] NULL,
	[rowguid] [uniqueidentifier] ROWGUIDCOL  NOT NULL,
	[ModifiedDate] [datetime] NOT NULL,
 CONSTRAINT [PK_Product_ProductID] PRIMARY KEY CLUSTERED 
(
	[ProductID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
CREATE UNIQUE NONCLUSTERED INDEX [AK_Product_Name] ON [Product]
(
	[Name] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
CREATE UNIQUE NONCLUSTERED INDEX [AK_Product_ProductNumber] ON [Product]
(
	[ProductNumber] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
CREATE UNIQUE NONCLUSTERED INDEX [AK_Product_rowguid] ON [Product]
(
	[rowguid] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [Product]  WITH CHECK ADD  CONSTRAINT [FK_Product_ProductModel_ProductModelID] FOREIGN KEY([ProductModelID])
REFERENCES [ProductModel] ([ProductModelID])
GO
ALTER TABLE [Product] CHECK CONSTRAINT [FK_Product_ProductModel_ProductModelID]
GO
ALTER TABLE [Product]  WITH CHECK ADD  CONSTRAINT [FK_Product_ProductSubcategory_ProductSubcategoryID] FOREIGN KEY([ProductSubcategoryID])
REFERENCES [ProductSubcategory] ([ProductSubcategoryID])
GO
ALTER TABLE [Product] CHECK CONSTRAINT [FK_Product_ProductSubcategory_ProductSubcategoryID]
GO
ALTER TABLE [Product]  WITH CHECK ADD  CONSTRAINT [FK_Product_UnitMeasure_SizeUnitMeasureCode] FOREIGN KEY([SizeUnitMeasureCode])
REFERENCES [UnitMeasure] ([UnitMeasureCode])
GO
ALTER TABLE [Product] CHECK CONSTRAINT [FK_Product_UnitMeasure_SizeUnitMeasureCode]
GO
ALTER TABLE [Product]  WITH CHECK ADD  CONSTRAINT [FK_Product_UnitMeasure_WeightUnitMeasureCode] FOREIGN KEY([WeightUnitMeasureCode])
REFERENCES [UnitMeasure] ([UnitMeasureCode])
GO
ALTER TABLE [Product] CHECK CONSTRAINT [FK_Product_UnitMeasure_WeightUnitMeasureCode]
GO
ALTER TABLE [Product]  WITH CHECK ADD  CONSTRAINT [CK_Product_Class] CHECK  ((upper([Class])='H' OR upper([Class])='M' OR upper([Class])='L' OR [Class] IS NULL))
GO
ALTER TABLE [Product] CHECK CONSTRAINT [CK_Product_Class]
GO
ALTER TABLE [Product]  WITH CHECK ADD  CONSTRAINT [CK_Product_DaysToManufacture] CHECK  (([DaysToManufacture]>=(0)))
GO
ALTER TABLE [Product] CHECK CONSTRAINT [CK_Product_DaysToManufacture]
GO
ALTER TABLE [Product]  WITH CHECK ADD  CONSTRAINT [CK_Product_ListPrice] CHECK  (([ListPrice]>=(0.00)))
GO
ALTER TABLE [Product] CHECK CONSTRAINT [CK_Product_ListPrice]
GO
ALTER TABLE [Product]  WITH CHECK ADD  CONSTRAINT [CK_Product_ProductLine] CHECK  ((upper([ProductLine])='R' OR upper([ProductLine])='M' OR upper([ProductLine])='T' OR upper([ProductLine])='S' OR [ProductLine] IS NULL))
GO
ALTER TABLE [Product] CHECK CONSTRAINT [CK_Product_ProductLine]
GO
ALTER TABLE [Product]  WITH CHECK ADD  CONSTRAINT [CK_Product_ReorderPoint] CHECK  (([ReorderPoint]>(0)))
GO
ALTER TABLE [Product] CHECK CONSTRAINT [CK_Product_ReorderPoint]
GO
ALTER TABLE [Product]  WITH CHECK ADD  CONSTRAINT [CK_Product_SafetyStockLevel] CHECK  (([SafetyStockLevel]>(0)))
GO
ALTER TABLE [Product] CHECK CONSTRAINT [CK_Product_SafetyStockLevel]
GO
ALTER TABLE [Product]  WITH CHECK ADD  CONSTRAINT [CK_Product_SellEndDate] CHECK  (([SellEndDate]>=[SellStartDate] OR [SellEndDate] IS NULL))
GO
ALTER TABLE [Product] CHECK CONSTRAINT [CK_Product_SellEndDate]
GO
ALTER TABLE [Product]  WITH CHECK ADD  CONSTRAINT [CK_Product_StandardCost] CHECK  (([StandardCost]>=(0.00)))
GO
ALTER TABLE [Product] CHECK CONSTRAINT [CK_Product_StandardCost]
GO
ALTER TABLE [Product]  WITH CHECK ADD  CONSTRAINT [CK_Product_Style] CHECK  ((upper([Style])='U' OR upper([Style])='M' OR upper([Style])='W' OR [Style] IS NULL))
GO
ALTER TABLE [Product] CHECK CONSTRAINT [CK_Product_Style]
GO
ALTER TABLE [Product]  WITH CHECK ADD  CONSTRAINT [CK_Product_Weight] CHECK  (([Weight]>(0.00)))
GO
ALTER TABLE [Product] CHECK CONSTRAINT [CK_Product_Weight]
GO
