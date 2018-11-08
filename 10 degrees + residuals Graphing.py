from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

Mod = (1/1000) * numpy.array([13686.62057,12592.77303,11699.50591,10953.47074,8627.502686,7258.335587,6338.370066,5669.529127,5158.080775,4748.875785,4415.967924,4135.871201,3898.768804,3693.871083])
Res =(1/1000) *  numpy.array([704.4127679,291.093637,8.827421043,-202.7040712,-186.1426857,-126.0989207,-34.70673273,102.9575396,156.1258915,141.210882,90.79874232,24.37546587,-49.35213773,-105.5710832])
Meas =(1/1000) *  numpy.array([14391.03333,12883.86667,11708.33333,10750.76667,8441.36,7132.236667,6303.663333,5772.486667,5314.206667,4890.086667,4506.766667,4160.246667,3849.416667,3588.3])
Err =(1/1000) *  numpy.array([103.0418901,99.09598602,65.08541397,52.56666667,40.82961221,30.55834874,37.21655113,43.55231962,24.62915098,38.12577008,31.50460354,28.13262065,27.07485508,22.57438888])
SR = numpy.array([2.652,3.026,3.4,3.774,5.508,7.242,8.976,10.71,12.44,14.18,15.91,17.65,19.38,21.11])


pyplot.close('all')

pyplot.figure()
ax1 = pyplot.subplot(211)
ax1.plot(SR, Mod, label="Mod", color = 'pink', )
pyplot.plot(SR, Meas, linestyle = '', marker ='^', color = 'pink')
pyplot.ylabel("Viscosity - Pa.s")

pyplot.title("")
ax1.set_xticklabels([])

pyplot.subplot(212)
pyplot.errorbar(SR, Res, yerr=Err,label="Res", marker = '^', color = 'red', linestyle = '' ) 
pyplot.ylabel("Residuals - Pa.s")
pyplot.xlabel("Shear rate - $s^{-1}$")
#pyplot.semilogy()

pyplot.tight_layout()

pyplot.show()