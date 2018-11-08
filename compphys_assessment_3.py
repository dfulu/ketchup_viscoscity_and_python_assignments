from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

USER = "James Fulton"
USER_ID = "njzc77"

#set decay parameters 
T_HALF = 20.8 # half-life in hours
TAU = T_HALF/numpy.log(2) # avaerge lifetime of an isotope in hours

def f(n):
	'''Computes the instantaneous decay rate for a sample of n atoms of radioactive substance'''
	L = 1 / TAU # define the decay constant
	return - L * n
	
def analytic(N0, timebase):
    '''Computes the analytic solution to the number of remaining atoms with time'''
    L = 1 / TAU 
    Nt = numpy.zeros( len(timebase), dtype = numpy.float32 ) # prepare array to hold values of N, the number of atoms with time
    for z in range( len(timebase) ): # fill array
        Nt[z] = N0 * numpy.e** ( -L * timebase[z] )
    return Nt
	
def solve_euler(N0, t1, n_panels):
	'''using the Euler's Method, a set of values is returned thats approximates the number of undecayed atoms left after time t, in hours'''
	dt = t1 / n_panels # define the panel width
	Nt = numpy.zeros(n_panels, dtype = numpy.float32) # create array of values of N, the number of atoms with time
	
	Nt[0] = N0 # place initial value of N
	for z in range(1,n_panels): 
		Nt[z] = Nt[z-1] + f(Nt[z-1]) * dt # integrate up to zth panel and fill appropriate place iin array
	return Nt
	
def solve_heun(N0, t1, n_panels):
    '''using the Heun's Method, a set of values is returned thats approximates the number of undecayed atoms left after time t, in hours'''
    dt = t1 / n_panels # define the panel width
    Nt = numpy.zeros(n_panels, dtype = numpy.float32) # create array of values of N, the number of atoms with time
    
    Nt[0] = N0 # place initial value of N
    for z in range(1, n_panels):
        N0 = Nt[z-1]  # define values needed for the Heun's method for each iteration
        k0 = f(Nt[z-1])
        k1 = f(N0 + k0 * dt) 
        Nt[z] = N0 + dt/2 * (k0 + k1 ) # calculate the next value in the sequence using Heun's method equation
    return Nt

#Set global values for test
t1 = 45
N_PANELS = 10
N0 = 1000
#create arays of time and number of undecayed atoms for each method
TIMEPOINTS = numpy.arange(0, t1, t1/N_PANELS )
n_analytic = analytic(N0, TIMEPOINTS)
n_euler = solve_euler(N0, t1, N_PANELS)
n_heun = solve_heun(N0, t1, N_PANELS)
#calculate the percentage errors in each numeric method
err_euler = 100 * abs(n_euler - n_analytic) / n_analytic
err_heun = 100 * abs(n_heun - n_analytic) / n_analytic


#Create subplot graph of undecayed atoms with time with the 3 methods plotted againt time
pyplot.figure()
pyplot.subplot(211)
pyplot.plot(TIMEPOINTS, n_analytic, color='grey', label='Analytic')
pyplot.plot(TIMEPOINTS, n_euler, color='red', label="Euler's")
pyplot.plot(TIMEPOINTS, n_heun, color='blue', label="Heun's", linestyle="--")
pyplot.xlabel("Time Passed (Hours)")
pyplot.ylabel("Undecayed Iodene-133 Atoms")
pyplot.legend()
pyplot.title("Contrasting Modelling Methods for Radioactive Decay")
#create subplot of percentage errors on the two numeric methods used - Heun's and Euler's
pyplot.subplot(212)
pyplot.semilogy()
pyplot.plot(TIMEPOINTS, err_euler, color='red', label="Euler's")
pyplot.plot(TIMEPOINTS, err_heun, color='blue', label="Heun's", linestyle = '--')
pyplot.ylabel("Error in Methods (%)")
pyplot.show()

ANSWER1 = """Heun's method is more accurate because it takes into account that the gradient (decay rate in this case),
changes over the interval dt. It tries to estimate an average gradient over this time which is more accurate than that 
constant one used in Euler's method. This leads to a lesser error in each interval and a lesser error overall"""