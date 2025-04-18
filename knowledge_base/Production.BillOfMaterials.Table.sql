SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [BillOfMaterials](
	[BillOfMaterialsID] [int] IDENTITY(1,1) NOT NULL,
	[ProductAssemblyID] [int] NULL,
	[ComponentID] [int] NOT NULL,
	[StartDate] [datetime] NOT NULL,
	[EndDate] [datetime] NULL,
	[UnitMeasureCode] [nchar](3) NOT NULL,
	[BOMLevel] [smallint] NOT NULL,
	[PerAssemblyQty] [decimal](8, 2) NOT NULL,
	[ModifiedDate] [datetime] NOT NULL,
 CONSTRAINT [PK_BillOfMaterials_BillOfMaterialsID] PRIMARY KEY NONCLUSTERED 
(
	[BillOfMaterialsID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
CREATE UNIQUE CLUSTERED INDEX [AK_BillOfMaterials_ProductAssemblyID_ComponentID_StartDate] ON [BillOfMaterials]
(
	[ProductAssemblyID] ASC,
	[ComponentID] ASC,
	[StartDate] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
CREATE NONCLUSTERED INDEX [IX_BillOfMaterials_UnitMeasureCode] ON [BillOfMaterials]
(
	[UnitMeasureCode] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [BillOfMaterials]  WITH CHECK ADD  CONSTRAINT [FK_BillOfMaterials_Product_ComponentID] FOREIGN KEY([ComponentID])
REFERENCES [Product] ([ProductID])
GO
ALTER TABLE [BillOfMaterials] CHECK CONSTRAINT [FK_BillOfMaterials_Product_ComponentID]
GO
ALTER TABLE [BillOfMaterials]  WITH CHECK ADD  CONSTRAINT [FK_BillOfMaterials_Product_ProductAssemblyID] FOREIGN KEY([ProductAssemblyID])
REFERENCES [Product] ([ProductID])
GO
ALTER TABLE [BillOfMaterials] CHECK CONSTRAINT [FK_BillOfMaterials_Product_ProductAssemblyID]
GO
ALTER TABLE [BillOfMaterials]  WITH CHECK ADD  CONSTRAINT [FK_BillOfMaterials_UnitMeasure_UnitMeasureCode] FOREIGN KEY([UnitMeasureCode])
REFERENCES [UnitMeasure] ([UnitMeasureCode])
GO
ALTER TABLE [BillOfMaterials] CHECK CONSTRAINT [FK_BillOfMaterials_UnitMeasure_UnitMeasureCode]
GO
ALTER TABLE [BillOfMaterials]  WITH CHECK ADD  CONSTRAINT [CK_BillOfMaterials_BOMLevel] CHECK  (([ProductAssemblyID] IS NULL AND [BOMLevel]=(0) AND [PerAssemblyQty]=(1.00) OR [ProductAssemblyID] IS NOT NULL AND [BOMLevel]>=(1)))
GO
ALTER TABLE [BillOfMaterials] CHECK CONSTRAINT [CK_BillOfMaterials_BOMLevel]
GO
ALTER TABLE [BillOfMaterials]  WITH CHECK ADD  CONSTRAINT [CK_BillOfMaterials_EndDate] CHECK  (([EndDate]>[StartDate] OR [EndDate] IS NULL))
GO
ALTER TABLE [BillOfMaterials] CHECK CONSTRAINT [CK_BillOfMaterials_EndDate]
GO
ALTER TABLE [BillOfMaterials]  WITH CHECK ADD  CONSTRAINT [CK_BillOfMaterials_PerAssemblyQty] CHECK  (([PerAssemblyQty]>=(1.00)))
GO
ALTER TABLE [BillOfMaterials] CHECK CONSTRAINT [CK_BillOfMaterials_PerAssemblyQty]
GO
ALTER TABLE [BillOfMaterials]  WITH CHECK ADD  CONSTRAINT [CK_BillOfMaterials_ProductAssemblyID] CHECK  (([ProductAssemblyID]<>[ComponentID]))
GO
ALTER TABLE [BillOfMaterials] CHECK CONSTRAINT [CK_BillOfMaterials_ProductAssemblyID]
GO
