from __future__ import division
import numpy.random, matplotlib.pyplot as pyplot, matplotlib.colors
import numpy, matplotlib.cm ###############################################check theses at end
USER = "James Fulton"
USER_ID = "njzc77"

def NR(z0):
    '''uses the Newton-Raphson Method to take a step towards the minimum'''
    z1 = 1/4 * ( 1/z0**3 + 3 * z0 )
    return z1

def root(z0, maxit):
    '''find the closest root and conergence speed'''
    z = z0 #make reference value
    for i in range(maxit):
        z = NR(z)
        if abs(z)>abs(z0):
            z1 = 0
            I = maxit
        if (z**4-1) == 0:
            z1 = z
            I = i
            break
    return z1, I

# GENERATING ARGAND CO-ORDS
x0, x1, y0, y1 = -3, 3, -3, 3 # bounds of data 
# generate N squared x,y co-ordinates for sweetness evaluation 
N = 100; dx = (x1-x0)/N; dy = (y1-y0)/N
REAL = numpy.arange(x0,x1,dx); IMAG = 1j * numpy.arange(y0,y1,dy)
IMAG.shape = (N, 1)
# generate argand co-ords
COMPLEX_COORDS = numpy.zeros((N,N))
COMPLEX_COORDS = COMPLEX_COORDS + REAL + IMAG

def roots(N, (x0,y0), (x1,y1)): 
    
    # argand co-ordinates 
    dx = (x1-x0)/N; dy = (y1-y0)/N
    real = numpy.arange(x0,x1,dx); imag = 1j * numpy.arange(y0,y1,dy)
    imag.shape = (N, 1)
    # generate argand co-ords
    zs = numpy.zeros((N,N))
    zs = zs + real + imag
    
    roots = numpy.zeros((N, N, 2))
    maxit = 100
    
    for m in range(N):
        for n in range(N):
            rootmn, roots[m,n,1] = root(zs[m,n],maxit)
            if rootmn == 0: 
                roots[m,n,0] = 0
            if rootmn == 1: 
                roots[m,n,0] = 1
            if rootmn == -1j: 
                roots[m,n,0] = 2
            if rootmn == -1: 
                roots[m,n,0] = 3
            if rootmn == 1j: 
                roots[m,n,0] = 4
    return roots

N = 1000
fractallarge = roots(N, (-3,-3), (3,3))
fractalzoom = roots(N, (-1,-1), (1,1))

#plot large root fractal
pyplot.subplot(221); pyplot.title('Convergent Root', fontsize = 12)
im = pyplot.imshow(fractallarge[:,:,0],extent = (-3,3, -3,3), origin = 'lower', 
cmap=matplotlib.cm.gray, norm = matplotlib.colors.Normalize(vmin=0, vmax=4)) 

# plot zoom root fractal
pyplot.subplot(222); pyplot.title('Convergence Speed', fontsize = 12)
im = pyplot.imshow(fractalzoom[:,:,0],extent = (-1,1, -1,1), origin = 'lower', 
cmap=matplotlib.cm.gray, norm = matplotlib.colors.Normalize(vmin = 0, vmax = 4)) 
cbar = pyplot.colorbar(im,orientation = 'vertical', label = 'Root', ticks=[0,1, 2, 3, 4]) 
cbar.ax.set_yticklabels(['None', '1', '-i', '-1', 'i'])# vertically oriented colorbar



# plot large convergence fractal
pyplot.subplot(223); pyplot.title('Convergence Speed', fontsize = 12)
im = pyplot.imshow(fractallarge[:,:,1],extent = (-3,3, -3,3), origin = 'lower', 
cmap=matplotlib.cm.gray, norm = matplotlib.colors.Normalize(vmin = 0, vmax = 20)) 

# plot large convergence fractal
pyplot.subplot(224); pyplot.title('Convergence Speed', fontsize = 12)
im = pyplot.imshow(fractalzoom[:,:,1],extent = (-1,1, -1,1), origin = 'lower', 
cmap=matplotlib.cm.gray, norm = matplotlib.colors.Normalize(vmin = 0, vmax = 20)) 
cbar = pyplot.colorbar(im,orientation = 'vertical', label = 'Required Steps') 

pyplot.show()
        

