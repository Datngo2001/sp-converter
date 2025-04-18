SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [ProductVendor](
	[ProductID] [int] NOT NULL,
	[BusinessEntityID] [int] NOT NULL,
	[AverageLeadTime] [int] NOT NULL,
	[StandardPrice] [money] NOT NULL,
	[LastReceiptCost] [money] NULL,
	[LastReceiptDate] [datetime] NULL,
	[MinOrderQty] [int] NOT NULL,
	[MaxOrderQty] [int] NOT NULL,
	[OnOrderQty] [int] NULL,
	[UnitMeasureCode] [nchar](3) NOT NULL,
	[ModifiedDate] [datetime] NOT NULL,
 CONSTRAINT [PK_ProductVendor_ProductID_BusinessEntityID] PRIMARY KEY CLUSTERED 
(
	[ProductID] ASC,
	[BusinessEntityID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
CREATE NONCLUSTERED INDEX [IX_ProductVendor_BusinessEntityID] ON [ProductVendor]
(
	[BusinessEntityID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
CREATE NONCLUSTERED INDEX [IX_ProductVendor_UnitMeasureCode] ON [ProductVendor]
(
	[UnitMeasureCode] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [ProductVendor]  WITH CHECK ADD  CONSTRAINT [FK_ProductVendor_Product_ProductID] FOREIGN KEY([ProductID])
REFERENCES [Product] ([ProductID])
GO
ALTER TABLE [ProductVendor] CHECK CONSTRAINT [FK_ProductVendor_Product_ProductID]
GO
ALTER TABLE [ProductVendor]  WITH CHECK ADD  CONSTRAINT [FK_ProductVendor_UnitMeasure_UnitMeasureCode] FOREIGN KEY([UnitMeasureCode])
REFERENCES [UnitMeasure] ([UnitMeasureCode])
GO
ALTER TABLE [ProductVendor] CHECK CONSTRAINT [FK_ProductVendor_UnitMeasure_UnitMeasureCode]
GO
ALTER TABLE [ProductVendor]  WITH CHECK ADD  CONSTRAINT [FK_ProductVendor_Vendor_BusinessEntityID] FOREIGN KEY([BusinessEntityID])
REFERENCES [Vendor] ([BusinessEntityID])
GO
ALTER TABLE [ProductVendor] CHECK CONSTRAINT [FK_ProductVendor_Vendor_BusinessEntityID]
GO
ALTER TABLE [ProductVendor]  WITH CHECK ADD  CONSTRAINT [CK_ProductVendor_AverageLeadTime] CHECK  (([AverageLeadTime]>=(1)))
GO
ALTER TABLE [ProductVendor] CHECK CONSTRAINT [CK_ProductVendor_AverageLeadTime]
GO
ALTER TABLE [ProductVendor]  WITH CHECK ADD  CONSTRAINT [CK_ProductVendor_LastReceiptCost] CHECK  (([LastReceiptCost]>(0.00)))
GO
ALTER TABLE [ProductVendor] CHECK CONSTRAINT [CK_ProductVendor_LastReceiptCost]
GO
ALTER TABLE [ProductVendor]  WITH CHECK ADD  CONSTRAINT [CK_ProductVendor_MaxOrderQty] CHECK  (([MaxOrderQty]>=(1)))
GO
ALTER TABLE [ProductVendor] CHECK CONSTRAINT [CK_ProductVendor_MaxOrderQty]
GO
ALTER TABLE [ProductVendor]  WITH CHECK ADD  CONSTRAINT [CK_ProductVendor_MinOrderQty] CHECK  (([MinOrderQty]>=(1)))
GO
ALTER TABLE [ProductVendor] CHECK CONSTRAINT [CK_ProductVendor_MinOrderQty]
GO
ALTER TABLE [ProductVendor]  WITH CHECK ADD  CONSTRAINT [CK_ProductVendor_OnOrderQty] CHECK  (([OnOrderQty]>=(0)))
GO
ALTER TABLE [ProductVendor] CHECK CONSTRAINT [CK_ProductVendor_OnOrderQty]
GO
ALTER TABLE [ProductVendor]  WITH CHECK ADD  CONSTRAINT [CK_ProductVendor_StandardPrice] CHECK  (([StandardPrice]>(0.00)))
GO
ALTER TABLE [ProductVendor] CHECK CONSTRAINT [CK_ProductVendor_StandardPrice]
GO
