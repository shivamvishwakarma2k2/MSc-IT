from pyamaze import maze, agent

my_maze = maze(10, 10)
my_maze.CreateMaze(loopPercent=30)
my_agent = agent(my_maze, shape='arrow', footprints=True)
my_maze.tracePath({my_agent: my_maze.path})
my_maze.run()