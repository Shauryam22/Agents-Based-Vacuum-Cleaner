import random
class environment:
    def __init__(self):
        #self.states = ['D','C']
        self.grid1 = [['D','D','#','D'], #state grid
                      ['D','D','D','D'],
                      ['#','#','D','D'],
                      ['D','D','D','#']]
        self.grid2 = [[0, 1, 2, 3],            # position grid
                      [4, 5, 6, 7],
                      [8, 9, 10, 11],
                      [12, 13, 14, 15]]
        self.current_state = self.grid1[0][0]   #Initialising state
        self.current_state1 = self.grid2[0][0]  #Corres posiitons
        self.perf_meas = 0

    def get_states(self):
        return self.current_state
    def get_neighbour(self):
        lk = []                   # binding the chosen state to the chosen position in position grid for eg 'D' initial is [0] or[0,0] in pos grid
        print('current_state: ',self.current_state1)
        for i in range(len(self.grid2)):
            for j in range(len(self.grid2)):
                if self.grid2[i][j] == self.current_state1:
                    lk.append(i)
                    lk.append(j)
        print('Present pos: ',lk)
        l = lk[0] 
        k = lk[1]
        set1 = []  #with D,C,# states
        set2 = []  # with 1,2,3..... representative states
        self.grid1[l][k] = 'C' # if action='action' then present state should be 'C' after this action
        
        # if (0,0)---> neighbours: +1 and -1 in one of the coord at a time :eg (0,1),(1,0) but (-1,0),(0,-1) not allowed
        # or for 3x3 matrix , if curr_pos=(3,3) then (2,3),(3,2) but (4,3),(3,4) not allowed
        # so we use pos grid such that +1 doesnt go beyond len of matrix, and -1 does not make index negative.


        if l+1<= (len(self.grid1)-1):      
            set1.append(self.grid1[l+1][k])
        if k+1<=(len(self.grid1)-1):
            set1.append(self.grid1[l][k+1])
        if l-1>=0:
            set1.append(self.grid1[l-1][k])
        if k-1>=0:
            set1.append(self.grid1[l][k-1])
    
        if l+1<= (len(self.grid2)-1):
            set2.append(self.grid2[l+1][k])
        if k+1<=(len(self.grid2)-1):
            set2.append(self.grid2[l][k+1])
        if l-1>=0:
            set2.append(self.grid2[l-1][k])
        if k-1>=0:
            set2.append(self.grid2[l][k-1])
        
        # set1 and set2 contains all the possible neighbours to the curent state.
        # now removing blocked states
        a_set = set1
        b_set = ['#']
        set1 = [i for i in a_set if i not in b_set]
        c_set = [] # removing indexes from pos grid also
        for i in range(len(self.grid2)):
            for j in range(len(self.grid2)):
                if self.grid1[i][j] == '#':
                    c_set.append(self.grid2[i][j])
        set2 = [i for i in set2 if i not in c_set] # note it contains 1,2,3,..... instead of indexes of the state
        print('Next Available states: ',set1)
        print('Next avail positions: ',set2)
        ind = []  # getting indexes of all neighbours using pos grid, which will directly tell us the corres states of neighbours.
        for k in range(len(set2)):
            for i in range(len(self.grid2)):
                for j in range(len(self.grid2)):
                    if self.grid2[i][j] == set2[k]:
                        ind.append([i,j])
        # ind is like [[0,0],[1,0],[0,1]]
        # now we want if one of the neighbour is 'D' just jump on it to clean
        # so we use ind to get where is 'D'
        for i in range(len(ind)):
            j,k = ind[i]
            if self.grid1[j][k] =='D':
                self.current_state1 = [j,k]
            else:
                self.current_state1 = random.choice(ind) # otherwise psoiton radnomly chosen
        m,n = self.current_state1
        return m,n
    def perform_action(self,action):
        if action=='C':
            m,n = self.get_neighbour()                     # getting the each index
            self.current_state = self.grid1[m][n]           # getting the state, which now becomes new curr_state
            self.current_state1 = self.grid2[m][n]
            print('The next chosen state: ',self.current_state)
            print('The next chosen position: ',self.current_state1)
            if self.current_state=='C':
                self.perf_meas-=5
            else:
                self.perf_meas+=10
            self.perf_meas-=1
            print('Grid',self.grid1)
        elif action == 'move':
            m,n = self.get_neighbour()
            self.current_state = self.grid1[m][n]
            self.current_state1 = self.grid2[m][n]
            print('The next chosen state: ',self.current_state)
            print('The next chosen position: ',self.current_state1)
            print('Grid: ',self.grid1)
            if self.current_state=='C':
                self.perf_meas-=5
            else:
                self.perf_meas+=10
                
            self.perf_meas-=1
        print('Performace Measure: ',self.perf_meas)
    
            
# Self reflex model

class Simple_reflex:
    def act(self,percept):
        if percept=='D':
            return 'C'
        #elif percept =='#':
            #return 'move'
        if percept =='C':
            return 'move'
class Model_based:
    def __init__(self):
        self.model = 'C'
    def act(self,percept):
        self.model = percept
        if self.model =='D':
            return "C"
        elif self.model =='#':
            return 'move'
        return 'move'

class Goal_based_agent:
    def __init__(self,goal='C'):
        self.goal = goal
    def act(self,percept):
        if percept == '#':
            return 'move'
        elif percept != self.goal:
            return 'C'
        return 'move'
    

class utility_based_agent:
    def utility(self,state):
        if state =='C':
            return 1
        elif state=='#':
            return 0
        elif state=='D':
            return -1
        
    def act(self,percept):
        if self.utility(percept)<0:
            return 'C'
        elif self.utility(percept)==0:
            return 'move'
        return 'move'
    
class Learning_agent:
    def __init__(self):
        self.knowledge = {}
    def act(self,percept):
        if percept in self.knowledge:
            #self.knowledge[percept]
            return self.knowledge[percept] 
        if percept == 'D':
            action = 'C'        # clean dirty cells
        elif percept == '#':
            action = 'move'     # walls → move
        else:  # percept == 'C' (already clean)
            action = 'move'

        # Store this experience in knowledge
        self.knowledge[percept] = action
        return action
def simulate(agent,step=10):   # can put higher step size, but iterations will automatically stop once all clear. 
    env = environment()
    for step in range(step):
        percept = env.get_states()
        action = agent.act(percept)
        env.perform_action(action)
        if any(env.grid1[i][j]== 'D' for i in range(len(env.grid1)) for j in range(len(env.grid1))):
            
            print(f"Step {step+1}: Percept = {percept},"f"Action = {action},"f"New state = {env.get_states()}")
        else:
            print('ALL CLEAN')
            break
print('----------------------Simple-Reflex---------------------------')
simulate(Simple_reflex())
print()
print()
print('-----------------------Model-Based-----------------------------')
simulate(Model_based())
print()
print()
print('------------------------Goal-Based---------------------------')
simulate(Goal_based_agent())
print()
print()
print('------------------------Utility-based-----------------------')
simulate(utility_based_agent())
print()
print()
print('------------------------Learning-based-----------------------')
simulate(Learning_agent())
print()
print()



