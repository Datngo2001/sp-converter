SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [ProductInventory](
	[ProductID] [int] NOT NULL,
	[LocationID] [smallint] NOT NULL,
	[Shelf] [nvarchar](10) NOT NULL,
	[Bin] [tinyint] NOT NULL,
	[Quantity] [smallint] NOT NULL,
	[rowguid] [uniqueidentifier] ROWGUIDCOL  NOT NULL,
	[ModifiedDate] [datetime] NOT NULL,
 CONSTRAINT [PK_ProductInventory_ProductID_LocationID] PRIMARY KEY CLUSTERED 
(
	[ProductID] ASC,
	[LocationID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [ProductInventory]  WITH CHECK ADD  CONSTRAINT [FK_ProductInventory_Location_LocationID] FOREIGN KEY([LocationID])
REFERENCES [Location] ([LocationID])
GO
ALTER TABLE [ProductInventory] CHECK CONSTRAINT [FK_ProductInventory_Location_LocationID]
GO
ALTER TABLE [ProductInventory]  WITH CHECK ADD  CONSTRAINT [FK_ProductInventory_Product_ProductID] FOREIGN KEY([ProductID])
REFERENCES [Product] ([ProductID])
GO
ALTER TABLE [ProductInventory] CHECK CONSTRAINT [FK_ProductInventory_Product_ProductID]
GO
ALTER TABLE [ProductInventory]  WITH CHECK ADD  CONSTRAINT [CK_ProductInventory_Bin] CHECK  (([Bin]>=(0) AND [Bin]<=(100)))
GO
ALTER TABLE [ProductInventory] CHECK CONSTRAINT [CK_ProductInventory_Bin]
GO
ALTER TABLE [ProductInventory]  WITH CHECK ADD  CONSTRAINT [CK_ProductInventory_Shelf] CHECK  (([Shelf] like '[A-Za-z]' OR [Shelf]='N/A'))
GO
ALTER TABLE [ProductInventory] CHECK CONSTRAINT [CK_ProductInventory_Shelf]
GO
