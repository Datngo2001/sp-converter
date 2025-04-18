SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [BusinessEntityAddress](
	[BusinessEntityID] [int] NOT NULL,
	[AddressID] [int] NOT NULL,
	[AddressTypeID] [int] NOT NULL,
	[rowguid] [uniqueidentifier] ROWGUIDCOL  NOT NULL,
	[ModifiedDate] [datetime] NOT NULL,
 CONSTRAINT [PK_BusinessEntityAddress_BusinessEntityID_AddressID_AddressTypeID] PRIMARY KEY CLUSTERED 
(
	[BusinessEntityID] ASC,
	[AddressID] ASC,
	[AddressTypeID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
CREATE UNIQUE NONCLUSTERED INDEX [AK_BusinessEntityAddress_rowguid] ON [BusinessEntityAddress]
(
	[rowguid] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
CREATE NONCLUSTERED INDEX [IX_BusinessEntityAddress_AddressID] ON [BusinessEntityAddress]
(
	[AddressID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
CREATE NONCLUSTERED INDEX [IX_BusinessEntityAddress_AddressTypeID] ON [BusinessEntityAddress]
(
	[AddressTypeID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [BusinessEntityAddress]  WITH CHECK ADD  CONSTRAINT [FK_BusinessEntityAddress_Address_AddressID] FOREIGN KEY([AddressID])
REFERENCES [Address] ([AddressID])
GO
ALTER TABLE [BusinessEntityAddress] CHECK CONSTRAINT [FK_BusinessEntityAddress_Address_AddressID]
GO
ALTER TABLE [BusinessEntityAddress]  WITH CHECK ADD  CONSTRAINT [FK_BusinessEntityAddress_AddressType_AddressTypeID] FOREIGN KEY([AddressTypeID])
REFERENCES [AddressType] ([AddressTypeID])
GO
ALTER TABLE [BusinessEntityAddress] CHECK CONSTRAINT [FK_BusinessEntityAddress_AddressType_AddressTypeID]
GO
ALTER TABLE [BusinessEntityAddress]  WITH CHECK ADD  CONSTRAINT [FK_BusinessEntityAddress_BusinessEntity_BusinessEntityID] FOREIGN KEY([BusinessEntityID])
REFERENCES [BusinessEntity] ([BusinessEntityID])
GO
ALTER TABLE [BusinessEntityAddress] CHECK CONSTRAINT [FK_BusinessEntityAddress_BusinessEntity_BusinessEntityID]
GO
