from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

USER = "James Fulton"
USER_ID = "njzc77"

g = 9.81 # gravitational constant (m/s)
LENGTH = 1.00 # length of pendulum (m)
KAPPA = 0.20 # damping constant (k)
MASS = 1.00 # mass of pendulum bob (kg)

def f((theta, omega), t):
    dtheta__dt = omega
    domega__dt = - g / LENGTH * theta - KAPPA / (LENGTH * MASS) * omega
    return numpy.array( (dtheta__dt, domega__dt) )

def solve_euler(X0, t1, n_panels):
    dt = t1 / n_panels # define the panel width
    t = numpy.zeros(n_panels, dtype = numpy.float32)
    dynamics = numpy.zeros((n_panels, 2), dtype = numpy.float32) # create a 2D array to hold theta and omega values
    
    dynamics[0] = X0
    for i in range(1,n_panels):
        t[i] = i * dt
        dynamics[i] = dynamics[i-1] + f(dynamics[i-1], t[i]) * dt
    return dynamics
    
def solve_blackbox(X0, t1, n_panels):
    timebase = numpy.arange(0, t1, t1/n_panels)
    dynamics = scipy.integrate.odeint(f, X0, timebase) # this line won't work ...integrate is not a module
    return dynamics
    

pyplot.figure()
pyplot.subplot(211)
pyplot.plot(TIMEPOINTS, theta, color='red', label="Euler's") # numeric
pyplot.plot(TIMEPOINTS, theta, color='grey', label="ODE int") # eulers
pyplot.xlabel("Time passed / s")
pyplot.ylabel("Angular Displacement of Bob")
pyplot.legend()
pyplot.title("Contrasting Modelling Methods for Pendulum Bob")

pyplot.subplot(212)
pyplot.semilogy()
pyplot.plot(omega, theta, color='red', label="Euler's") #for the eulers soln
pyplot.plot(omega, theta, color='grey', label="ODE int")# for the ode soln
pyplot.ylabel("Angular Displacement / rad")
pyplot.xlabel("Angular Velocity / rad/s")
pyplot.show()