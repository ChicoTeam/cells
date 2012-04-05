import random, cells
import math

class AgentMind():
    def __init__(self, junk):
        self.x = 1
        pass

    def act(self, view, msg):
        me = view.get_me()
        my_pos = (mx,my) = me.get_pos()
      
        for agent in view.get_agents():
		      #print "Agent!" 
				pass

        if (me.energy < 50) :
            return cells.Action(cells.ACT_EAT)

        return cells.Action(cells.ACT_MOVE,(mx + 1 + random.randrange(-1,1),                                              my + 1+ random.randrange(-1,1))                               )
