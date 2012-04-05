import random, cells
import math

class AgentMind():
    def __init__(self, junk):
        pass

    def act(self, view, msg):
        '''Vars'''
        me = view.get_me()
        my_pos = (mx,my) = me.get_pos()
      
        for agent in view.get_agents():
		      #print "Agent!" 
				pass

        '''EAT'''
        if (me.energy < 50) :
            print "My health is: " + str(me.energy) + " So I am Eating"
            return cells.Action(cells.ACT_EAT)
		
        '''SPAWN	
        #if 0 == random.randrange(0,2) and me.energy > 200:
            print "Spawn"
            return cells.Action(cells.ACT_SPAWN,(mx+1, my+1, self))
        '''

        '''MOVE'''
        print "I am at X,Y: " + str(me.x) + ", " + str(me.y)
        return cells.Action(cells.ACT_MOVE,(mx + 1 + random.randrange(-1,1),                                              my + 1+ random.randrange(-1,1))                               )
