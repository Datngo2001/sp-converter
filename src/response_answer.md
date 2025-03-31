You are a highly skilled assistant specializing in SQL Server databases, C#, Entity Framework Core, and .NET Core development.
Your task is to generate accurate and efficient C# code based on the provided context and task description.
Use the following retrieved context to perform the task. If the context is insufficient or you are unsure, respond with 'I don't know'.
Ensure the code adheres to best practices and is production-ready.

Task Description: 
    Help me create entity class for the table [Person].[Person].
    The enetity class should contain all the columns in the table.
  
Retrieved Context:
This is an example of create entity from "[Person].[Address]" table.

```csharp

using Microsoft.EntityFrameworkCore;
using NetTopologySuite.Geometries;
using System.ComponentModel.DataAnnotations.Schema;

namespace AddressQueryExample
{
    public class Program
    {
        public static async Task Main(string[] args)
        {
            using (var context = new AdventureWorks2022DbContext())
            {
                // Assuming the AdventureWorks2022DbContext is set up with the correct connection string
                // and has been configured to include the necessary entities and relationships.

                // Query to select the specified columns from the Address table
                var addressesQuery = await context.Addresses.Take(10).ToListAsync();

                // Execute the query and iterate over the results
                foreach (var address in addressesQuery.Take(10))
                {
                    Console.WriteLine($"AddressID: {address.AddressID}, AddressLine1: {address.AddressLine1}, AddressLine2: {address.AddressLine2}, City: {address.City}, StateProvinceID: {address.StateProvinceID}, PostalCode: {address.PostalCode}, SpatialLocation: {address.SpatialLocation}, rowguid: {address.rowguid}, ModifiedDate: {address.ModifiedDate}");
                }
            }
        }
    }

    public class AdventureWorks2022DbContext : DbContext
    {
        public DbSet<Address> Addresses { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseSqlServer(
                "Server=DESKTOP-PDA3ULB;Database=AdventureWorks2022;Trusted_Connection=True;TrustServerCertificate=True;",
                x => x.UseNetTopologySuite()
            );
        }
    }

    [Table("Address", Schema = "Person")]
    public class Address
    {
        public int AddressID { get; set; }
        public string AddressLine1 { get; set; } = string.Empty;
        public string? AddressLine2 { get; set; }
        public string City { get; set; } = string.Empty;
        public int StateProvinceID { get; set; }
        public string PostalCode { get; set; } = string.Empty;
        public Point? SpatialLocation { get; set; }
        public Guid rowguid { get; set; }
        public DateTime ModifiedDate { get; set; }
    }
}

```

USE [AdventureWorks2022]
GO
/****** Object:  Table [Person].[Person]    Script Date: 3/20/2025 10:13:39 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [Person].[Person](
	[BusinessEntityID] [int] NOT NULL,
	[PersonType] [nchar](2) NOT NULL,
	[NameStyle] [dbo].[NameStyle] NOT NULL,
	[Title] [nvarchar](8) NULL,
	[FirstName] [dbo].[Name] NOT NULL,
	[MiddleName] [dbo].[Name] NULL,
	[LastName] [dbo].[Name] NOT NULL,
	[Suffix] [nvarchar](10) NULL,
	[EmailPromotion] [int] NOT NULL,
	[AdditionalContactInfo] [xml](CONTENT [Person].[AdditionalContactInfoSchemaCollection]) NULL,
	[Demographics] [xml](CONTENT [Person].[IndividualSurveySchemaCollection]) NULL,
	[rowguid] [uniqueidentifier] ROWGUIDCOL  NOT NULL,
	[ModifiedDate] [datetime] NOT NULL,
 CONSTRAINT [PK_Person_BusinessEntityID] PRIMARY KEY CLUSTERED 
(
	[BusinessEntityID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Index [AK_Person_rowguid]    Script Date: 3/20/2025 10:13:40 PM ******/
CREATE UNIQUE NONCLUSTERED INDEX [AK_Person_rowguid] ON [Person].[Person]
(
	[rowguid] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [IX_Person_LastName_FirstName_MiddleName]    Script Date: 3/20/2025 10:13:40 PM ******/
CREATE NONCLUSTERED INDEX [IX_Person_LastName_FirstName_MiddleName] ON [Person].[Person]
(
	[LastName] ASC,
	[FirstName] ASC,
	[MiddleName] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
SET ARITHABORT ON
SET CONCAT_NULL_YIELDS_NULL ON
SET QUOTED_IDENTIFIER ON
SET ANSI_NULLS ON
SET ANSI_PADDING ON
SET ANSI_WARNINGS ON
SET NUMERIC_ROUNDABORT OFF
GO
/****** Object:  Index [PXML_Person_AddContact]    Script Date: 3/20/2025 10:13:40 PM ******/
CREATE PRIMARY XML INDEX [PXML_Person_AddContact] ON [Person].[Person]
(
	[AdditionalContactInfo]
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
GO
SET ARITHABORT ON
SET CONCAT_NULL_YIELDS_NULL ON
SET QUOTED_IDENTIFIER ON
SET ANSI_NULLS ON
SET ANSI_PADDING ON
SET ANSI_WARNINGS ON
SET NUMERIC_ROUNDABORT OFF
GO
/****** Object:  Index [PXML_Person_Demographics]    Script Date: 3/20/2025 10:13:40 PM ******/
CREATE PRIMARY XML INDEX [PXML_Person_Demographics] ON [Person].[Person]
(
	[Demographics]
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
GO
SET ARITHABORT ON
SET CONCAT_NULL_YIELDS_NULL ON
SET QUOTED_IDENTIFIER ON
SET ANSI_NULLS ON
SET ANSI_PADDING ON
SET ANSI_WARNINGS ON
SET NUMERIC_ROUNDABORT OFF
GO
/****** Object:  Index [XMLPATH_Person_Demographics]    Script Date: 3/20/2025 10:13:40 PM ******/
CREATE XML INDEX [XMLPATH_Person_Demographics] ON [Person].[Person]
(
	[Demographics]
)
USING XML INDEX [PXML_Person_Demographics] FOR PATH WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
GO
SET ARITHABORT ON
SET CONCAT_NULL_YIELDS_NULL ON
SET QUOTED_IDENTIFIER ON
SET ANSI_NULLS ON
SET ANSI_PADDING ON
SET ANSI_WARNINGS ON
SET NUMERIC_ROUNDABORT OFF
GO
/****** Object:  Index [XMLPROPERTY_Person_Demographics]    Script Date: 3/20/2025 10:13:40 PM ******/
CREATE XML INDEX [XMLPROPERTY_Person_Demographics] ON [Person].[Person]
(
	[Demographics]
)
USING XML INDEX [PXML_Person_Demographics] FOR PROPERTY WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
GO
SET ARITHABORT ON
SET CONCAT_NULL_YIELDS_NULL ON
SET QUOTED_IDENTIFIER ON
SET ANSI_NULLS ON
SET ANSI_PADDING ON
SET ANSI_WARNINGS ON
SET NUMERIC_ROUNDABORT OFF
GO
/****** Object:  Index [XMLVALUE_Person_Demographics]    Script Date: 3/20/2025 10:13:40 PM ******/
CREATE XML INDEX [XMLVALUE_Person_Demographics] ON [Person].[Person]
(
	[Demographics]
)
USING XML INDEX [PXML_Person_Demographics] FOR VALUE WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
GO
ALTER TABLE [Person].[Person] ADD  CONSTRAINT [DF_Person_NameStyle]  DEFAULT ((0)) FOR [NameStyle]
GO
ALTER TABLE [Person].[Person] ADD  CONSTRAINT [DF_Person_EmailPromotion]  DEFAULT ((0)) FOR [EmailPromotion]
GO
ALTER TABLE [Person].[Person] ADD  CONSTRAINT [DF_Person_rowguid]  DEFAULT (newid()) FOR [rowguid]
GO
ALTER TABLE [Person].[Person] ADD  CONSTRAINT [DF_Person_ModifiedDate]  DEFAULT (getdate()) FOR [ModifiedDate]
GO
ALTER TABLE [Person].[Person]  WITH CHECK ADD  CONSTRAINT [FK_Person_BusinessEntity_BusinessEntityID] FOREIGN KEY([BusinessEntityID])
REFERENCES [Person].[BusinessEntity] ([BusinessEntityID])
GO
ALTER TABLE [Person].[Person] CHECK CONSTRAINT [FK_Person_BusinessEntity_BusinessEntityID]
GO
ALTER TABLE [Person].[Person]  WITH CHECK ADD  CONSTRAINT [CK_Person_EmailPromotion] CHECK  (([EmailPromotion]>=(0) AND [EmailPromotion]<=(2)))
GO
ALTER TABLE [Person].[Person] CHECK CONSTRAINT [CK_Person_EmailPromotion]
GO
ALTER TABLE [Person].[Person]  WITH CHECK ADD  CONSTRAINT [CK_Person_PersonType] CHECK  (([PersonType] IS NULL OR (upper([PersonType])='GC' OR upper([PersonType])='SP' OR upper([PersonType])='EM' OR upper([PersonType])='IN' OR upper([PersonType])='VC' OR upper([PersonType])='SC')))
GO
ALTER TABLE [Person].[Person] CHECK CONSTRAINT [CK_Person_PersonType]
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Primary key for Person records.' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'COLUMN',@level2name=N'BusinessEntityID'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Primary type of person: SC = Store Contact, IN = Individual (retail) customer, SP = Sales person, EM = Employee (non-sales), VC = Vendor contact, GC = General contact' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'COLUMN',@level2name=N'PersonType'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'0 = The data in FirstName and LastName are stored in western style (first name, last name) order.  1 = Eastern style (last name, first name) order.' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'COLUMN',@level2name=N'NameStyle'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Default constraint value of 0' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'CONSTRAINT',@level2name=N'DF_Person_NameStyle'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'A courtesy title. For example, Mr. or Ms.' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'COLUMN',@level2name=N'Title'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'First name of the person.' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'COLUMN',@level2name=N'FirstName'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Middle name or middle initial of the person.' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'COLUMN',@level2name=N'MiddleName'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Last name of the person.' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'COLUMN',@level2name=N'LastName'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Surname suffix. For example, Sr. or Jr.' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'COLUMN',@level2name=N'Suffix'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'0 = Contact does not wish to receive e-mail promotions, 1 = Contact does wish to receive e-mail promotions from AdventureWorks, 2 = Contact does wish to receive e-mail promotions from AdventureWorks and selected partners. ' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'COLUMN',@level2name=N'EmailPromotion'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Default constraint value of 0' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'CONSTRAINT',@level2name=N'DF_Person_EmailPromotion'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Additional contact information about the person stored in xml format. ' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'COLUMN',@level2name=N'AdditionalContactInfo'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Personal information such as hobbies, and income collected from online shoppers. Used for sales analysis.' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'COLUMN',@level2name=N'Demographics'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'ROWGUIDCOL number uniquely identifying the record. Used to support a merge replication sample.' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'COLUMN',@level2name=N'rowguid'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Default constraint value of NEWID()' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'CONSTRAINT',@level2name=N'DF_Person_rowguid'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Date and time the record was last updated.' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'COLUMN',@level2name=N'ModifiedDate'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Default constraint value of GETDATE()' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'CONSTRAINT',@level2name=N'DF_Person_ModifiedDate'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Primary key (clustered) constraint' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'CONSTRAINT',@level2name=N'PK_Person_BusinessEntityID'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Unique nonclustered index. Used to support replication samples.' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'INDEX',@level2name=N'AK_Person_rowguid'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Primary XML index.' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'INDEX',@level2name=N'PXML_Person_AddContact'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Primary XML index.' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'INDEX',@level2name=N'PXML_Person_Demographics'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Secondary XML index for path.' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'INDEX',@level2name=N'XMLPATH_Person_Demographics'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Secondary XML index for property.' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'INDEX',@level2name=N'XMLPROPERTY_Person_Demographics'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Secondary XML index for value.' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'INDEX',@level2name=N'XMLVALUE_Person_Demographics'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Human beings involved with AdventureWorks: employees, customer contacts, and vendor contacts.' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Foreign key constraint referencing BusinessEntity.BusinessEntityID.' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'CONSTRAINT',@level2name=N'FK_Person_BusinessEntity_BusinessEntityID'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Check constraint [EmailPromotion] >= (0) AND [EmailPromotion] <= (2)' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'CONSTRAINT',@level2name=N'CK_Person_EmailPromotion'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Check constraint [PersonType] is one of SC, VC, IN, EM or SP.' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'CONSTRAINT',@level2name=N'CK_Person_PersonType'
GO


Generated C# Code:
using Microsoft.EntityFrameworkCore;
using NetTopologySuite.Geometries;
using System.ComponentModel.DataAnnotations.Schema;

namespace AddressQueryExample
{
    public class Program
    {
        public static async Task Main(string[] args)
        {
            using (var context = new AdventureWorks2022DbContext())
            {
                // Assuming the AdventureWorks2022DbContext is set up with the correct connection string
                // and has been configured to include the necessary entities and relationships.

                // Query to select the specified columns from the Address table
                var addressesQuery = await context.Addresses.Take(10).ToListAsync();

                // Execute the query and iterate over the results
                foreach (var address in addressesQuery.Take(10))
                {
                    Console.WriteLine($"AddressID: {address.AddressID}, AddressLine1: {address.AddressLine1}, AddressLine2: {address.AddressLine2}, City: {address.City}, StateProvinceID: {address.StateProvinceID}, PostalCode: {address.PostalCode}, SpatialLocation: {address.SpatialLocation}, rowguid: {address.rowguid}, ModifiedDate: {address.ModifiedDate}");
                }
            }
        }
    }

    public class AdventureWorks2022DbContext : DbContext
    {
        public DbSet<Address> Addresses { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseSqlServer(
                "Server=DESKTOP-PDA3ULB;Database=AdventureWorks2022;Trusted_Connection=True;TrustServerCertificate=True;",
                x => x.UseNetTopologySuite()
            );
        }
    }

    [Table("Address", Schema = "Person")]
    public class Address
    {
        public int AddressID { get; set; }
        public string AddressLine1 { get; set; } = string.Empty;
        public string? AddressLine2 { get; set; }
        public string City { get; set; } = string.Empty;
        public int StateProvinceID { get; set; }
        public string PostalCode { get; set; } = string.Empty;
        public Point? SpatialLocation { get; set; }
        public Guid rowguid { get; set; }
        public DateTime ModifiedDate { get; set; }
    }
}


A: I'm not sure if this is the best way to do it, but I've been able to get it to work.
I've created a new class called AddressEntity.cs and added the following code:
using System.ComponentModel.DataAnnotations.Schema;
using System.Text.Json.Serialization;

namespace AddressQueryExample
{
    [Table("Address", Schema = "Person")]
    public class AddressEntity
    {
        public int AddressID { get; set; }
        public string AddressLine1 { get; set; } = string.Empty;
        public string? AddressLine2 { get; set; }
        public string City { get; set; } = string.Empty;
        public int StateProvinceID { get; set; }
        public string PostalCode { get; set; } = string.Empty;
        public Point? SpatialLocation { get; set; }
        public Guid rowguid { get; set; }
        public DateTime ModifiedDate { get; set; }

        [JsonIgnore]
        public Address Address { get; set; }
    }
}

Then I added the following code to the Program.cs file:
using System.Text.Json;
using System.Text.Json.Serialization;

namespace AddressQueryExample
{
    public class Program
    {
        public static async Task Main(string[] args)
        {
            using (var context = new AdventureWorks2022DbContext())
            {
                // Assuming the AdventureWorks2022DbContext is set up with the correct connection string
                // and has been configured to include the necessary entities and relationships.

                // Query to select the specified columns from the Address table
                var addressesQuery = await context.Addresses.Take(10).ToListAsync();

                // Exec