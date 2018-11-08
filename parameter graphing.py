from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

Temp=numpy.array([10,15,20,25,30,35,40,45,50,55,60,65])
n = numpy.array([0.368625593,0.346368274,0.301035187,0.23760474,0.195910723,0.20301611,0.228064763,0.275421762,0.281622236,0.274182846,0.318111344,0.328173682])
dn = numpy.array([0.00242,0.003501465,0.002905968,0.001079754,0.003089617,0.004363071,0.005139527,0.002833398,0.003801113,0.003741326,0.004435592,0.004706751])
K =(1/1000) * numpy.array([25335.51329,25858.11404,28217.12721,31203.47546,32947.08823,31585.9789,28918.33661,25455.16399,25033.35477,23860.95547,20544.56175,19480.6714])
dK = (1/1000) * numpy.array([132.8,217.2553674,234.7889575,94.01484254,279.2236401,258.1782635,318.7616996,171.1699765,216.183258,226.2964325,219.5241016,238.8678697])
RedChi = [16.88944269,19.0382326,26.86181305,230.2510656,12.34036348,0.596890262,3.504030435,14.35024733,21.28720252,25.32837525,19.97877211,4.65651664]
Percent_dn = dn/n
Percent_dK = dK/K

pyplot.close('all')

pyplot.figure()
ax1 = pyplot.subplot(211)
ax1.plot(Temp, n, label="n", color = 'red', marker = ".", linestyle = '' )
pyplot.fill_between(Temp, n-dn, n+dn, facecolor='red', alpha=0.3, edgecolor='none')
pyplot.ylabel("Value of Parameter n")

pyplot.twinx()
pyplot.plot(Temp, K, label="K", color = 'purple', marker = ".", linestyle = '')
pyplot.ylabel("Value of Parameter K - Pa.s")
pyplot.fill_between(Temp, K-dK, K+dK, facecolor='purple', alpha=0.3, edgecolor='none')
pyplot.title("")


ax1.set_xticklabels([])

pyplot.subplot(212)
pyplot.plot(Temp, RedChi, color='red', label="RedChi", marker = '^', linestyle = '') #for the eulers soln
pyplot.ylabel("Reduced Chi Squared")
pyplot.xlabel("Temperature - Degrees Celcius")
pyplot.semilogy()
#pyplot.bar(Temp-2.5, RedChi, 5, color='pink', alpha=0.7)


pyplot.tight_layout()

pyplot.show()