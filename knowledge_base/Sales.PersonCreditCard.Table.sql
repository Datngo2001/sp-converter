SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [PersonCreditCard](
	[BusinessEntityID] [int] NOT NULL,
	[CreditCardID] [int] NOT NULL,
	[ModifiedDate] [datetime] NOT NULL,
 CONSTRAINT [PK_PersonCreditCard_BusinessEntityID_CreditCardID] PRIMARY KEY CLUSTERED 
(
	[BusinessEntityID] ASC,
	[CreditCardID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [PersonCreditCard]  WITH CHECK ADD  CONSTRAINT [FK_PersonCreditCard_CreditCard_CreditCardID] FOREIGN KEY([CreditCardID])
REFERENCES [CreditCard] ([CreditCardID])
GO
ALTER TABLE [PersonCreditCard] CHECK CONSTRAINT [FK_PersonCreditCard_CreditCard_CreditCardID]
GO
ALTER TABLE [PersonCreditCard]  WITH CHECK ADD  CONSTRAINT [FK_PersonCreditCard_Person_BusinessEntityID] FOREIGN KEY([BusinessEntityID])
REFERENCES [Person] ([BusinessEntityID])
GO
ALTER TABLE [PersonCreditCard] CHECK CONSTRAINT [FK_PersonCreditCard_Person_BusinessEntityID]
GO
