from pyamaze import maze,agent,COLOR

m=maze(7,10)
m.CreateMaze( pattern='v', loopPercent=40, theme=COLOR.dark)
a=agent(m,filled=True,shape = 'arrow', footprints=True, color='red')
m.tracePath({a:m.path})
m.run()
