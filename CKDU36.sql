CREATE TABLE "STATDATA" (
     "YEAR-Q" nvarchar(10),
     "Country" nvarchar(20),
     "I10GDP" decimal (10,5),
     "I05HICP_T" decimal (10,5),
     "I05HICP_R" decimal (10,5),
     "I15HPI" decimal (10,5),
     "UNEMPLOYMENT" decimal (10,5),
     "I10LABOUR" decimal (10,5),
     "KEY1" nvarchar(20)
)
CREATE TABLE "I05HICP_T" (
     "I05HICP_T" decimal (10,5),
     "KEY1" nvarchar(20)
)
CREATE TABLE "I05HICP_R" (
     "I05HICP_R" decimal (10,5),
     "KEY1" nvarchar(20)
)
CREATE TABLE "I15HPI" (
     "I15HPI" decimal (10,5),
     "KEY1" nvarchar(20)
)
CREATE TABLE "UNEMPLOYMENT" (
     "UNEMPLOYMENT" decimal (10,5),
     "KEY1" nvarchar(20)
)
CREATE TABLE "I10LABOUR" (
     "I10LABOUR" decimal (10,5),
     "KEY1" nvarchar(20)
)
CREATE TABLE "POPULATION" (
     "COUNTRY" nvarchar(20),
     "POPULATION" decimal (20,7),
     "KEY1" nvarchar(20),
     "YEAR" integer
)