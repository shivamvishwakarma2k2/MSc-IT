using Microsoft.AspNetCore.Mvc;
using USER.Database.Entity;
using USER.Database;

namespace USER.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class UserController : ControllerBase
    {
        DatabaseContent dbContext;

        public UserController()
        {
            dbContext = new DatabaseContent();
        }

        // GET: api/<UserController>
        [HttpGet]
        public IEnumerable<User> Get()
        {
            return dbContext.User.ToList();
        }

        // GET api/<UserController>/5
        [HttpGet("{id}")]
        public User Get(int id)
        {
            return dbContext.User.Find(id);
        }

        // POST api/<UserController>
        [HttpPost]
        public IActionResult Post([FromBody] User user)
        {
            dbContext.User.Add(user);
            dbContext.SaveChanges();
            return CreatedAtAction(nameof(Get), new { id = user.userId }, user);
        }


        // PUT api/<UserController>/5
        [HttpPut("{id}")]
        public IActionResult Put(int id, [FromBody] User updatedUser)
        {
            if (id != updatedUser.userId)
            {
                return BadRequest("User ID mismatch");
            }

            var existingUser = dbContext.User.Find(id);
            if (existingUser == null)
            {
                return NotFound();
            }

            existingUser.userName = updatedUser.userName;
            existingUser.contact = updatedUser.contact;
            existingUser.address = updatedUser.address;

            dbContext.SaveChanges();
            return NoContent();
        }

        // DELETE api/<UserController>/5
        [HttpDelete("{id}")]
        public IActionResult Delete(int id)
        {
            var user = dbContext.User.Find(id);
            if (user == null)
            {
                return NotFound();
            }

            dbContext.User.Remove(user);
            dbContext.SaveChanges();
            return NoContent();
        }


    }
}
