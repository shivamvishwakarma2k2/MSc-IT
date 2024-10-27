from pyamaze import maze,agent,COLOR

m = maze(10, 15)
m.CreateMaze(pattern='v', loopPercent=50, theme=COLOR.light)
a = agent(m, filled=True,shape = 'arrow', footprints=True, color='red')
m.tracePath({a:m.path})
m.run()
