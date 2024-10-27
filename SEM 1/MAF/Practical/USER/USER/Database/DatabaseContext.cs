using Microsoft.EntityFrameworkCore;
using USER.Database.Entity;

namespace USER.Database
{
    public class DatabaseContext : DbContext
    {
        public DbSet<UserEntity>? User { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseSqlServer(@"Data Source = (localdb)\MSSQLLocalDB;Initial Catalog = Database; Integrated Security = True; Connect Timeout = 30; Encrypt=False;Trust Server Certificate=False;Application Intent = ReadWrite; Multi Subnet Failover=False");
        }



          }
}
