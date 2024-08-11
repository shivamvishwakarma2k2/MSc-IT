using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace Glossary.Controllers
{
    public class GlossaryController : ControllerBase
    {
        //// GET: GlossaryController
        //public ActionResult Index()
        //{
        //    return View();
        //}

        //// GET: GlossaryController/Details/5
        //public ActionResult Details(int id)
        //{
        //    return View();
        //}

        //// GET: GlossaryController/Create
        //public ActionResult Create()
        //{
        //    return View();
        //}

        //// POST: GlossaryController/Create
        //[HttpPost]
        //[ValidateAntiForgeryToken]
        //public ActionResult Create(IFormCollection collection)
        //{
        //    try
        //    {
        //        return RedirectToAction(nameof(Index));
        //    }
        //    catch
        //    {
        //        return View();
        //    }
        //}

        //// GET: GlossaryController/Edit/5
        //public ActionResult Edit(int id)
        //{
        //    return View();
        //}

        //// POST: GlossaryController/Edit/5
        //[HttpPost]
        //[ValidateAntiForgeryToken]
        //public ActionResult Edit(int id, IFormCollection collection)
        //{
        //    try
        //    {
        //        return RedirectToAction(nameof(Index));
        //    }
        //    catch
        //    {
        //        return View();
        //    }
        //}

        //// GET: GlossaryController/Delete/5
        //public ActionResult Delete(int id)
        //{
        //    return View();
        //}

        //// POST: GlossaryController/Delete/5
        //[HttpPost]
        //[ValidateAntiForgeryToken]
        //public ActionResult Delete(int id, IFormCollection collection)
        //{
        //    try
        //    {
        //        return RedirectToAction(nameof(Index));
        //    }
        //    catch
        //    {
        //        return View();
        //    }
        //}





        // Glossary data, initialized with some sample GlossaryItems.
        public static List<GlossaryItem> Glossary = new List<GlossaryItem>
        {
            new GlossaryItem { Term = "HTML", Definition = "Hypertext Markup Language" },
            new GlossaryItem { Term = "MVC", Definition = "Model View Controller" },
            new GlossaryItem { Term = "OpenID", Definition = "An open standard for authentication" }
        };


        // GET: api/<GlossaryController>

        [HttpGet]
        public ActionResult<List<GlossaryItem>> Get()
        {
            // Return the entire glossary when a GET request is made
            return Ok(Glossary);
        }

        // GET api/<GlossaryController>/5
        [HttpGet("{term}")]
        public ActionResult<GlossaryItem> Get(string term)
        {
            // Find and return a glossary item by its term (case-insensitive) or return a 404 Not Found response if not found.
            var glossaryItem = Glossary.FirstOrDefault(item => item.Term.Equals(term, StringComparison.InvariantCultureIgnoreCase));
            if (glossaryItem == null)
            {
                return NotFound();
            }
            else
            {
                return Ok(glossaryItem);
            }
        }

        // POST api/<GlossaryController>
        [HttpPost]
        public ActionResult Post(GlossaryItem glossaryItem)
        {
            // Check if a glossary item with the same term already exists. If so, return a conflict response. Otherwise, add the new glossary item.
            var existingGlossaryItem = Glossary.FirstOrDefault(item => item.Term.Equals(glossaryItem.Term, StringComparison.InvariantCultureIgnoreCase));
            if (existingGlossaryItem != null)
            {
                return Conflict("Can't create the term because it already exists.");
            }
            else
            {
                Glossary.Add(glossaryItem);
                var resourceUrl = Path.Combine(Request.Path.ToString(), Uri.EscapeDataString(glossaryItem.Term));
                return Created(resourceUrl, glossaryItem);
            }
        }

        // PUT api/<GlossaryController>/5
        [HttpPut]
        public ActionResult Put(GlossaryItem glossaryItem)
        {
            // Update the definition of an existing glossary item if it exists, or return a bad request response if it doesn't exist.
            var existingGlossaryItem = Glossary.FirstOrDefault(item => item.Term.Equals(glossaryItem.Term, StringComparison.InvariantCultureIgnoreCase));
            if (existingGlossaryItem == null)
            {
                return BadRequest("Can't update a non-existing term");
            }
            else
            {
                existingGlossaryItem.Definition = glossaryItem.Definition;
                return Ok();
            }
        }

        // DELETE api/<GlossaryController>/5
        [HttpDelete("{term}")]
        public ActionResult Delete(string term)
        {
            // Delete a glossary item by its term if it exists, or return a 404 Not Found response if it doesn't exist.
            var glossaryItem = Glossary.FirstOrDefault(item => item.Term.Equals(term, StringComparison.InvariantCultureIgnoreCase));
            if (glossaryItem == null)
            {
                return NotFound();
            }
            else
            {
                Glossary.Remove(glossaryItem);
                return NoContent();
            }
        }
    }
}
