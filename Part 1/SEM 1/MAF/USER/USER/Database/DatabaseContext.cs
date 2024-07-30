using Microsoft.EntityFrameworkCore;
using USER.Database.Entity;

namespace USER.Database
{
    public class DatabaseContent : DbContext
    {
        public DbSet<User>? User { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseSqlServer(@"Data Source=(localdb)\MSSQLLocalDB;Initial Catalog=User_Database;Integrated Security=True;Connect Timeout=30;Encrypt=False;Trust Server Certificate=False;Application Intent=ReadWrite;Multi Subnet Failover=False");

        }
    }

}
