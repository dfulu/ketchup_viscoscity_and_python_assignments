from __future__ import division
import numpy.random
import matplotlib.pyplot as pyplot

USER = "James Fulton"
USER_ID = "njzc77"

scatter_plot = numpy.zeros((51200,2))

def estimate_pi(n):
	scatter = numpy.random.uniform(size = (n,2))
	r = (scatter[:,0]**2 + scatter[:,1]**2)
        hit= len(scatter[r<1.0])
	pi_try = hit / n * 4
	return pi_try

def measure_error(n):
	estimates = numpy.zeros(50, dtype = numpy.float32)
	for i in range(50):
		estimates[i] = estimate_pi(n)
	standarddev = numpy.std((estimates-numpy.pi)/numpy.pi)
	return standarddev

N_VALUES = numpy.array((25, 50, 100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200))
dev_values = numpy.zeros(len(N_VALUES), dtype = numpy.float32)

for i in range(len(N_VALUES)):
	dev_values[i] = measure_error(N_VALUES[i])

pyplot.figure()
pyplot.loglog( N_VALUES,dev_values, color='red')
pyplot.xlabel("Number of Scatter Points")
pyplot.ylabel("Standard Deviation of Percentage Error")
pyplot.legend()
pyplot.title("Accuracy of Calculating Pi Using Random Scatter Method")
pyplot.show()

ANSWER1 = '''The accuracy increases with number of points because as the number of points scale, the ratio of points that hit and 
points that missed can become closer to the true value of pi (ie with 4 points the best ratio you can get is 3/4). It is also
statistically more likely with more points that the ratio will be closer to pi, as with more points there becomes a more even 
distribution over the x-y plane.'''