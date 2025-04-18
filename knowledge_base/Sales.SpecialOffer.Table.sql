SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [SpecialOffer](
	[SpecialOfferID] [int] IDENTITY(1,1) NOT NULL,
	[Description] [nvarchar](255) NOT NULL,
	[DiscountPct] [smallmoney] NOT NULL,
	[Type] [nvarchar](50) NOT NULL,
	[Category] [nvarchar](50) NOT NULL,
	[StartDate] [datetime] NOT NULL,
	[EndDate] [datetime] NOT NULL,
	[MinQty] [int] NOT NULL,
	[MaxQty] [int] NULL,
	[rowguid] [uniqueidentifier] ROWGUIDCOL  NOT NULL,
	[ModifiedDate] [datetime] NOT NULL,
 CONSTRAINT [PK_SpecialOffer_SpecialOfferID] PRIMARY KEY CLUSTERED 
(
	[SpecialOfferID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
CREATE UNIQUE NONCLUSTERED INDEX [AK_SpecialOffer_rowguid] ON [SpecialOffer]
(
	[rowguid] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [SpecialOffer]  WITH CHECK ADD  CONSTRAINT [CK_SpecialOffer_DiscountPct] CHECK  (([DiscountPct]>=(0.00)))
GO
ALTER TABLE [SpecialOffer] CHECK CONSTRAINT [CK_SpecialOffer_DiscountPct]
GO
ALTER TABLE [SpecialOffer]  WITH CHECK ADD  CONSTRAINT [CK_SpecialOffer_EndDate] CHECK  (([EndDate]>=[StartDate]))
GO
ALTER TABLE [SpecialOffer] CHECK CONSTRAINT [CK_SpecialOffer_EndDate]
GO
ALTER TABLE [SpecialOffer]  WITH CHECK ADD  CONSTRAINT [CK_SpecialOffer_MaxQty] CHECK  (([MaxQty]>=(0)))
GO
ALTER TABLE [SpecialOffer] CHECK CONSTRAINT [CK_SpecialOffer_MaxQty]
GO
ALTER TABLE [SpecialOffer]  WITH CHECK ADD  CONSTRAINT [CK_SpecialOffer_MinQty] CHECK  (([MinQty]>=(0)))
GO
ALTER TABLE [SpecialOffer] CHECK CONSTRAINT [CK_SpecialOffer_MinQty]
GO
