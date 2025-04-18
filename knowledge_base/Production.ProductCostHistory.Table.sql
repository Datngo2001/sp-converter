SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [ProductCostHistory](
	[ProductID] [int] NOT NULL,
	[StartDate] [datetime] NOT NULL,
	[EndDate] [datetime] NULL,
	[StandardCost] [money] NOT NULL,
	[ModifiedDate] [datetime] NOT NULL,
 CONSTRAINT [PK_ProductCostHistory_ProductID_StartDate] PRIMARY KEY CLUSTERED 
(
	[ProductID] ASC,
	[StartDate] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [ProductCostHistory]  WITH CHECK ADD  CONSTRAINT [FK_ProductCostHistory_Product_ProductID] FOREIGN KEY([ProductID])
REFERENCES [Product] ([ProductID])
GO
ALTER TABLE [ProductCostHistory] CHECK CONSTRAINT [FK_ProductCostHistory_Product_ProductID]
GO
ALTER TABLE [ProductCostHistory]  WITH CHECK ADD  CONSTRAINT [CK_ProductCostHistory_EndDate] CHECK  (([EndDate]>=[StartDate] OR [EndDate] IS NULL))
GO
ALTER TABLE [ProductCostHistory] CHECK CONSTRAINT [CK_ProductCostHistory_EndDate]
GO
ALTER TABLE [ProductCostHistory]  WITH CHECK ADD  CONSTRAINT [CK_ProductCostHistory_StandardCost] CHECK  (([StandardCost]>=(0.00)))
GO
ALTER TABLE [ProductCostHistory] CHECK CONSTRAINT [CK_ProductCostHistory_StandardCost]
GO
