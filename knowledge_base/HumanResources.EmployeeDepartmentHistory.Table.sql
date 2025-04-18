SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [EmployeeDepartmentHistory](
	[BusinessEntityID] [int] NOT NULL,
	[DepartmentID] [smallint] NOT NULL,
	[ShiftID] [tinyint] NOT NULL,
	[StartDate] [date] NOT NULL,
	[EndDate] [date] NULL,
	[ModifiedDate] [datetime] NOT NULL,
 CONSTRAINT [PK_EmployeeDepartmentHistory_BusinessEntityID_StartDate_DepartmentID] PRIMARY KEY CLUSTERED 
(
	[BusinessEntityID] ASC,
	[StartDate] ASC,
	[DepartmentID] ASC,
	[ShiftID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
CREATE NONCLUSTERED INDEX [IX_EmployeeDepartmentHistory_DepartmentID] ON [EmployeeDepartmentHistory]
(
	[DepartmentID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
CREATE NONCLUSTERED INDEX [IX_EmployeeDepartmentHistory_ShiftID] ON [EmployeeDepartmentHistory]
(
	[ShiftID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [EmployeeDepartmentHistory]  WITH CHECK ADD  CONSTRAINT [FK_EmployeeDepartmentHistory_Department_DepartmentID] FOREIGN KEY([DepartmentID])
REFERENCES [Department] ([DepartmentID])
GO
ALTER TABLE [EmployeeDepartmentHistory] CHECK CONSTRAINT [FK_EmployeeDepartmentHistory_Department_DepartmentID]
GO
ALTER TABLE [EmployeeDepartmentHistory]  WITH CHECK ADD  CONSTRAINT [FK_EmployeeDepartmentHistory_Employee_BusinessEntityID] FOREIGN KEY([BusinessEntityID])
REFERENCES [Employee] ([BusinessEntityID])
GO
ALTER TABLE [EmployeeDepartmentHistory] CHECK CONSTRAINT [FK_EmployeeDepartmentHistory_Employee_BusinessEntityID]
GO
ALTER TABLE [EmployeeDepartmentHistory]  WITH CHECK ADD  CONSTRAINT [FK_EmployeeDepartmentHistory_Shift_ShiftID] FOREIGN KEY([ShiftID])
REFERENCES [Shift] ([ShiftID])
GO
ALTER TABLE [EmployeeDepartmentHistory] CHECK CONSTRAINT [FK_EmployeeDepartmentHistory_Shift_ShiftID]
GO
ALTER TABLE [EmployeeDepartmentHistory]  WITH CHECK ADD  CONSTRAINT [CK_EmployeeDepartmentHistory_EndDate] CHECK  (([EndDate]>=[StartDate] OR [EndDate] IS NULL))
GO
ALTER TABLE [EmployeeDepartmentHistory] CHECK CONSTRAINT [CK_EmployeeDepartmentHistory_EndDate]
GO
