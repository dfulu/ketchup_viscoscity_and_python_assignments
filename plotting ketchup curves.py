import numpy, matplotlib.pyplot as pyplot, matplotlib.colors

#use regular intervals of shear rate and Temp
dSr = 1 # set
dT = 1 # set
#set extents maxc and min temp and shear rates
SrMin = ; SrMax = 
TMin = ; TMax = 
grid = numpy.zeros( ((TMax-TMin)/dT + 1, (SrMax - SrMin)/dSr + 1), dtype = numpy.float)

#enter data collected for temp
grid[0,:] = 
grid[1,:] =
grid[2,:] =
grid[3,:] =
grid[4,:] =
grid[5,:] =
grid[6,:] =
grid[7,:] =
grid[8,:] =
grid[9,:] =
grid[10,:] =
grid[11,:] =
grid[12,:] =
grid[13,:] =
grid[14,:] =
grid[15,:] =
grid[16,:] =



#plot the function and add scale bar
pyplot.figure()

im = pyplot.imshow(grid,extent = ( SrMin,SrMax, TMin,TMax), origin = 'lower', 
cmap=matplotlib.cm.gray, norm = matplotlib.colors.Normalize(vmin = numpy.amin(grid) , vmax = numpy.amax(grid)))
pyplot.colorbar(im,orientation = 'vertical')

pyplot.title('The Non-Newtonain Proprties of Ketchup') 
pyplot.xlabel('Shear Rate')
pyplot.ylabel('Temperature')
#pyplot.xlim(xmax = x1, xmin = x0)
#pyplot.ylim(ymax = y1, ymin = y0)
pyplot.show()

