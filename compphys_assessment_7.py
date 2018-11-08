# -*- coding: utf-8 -*-
from __future__ import division
import numpy.random, matplotlib.pyplot as pyplot, matplotlib.colors
import numpy, matplotlib.cm, random
USER = "James Fulton"
USER_ID = "njzc77"

dt = 0.1 # time step used in seconds
v = 2 # speed of the bacteria in microns/s


def f((x,y)):
        '''Returns value of Sugar Density for co-ordinates given'''
	z = 5000-( x**2 + y**2 )
	return z

def step((start),theta):
        '''Makes a step for the bacteria'''
	dx = numpy.cos(theta)
	dy = numpy.sin(theta)
	(x1,y1) = numpy.array(start) + dt * v * numpy.array((dx,dy))
	return (x1,y1)

def path(start,k):
        '''Uses the step function to model the motion of a sugar seeking bacteria in the sugar field f'''
        #start conditions
	f0 = f((start))
	shift = [f0,f0,f0,f0,f0,f0,f0,f0,f0,f0]
	theta0 = 2 * numpy.pi * random.random()
	theta = theta0
	path = [(start)]
	
	for i in numpy.arange(0.1,100,dt):
        
		eNew = f(path[-1]) # New sugar level
		shift.append(eNew) # add to the python list
		shift = shift[-10:] # keep only the 10 most recent entries
		de = shift[-1] - shift[0] # [-1] is the newest 
                       
		t_half = 1 + k*(de)
		if t_half < 0.1:
			t_half = 0.1
		tau = t_half/numpy.log(2)
		P_not_tumble =  numpy.exp( - dt/tau )
		if P_not_tumble < random.random():
			theta = 2 * numpy.pi * random.random()
			path.append(path[-1])
		else:
			path.append(step(path[-1],theta))
	Path = numpy.asarray(path)
	return Path  
    
# GENERATE 20 BACTERIA PATHS
Bacteria = []
for i in range(20):
		Bacteria.append( path((20,40), 0.2) )
# DEFINE TIMEBASE CORRESPONDING TO PATH POSITION
timebase = numpy.arange(0,100,dt)

# GENERATING SUGAR FIELD
# bounds of data 
x0, x1, y0, y1 = -30, 40, -20,50

#generate x,y co-ordinates for sweetness evaluation 
N = 300; dx = (x1-x0)/N; dy = (y1-y0)/N
X_AXIS = numpy.arange(x0,x1,dx)
Y_AXIS = numpy.arange(y0,y1,dy)

#generate sugar function data for bounds
data = numpy.zeros((len(X_AXIS),len(Y_AXIS)))
for iy in range(len(Y_AXIS)):
	for ix in range(len(X_AXIS)):
		data[(iy,ix)]=f((X_AXIS[ix],Y_AXIS[iy]))
		
#create MSD - from start position
displacement_squared = ['value']*20
for i in range(20):
    displacement_squared[i] =( Bacteria[i] - numpy.array((20,40)) )**2
Sum_SD_start = numpy.zeros(1000)
for i in range(1000):
    for j in range(20):
        Sum_SD_start[i] += sum(displacement_squared[j][i])
    MSD_start = Sum_SD_start / 20
    
#create MSD - from orgin position
from_sugar_squared = ['value']*20
for i in range(20):
    from_sugar_squared[i] =Bacteria[i]**2
Sum_SD_sugar = numpy.zeros(1000)
for i in range(1000):
    for j in range(20):
        Sum_SD_sugar[i] += sum(from_sugar_squared[j][i])
    MSD_sugar = Sum_SD_sugar / 20

# PLOTTING

# plot sugar field and bacteria tracks in top left
pyplot.subplot(221); pyplot.title('Bacteria Tracks', fontsize = 12)
im = pyplot.imshow(data,extent = (x0,x1, y0,y1, ), origin = 'lower', 
cmap=matplotlib.cm.gray, norm = matplotlib.colors.Normalize(vmin=1600, vmax=5000))

for i in range(20):
	pyplot.plot(Bacteria[i][:,0],Bacteria[i][:,1])
pyplot.ylabel( 'y - microns' ); pyplot.xlabel('x - microns')
pyplot.xticks((-20,0,20,40))
pyplot.xlim(xmax = x1, xmin = x0); pyplot.ylim(ymax = y1, ymin = y0)

#plot sugar field, simplified bacteria tracks and colour scale in top right
pyplot.subplot(222); pyplot.title('Simplified Bacteria Tracks', fontsize = 12)
im = pyplot.imshow(data,extent = (x0,x1, y0,y1, ), origin = 'lower', 
cmap=matplotlib.cm.gray, norm = matplotlib.colors.Normalize(vmin=1600, vmax=5000))
for i in range(20):
	(x0,y0) = Bacteria[i][0]; (xF, yF) = Bacteria[i][-1]
	pyplot.plot((x0,xF), (y0,yF), marker = 'o')
pyplot.ylabel( 'y - microns' ); pyplot.xlabel('x - microns')
pyplot.xticks((-20,0,20,40))
pyplot.colorbar(im,orientation = 'vertical', label = 'Relative Sugar Density')
#pyplot.colorbar(ticks=[1800,2200,2600,3000,3400,3800,4200])
pyplot.subplots_adjust(hspace=0.4)

# plot MSD - from start postion in bottom graph
pyplot.subplot(212)
pyplot.plot(timebase,MSD_start, label = 'From start position')

# plot MSD - from origin in bottom graph
pyplot.plot(timebase,MSD_sugar, label = 'From sugar peak' )
pyplot.ylabel('MSD - microns squared ')
pyplot.xlabel('Time - seconds')
pyplot.legend(loc='best', fancybox=True, framealpha=0)
pyplot.title('Mean Square Distance From Position', fontsize = 12)
pyplot.suptitle("Modelling Chemotaxis of Feeding Bacteria ", fontsize=18)



pyplot.show()