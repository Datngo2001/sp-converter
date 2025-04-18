SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [ProductDocument](
	[ProductID] [int] NOT NULL,
	[DocumentNode] [hierarchyid] NOT NULL,
	[ModifiedDate] [datetime] NOT NULL,
 CONSTRAINT [PK_ProductDocument_ProductID_DocumentNode] PRIMARY KEY CLUSTERED 
(
	[ProductID] ASC,
	[DocumentNode] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [ProductDocument]  WITH CHECK ADD  CONSTRAINT [FK_ProductDocument_Document_DocumentNode] FOREIGN KEY([DocumentNode])
REFERENCES [Document] ([DocumentNode])
GO
ALTER TABLE [ProductDocument] CHECK CONSTRAINT [FK_ProductDocument_Document_DocumentNode]
GO
ALTER TABLE [ProductDocument]  WITH CHECK ADD  CONSTRAINT [FK_ProductDocument_Product_ProductID] FOREIGN KEY([ProductID])
REFERENCES [Product] ([ProductID])
GO
ALTER TABLE [ProductDocument] CHECK CONSTRAINT [FK_ProductDocument_Product_ProductID]
GO
