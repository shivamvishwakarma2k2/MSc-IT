using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.IO;
using System.Reflection.Metadata;

// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace Glossary_6620.Controller
{
    [Route("api/[controller]")]
    [ApiController]
    public class GlossaryController : ControllerBase
    {
        private static List<GlossaryItem> GlossaryItem = new List<GlossaryItem>
        {
            new GlossaryItem
            {
                Term = "HTML",
                Definition = "Hypertext Markup Language"
            },

            new GlossaryItem
            {
                Term = "MVC",
                Definition = "Model View Controller"
            },
            new GlossaryItem
            {
                Term = "OpenID",
                Definition = "An open standard for authentication"
            }
        };

        // GET: api/<GlossaryController>
        [HttpGet]
        public ActionResult<List<GlossaryItem>> Get()
        {
            return Ok(GlossaryItem);

        }
        [HttpGet("{term}")]

        //[Route("{term}")]
        public ActionResult<GlossaryItem> Get(string term)
        {
            var glossaryItem = GlossaryItem.Find(item => item.Term.Equals(term, StringComparison.InvariantCultureIgnoreCase));
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
            var existingGlossaryItem = GlossaryItem.Find(item => item.Term.Equals(glossaryItem.Term, StringComparison.InvariantCultureIgnoreCase));
            if (existingGlossaryItem != null)
            {
                return Conflict("Cannot create the term because it already exists.");
            }
            else
            {
                GlossaryItem.Add(glossaryItem);
                var resourceUrl = Path.Combine(Request.Path.ToString(), Uri.EscapeUriString(glossaryItem.Term));
                return Created(resourceUrl, glossaryItem);
            }
        }


        // PUT api/<GlossaryController>/5
        [HttpPut("{id}")]
        public ActionResult Put(GlossaryItem glossaryItem)
        {
            var existingGlossaryItem = GlossaryItem.Find(item => item.Term.Equals(glossaryItem.Term, StringComparison.InvariantCultureIgnoreCase));
            if (existingGlossaryItem == null)
            {
                return BadRequest("Cannot update a non existing term.");
            }
            else
            {
                existingGlossaryItem.Definition = glossaryItem.Definition;
                return Ok();
            }
        }

        // DELETE api/<GlossaryController>/5
        [HttpDelete("{term}")]
        //[Route("{term}")]
        public ActionResult Delete(string term)
        {
            var glossaryItem = GlossaryItem.Find(item => item.Term.Equals(term, StringComparison.InvariantCultureIgnoreCase));
            if (glossaryItem == null)
            {
                return NotFound();
            }
            else
            {
                GlossaryItem.Remove(glossaryItem);
                return NoContent();
            }
        }
    }
}
