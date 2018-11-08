from __future__ import division
import numpy.random, matplotlib.pyplot as pyplot, matplotlib.colors
import numpy, matplotlib.cm

USER = "James Fulton"
USER_ID = "njzc77"

def f((x,y)):
        '''Returns value Rosenbrock's Banana Function for co-ordinates given'''
	z = (1-x)**2 + 100 * (y - x**2)**2
	return z

def grad((x,y)):
        '''Returns gradient of the Banana Function for co-ordinates given'''
	dx = 400 * x**3 - 400 * x * y + 2 * x - 2
	dy = 200 *(y - x**2)
	return numpy.array((dx,dy))

def banana_way((x0,y0), d):
        '''Takes a step towards the minumum of the Banana Function'''
	(x1,y1) = numpy.array((x0,y0)) - grad((x0,y0)) * d
	return (x1,y1)


def banana_path(d,start):
        '''Calculates the gradient decent of the Banana function for a given gamma size and start point'''
	if start == 0: # if start not defined random start point is generated
	   x0 = numpy.random.uniform(-0.2,1,) 
	   y0 = numpy.random.uniform(-0.2,1,) 
	else:
	    (x0,y0) = start  
	# make list to store decent path and unput sytart point
	path = [(x0,y0)]
	# calculate decent path and store
	for i in range(10000):
		path.append((banana_way(path[-1],d)))
		(x,y) = path[-1]
		# if path strays outside of the region -0.2< (x and y) < 1 stop due to non-convergence
		if ( x < -0.2 ) or ( x > 1 ) or  ( y < -0.2 ) or ( y > 1 ):
			break
	Path=numpy.asarray(path)
	return Path

# generate decent paths for a few gamma values
gamma1 = banana_path(0.001,(0.2,1))
gamma2 = banana_path(0.002,(0.2,1))
gamma3 = banana_path(0.005,(0.2,1))
gamma4 = banana_path(0.01,(0.2,1))

# GENERATING BANANA BACKGROUND
#limits of data 
x0, x1, y0, y1 = -0.2, 1, -0.2, 1
#generate x,y co-ordinates for banana function evaluation 
N = 300
dx = (x1-x0)/N
dy = (y1-y0)/N
X_AXIS = numpy.arange(x0,x1,dx)
Y_AXIS = numpy.arange(y0,y1,dy)
#generate banana function data for bounds
data = numpy.zeros((len(X_AXIS),len(Y_AXIS)))
for iy in range(len(Y_AXIS)):
	for ix in range(len(X_AXIS)):
		data[(iy,ix)]=f((X_AXIS[ix],Y_AXIS[iy]))

#plot the function and add scale bar
im = pyplot.imshow(data,extent = ( y0,y1, x0,x1,), origin = 'lower', 
cmap=matplotlib.cm.gray, norm = matplotlib.colors.LogNorm(vmin = 0.01, vmax = 200))
pyplot.colorbar(im,orientation = 'vertical')
#plot the grad decent paths
pyplot.plot(gamma4[:,0],gamma4[:,1], label = '0.010', color = 'blue')
pyplot.plot(gamma3[:,0],gamma3[:,1], label = '0.005', color = 'red')
pyplot.plot(gamma2[:,0],gamma2[:,1], label = '0.002', color = 'yellow')
pyplot.plot(gamma1[:,0],gamma1[:,1], label = '0.001', color = 'pink')
pyplot.title('Gradient Decent of Varying Gamma Values') 
pyplot.legend(loc='best', fancybox=True, framealpha=0.1)
pyplot.xlabel('x - no units')
pyplot.ylabel('y - no units')
pyplot.xlim(xmax = x1, xmin = x0)
pyplot.ylim(ymax = y1, ymin = y0)
pyplot.show()
 
# answers
ANSWER1 = ''' As gamma increases from zero, the gradient decent starts out very inefficient at low gamma values just because of the  
small step size. As it is increased the effiency of the method goes up but eventually the step size becomes too great causing our 
approximation of following the gradient exactly to break down , causing some scattering inside the trench due to the curve of the trench.
At large gamma values the step size oversteps the trench completely causing the path to vary to plus and minus infinity'''
(xmin,ymin) = gamma3[-1]
ANSWER2 = 'Minima occurs at %.2f, %.2f' % (xmin,ymin)
