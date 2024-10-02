using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Logging;

namespace console_practical
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            var config = new ConfigurationBuilder().AddCommandLine(args).Build();

            var host = new WebHostBuilder().UseKestrel().UseStartup<Startup>().UseConfiguration(config).Build();
            host.Run();
        }
    }

    class Startup
    {
        public Startup(IHostingEnvironment env)
        {

        }

        public void configure(IHostingEnvironment env, IApplicationBuilder app, ILoggerFactory logger)
        {
            app.Run(
                async context => await context
                .Response
                .WriteAsync("Hello weolcome to this console application")
            );

        }
    }
}