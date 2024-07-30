using Microsoft.AspNetCore.Mvc;
using PracticalMVC.Models;
using System.Diagnostics;

namespace PracticalMVC.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;

        public HomeController(ILogger<HomeController> logger)
        {
            _logger = logger;
        }

        public IActionResult Index()
        {
            var model = new StockQuote{stockName = "Reliance", stockPrice = 5499.45F, stockDesc = "Reliance one of the India's Leading Organsation in alomost every scetor" };
            return View(model);
        }

        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
