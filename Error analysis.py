'''This thingy is meant to be used in order to find the errors on parameters used to model a thing. 
These parameters must already have been optomised to give the lowest Chi squared value.'''

import numpy.random, matplotlib.pyplot as pyplot, numpy, random

# BELOW DEFINE THE SHEAR_RATE (X - AXIS COMPONENT), THE RAW DATA AND THE STANDARD ERROS ON THIS DATA
Shear_Rates = numpy.array([2.652, 3.026, 3.4, 3.774, 5.508, 7.242, 8.976, 10.71, 12.44, 14.18, 15.91, 17.65, 19.38, 21.11])
RawData = numpy.array([10192.3,9662.92,8750,7792.79,6141.98,4882.63,4346.59,3888.89,3538.25,3435.25,3103.63,2803.47,2640.35,2520.13])
StdErrors = numpy.array([158.9852429,141.8597591,140.7730956,131.2316548,90.28264106,77.68927301,50.80111914,46.23083044,38.37375708,37.54038538,31.7193331,44.10285706,25.90513258,22.51724804])



# BELOW INCERT THE CHIMIN VALUE AND THE PARAMETERS VALUES THAT GIVE THIS VALUE
ChiMin = 55.87819968
n0, k0 = 0.328173682, 19480.6714
Temp = 65 # for log keeping

# HERE WE PUT IN THE SETTINGS FOR THE BOTS INCLUDING HOW MANY, TIME, SPEED AND SENSITIVITY
DT, V = 0.1, 0.1
k =  1 # k is the sensitivity of the bots to changing function values. The higher the value the more they react and tumble
NUM = 1000 # this defines how many bots to release to find a Chi+1 value (most are unsuccessful)
Tolerance = 0.1

def model((n,k),SR):
        '''Returns modelled value of the viscosity for a shear rate SR'''
	v = k*((SR)**(n-1))
	return v

def Chi((n,k)):
    '''returns Chi squared value for these n,k co-ordinate'''
    ChiArray =( (model((n,k), Shear_Rates) - RawData)/StdErrors )**2
    return sum(ChiArray)
    
def Chiplus((n,k), ChiMin):
    '''funtion used for targeting chi + 1. This function has it's max - a value of 0 at the ChiMin +1 value.'''
    ChiArray = ( (model((n,k), Shear_Rates) - RawData)/StdErrors )**2
    chiplus = - abs(sum(ChiArray) - (ChiMin + 1))
    return chiplus


def step((start),theta):
        '''Makes a step for the max seeking bot '''
	dx = numpy.cos(theta); dy = 10000*numpy.sin(theta) # here we make sure it moves in the x and y directions to an equal extent. That is where the factor of 10000 comes in
	(x1,y1) = numpy.array(start) + DT * V * numpy.array((dx,dy))
	return (x1,y1)

def path(start,k):
        '''Uses the step function to move the bot around the ChiPlus field searching for a value larger than -0.01 . ie the ChiPlus outcome'''
        #start conditions
        end = numpy.asarray((0,0))
	path = [(start)]
	theta = 2 * numpy.pi * random.random()
	shift = [Chiplus(start, ChiMin)]*10 # defines the bot's memory of values
        for i in numpy.arange(0.1,100,DT):
        	eNew = Chiplus(path[-1], ChiMin) # New chiplus value
        	if eNew > -Tolerance:
        	   end = numpy.asarray(path[-1]) # if the bot finds a max it will stop there and report co-ords
        	   break 
        	   
		shift.append(eNew) # add to the bot memory
		shift = shift[-10:] # keep only the 10 most recent memories
		de = shift[-1] - shift[0] # recent chiplus change    
		t_half = k*(de) # define the tumbling half life
		if t_half < 0.1: 
			t_half = 0.1  # this is needed so that the bot won't continue to tumble on the same spot
		tau = t_half/numpy.log(2)
		P_not_tumble =  numpy.exp( - DT/tau ) # probability of not tumbling 
		if P_not_tumble < random.random(): 
			theta = 2 * numpy.pi * random.random()
			path.append(step(path[-1],theta)) # if it tumbles it will take a step in a new direction
		else:
			path.append(step(path[-1],theta)) # otherwise continue in same direction
		    
        if sum(end) != 0:
	       return end # it returns a value only if the bot found a ChiMin + 1 value 


# GENERATE LIST BOT END POINTS
BotEnd = []
for i in range(NUM):
                xi = numpy.random.uniform(0,1) # here we sactter the bots over the rough area of the ChiMin value
                yi = numpy.random.uniform(25000,40000) 
                starti = (n0,k0) 
                B = path(starti, k)
                if B != None:
		  BotEnd.append( B )  

# TURN THE LIST OF END POINTS INTO AN ARRAY
ParameterUncert = numpy.asarray(BotEnd)

# PLOTTING
pyplot.plot(); pyplot.title('ChiMin + 1 Evaluation', fontsize = 12)
pyplot.plot(ParameterUncert[:,0],ParameterUncert[:,1], marker = '.', linestyle = 'None', color = 'pink') # No line is plotted just a scatter chart
pyplot.plot(n0, k0, marker = 'x', color = 'red') # plot the ChiMin co-ordinate
pyplot.ylabel( 'k' ); pyplot.xlabel('n')
pyplot.show()


print 'Temp =', Temp # for log keeping
#EXTRACT MAXIMUMS AND MINUMUMS OF THE DATA REPRESENTING UPPER AND LOWER BOUNDS OF THE ERROR BARS
n_max,n_min = max(ParameterUncert[:,0]), min(ParameterUncert[:,0])
k_max, k_min = max(ParameterUncert[:,1]), min(ParameterUncert[:,1])



#print 'n_max =', n_max
#print 'n_min =', n_min
#print 'k_max =', k_max
#print 'k_min =', k_min

#EXTRACTING ERROR BAR INFORMATION
n_pos = n_max - n0;      n_neg = n0-n_min
k_pos = k_max - k0;      k_neg = k0 - k_min

print 'n_pos =', n_pos
print 'n_neg =', n_neg
print 'k_pos =', k_pos
print 'k_neg =', k_neg