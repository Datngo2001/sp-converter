You are a highly skilled assistant specializing in SQL Server databases, C#, Entity Framework Core, and .NET Core development.
Your task is to generate accurate and efficient C# code based on the provided context and task description.
Use the following retrieved context to perform the task. If the context is insufficient or you are unsure, respond with 'I don't know'.
Ensure the code adheres to best practices and is production-ready.

Task Description: 
    Help me create entity class for the table [Person].[Person]
  
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

REFERENCES [Person].[Person] ([BusinessEntityID])
GO
ALTER TABLE [Person].[BusinessEntityContact] CHECK CONSTRAINT [FK_BusinessEntityContact_Person_PersonID]
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Primary key. Foreign key to BusinessEntity.BusinessEntityID.' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'BusinessEntityContact', @level2type=N'COLUMN',@level2name=N'BusinessEntityID'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Primary key. Foreign key to Person.BusinessEntityID.' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'BusinessEntityContact', @level2type=N'COLUMN',@level2name=N'PersonID'
GO

GO
ALTER TABLE [Person].[Person] CHECK CONSTRAINT [CK_Person_EmailPromotion]
GO
ALTER TABLE [Person].[Person]  WITH CHECK ADD  CONSTRAINT [CK_Person_PersonType] CHECK  (([PersonType] IS NULL OR (upper([PersonType])='GC' OR upper([PersonType])='SP' OR upper([PersonType])='EM' OR upper([PersonType])='IN' OR upper([PersonType])='VC' OR upper([PersonType])='SC')))
GO
ALTER TABLE [Person].[Person] CHECK CONSTRAINT [CK_Person_PersonType]
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Primary key for Person records.' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'Person', @level2type=N'COLUMN',@level2name=N'BusinessEntityID'
GO

GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Foreign key constraint referencing Person.BusinessEntityID.' , @level0type=N'SCHEMA',@level0name=N'Person', @level1type=N'TABLE',@level1name=N'BusinessEntityContact', @level2type=N'CONSTRAINT',@level2name=N'FK_BusinessEntityContact_Person_PersonID'
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

            }
        }
    }

    public class AdventureWorks2022DbContext : DbContext
    {
        public DbSet<Address> Addresses { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseSqlServer("Server=(localdb)\\mssqllocaldb;Database=AdventureWorks2022;Trusted_Connection=True;");
        }
    }

    public class Address
    {
        public int AddressID { get; set; }
        public string AddressLine1 { get; set; }
        public string AddressLine2 { get; set; }
        public string City { get; set; }
        public string StateProvinceID { get; set; }
        public string PostalCode { get; set; }
        public string SpatialLocation { get; set; }
        public Geometry Location { get; set; }
    }
}

```






























































































































































































































































































































































































































































































































































































































































































