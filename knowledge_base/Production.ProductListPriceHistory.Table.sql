SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [ProductListPriceHistory](
	[ProductID] [int] NOT NULL,
	[StartDate] [datetime] NOT NULL,
	[EndDate] [datetime] NULL,
	[ListPrice] [money] NOT NULL,
	[ModifiedDate] [datetime] NOT NULL,
 CONSTRAINT [PK_ProductListPriceHistory_ProductID_StartDate] PRIMARY KEY CLUSTERED 
(
	[ProductID] ASC,
	[StartDate] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [ProductListPriceHistory]  WITH CHECK ADD  CONSTRAINT [FK_ProductListPriceHistory_Product_ProductID] FOREIGN KEY([ProductID])
REFERENCES [Product] ([ProductID])
GO
ALTER TABLE [ProductListPriceHistory] CHECK CONSTRAINT [FK_ProductListPriceHistory_Product_ProductID]
GO
ALTER TABLE [ProductListPriceHistory]  WITH CHECK ADD  CONSTRAINT [CK_ProductListPriceHistory_EndDate] CHECK  (([EndDate]>=[StartDate] OR [EndDate] IS NULL))
GO
ALTER TABLE [ProductListPriceHistory] CHECK CONSTRAINT [CK_ProductListPriceHistory_EndDate]
GO
ALTER TABLE [ProductListPriceHistory]  WITH CHECK ADD  CONSTRAINT [CK_ProductListPriceHistory_ListPrice] CHECK  (([ListPrice]>(0.00)))
GO
ALTER TABLE [ProductListPriceHistory] CHECK CONSTRAINT [CK_ProductListPriceHistory_ListPrice]
GO
