using Microsoft.AspNetCore.Mvc;
using USER.Database;
using USER.Database.Entity;

// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace USER.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class UserController : ControllerBase
    {

        DatabaseContext dbContext;

        public UserController()
        {
            dbContext = new DatabaseContext();
        }


        // GET: api/<UserController>
        [HttpGet]
        public IEnumerable<UserEntity> Get()
        {
            return dbContext.User.ToList();
        }


        // GET api/<UserController>/5
        [HttpGet("{id}")]
        public UserEntity Get(int id)
        {
            return dbContext.User.Find(id);
        }


        // POST api/<UserController>
        [HttpPost]
        public void Post([FromBody] string value)
        {
        }

        // PUT api/<UserController>/5
        [HttpPut("{id}")]
        public void Put(int id, [FromBody] string value)
        {
        }

        // DELETE api/<UserController>/5
        [HttpDelete("{id}")]
        public void Delete(int id)
        {
        }
    }
}
