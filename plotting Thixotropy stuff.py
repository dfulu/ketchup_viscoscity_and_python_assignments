from __future__ import division
import numpy
import matplotlib.pyplot as pyplot

Time = numpy.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301])

#20 degrees Recovery
#Mod = (1/1000) * numpy.array([73993.14438,74299.77916,74602.26951,74900.67144,75195.04022,75485.43035,75771.89561,76054.48905,76333.263,76608.26907,76879.55821,77147.18064,77411.18593,77671.62295,77928.53995,78181.9845,78432.00353,78678.64333,78921.94959,79161.96736,79398.74108,79632.3146,79862.73118,80090.03348,80314.26359,80535.46305,80753.6728,80968.93326,81181.28429,81390.76522,81597.41484,81801.2714,82002.37268,82200.75589,82396.45779,82589.51461,82779.9621,82967.83553,83153.16969,83335.9989,83516.35702,83694.27745,83869.79312,84042.93656,84213.73981,84382.23451,84548.45186,84712.42264,84874.17722,85033.74554,85191.15716,85346.44123,85499.6265,85650.74135,85799.81374,85946.8713,86091.94124,86235.05045,86376.22541,86515.49227,86652.87681,86788.40449,86922.1004,87053.98929,87184.09559,87312.4434,87439.05647,87563.95826,87687.1719,87808.72019,87928.62566,88046.9105,88163.59663,88278.70564,88392.25885,88504.2773,88614.78171,88723.79257,88831.33006,88937.41408,89042.06428,89145.30005,89247.1405,89347.60449,89446.71062,89544.47725,89640.92248,89736.06417,89829.91994,89922.50716,90013.84299,90103.94434,90192.8279,90280.51011,90367.00723,90452.33526,90536.51001,90619.54707,90701.46181,90782.2694,90861.98481,90940.6228,91018.19793,91094.72456,91170.21688,91244.68884,91318.15426,91390.62673,91462.11967,91532.64632,91602.21975,91670.85283,91738.55827,91805.34862,91871.23624,91936.23333,92000.35193,92063.60392,92126.001,92187.55473,92248.2765,92308.17758,92367.26903,92425.56182,92483.06673,92539.79441,92595.75536,92650.95996,92705.41842,92759.14083,92812.13713,92864.41715,92915.99055,92966.8669,93017.0556,93066.56597,93115.40716,93163.58822,93211.11807,93258.00551,93304.25923,93349.8878,93394.89965,93439.30313,93483.10646,93526.31775,93568.945,93610.99611,93652.47886,93693.40094,93733.76991,93773.59327,93812.87839,93851.63252,93889.86287,93927.5765,93964.7804,94001.48145,94037.68646,94073.40212,94108.63506,94143.3918,94177.67877,94211.50232,94244.86872,94277.78414,94310.25468,94342.28635,94373.88509,94405.05675,94435.80709,94466.14182,94496.06654,94525.58681,94554.70809,94583.43576,94611.77516,94639.73153,94667.31004,94694.51581,94721.35387,94747.82918,94773.94666,94799.71114,94825.1274,94850.20013,94874.93398,94899.33353,94923.4033,94947.14774,94970.57126,94993.6782,95016.47282,95038.95935,95061.14196,95083.02475,95104.61178,95125.90703,95146.91447,95167.63797,95188.08138,95208.24848,95228.143,95247.76863,95267.129,95286.2277,95305.06826,95323.65418,95341.9889,95360.0758,95377.91824,95395.51953,95412.88293,95430.01164,95446.90884,95463.57766,95480.02119,95496.24247,95512.24451,95528.03026,95543.60266,95558.96458,95574.11887,95589.06834,95603.81576,95618.36385,95632.71531,95646.8728,95660.83894,95674.61631,95688.20747,95701.61494,95714.84119,95727.88868,95740.75981,95753.45699,95765.98255,95778.33882,95790.52808,95802.5526,95814.41459,95826.11626,95837.65977,95849.04726,95860.28083,95871.36258,95882.29455,95893.07876,95903.71721,95914.21188,95924.5647,95934.7776,95944.85246,95954.79114,95964.5955,95974.26735,95983.80847,95993.22063,96002.50558,96011.66504,96020.7007,96029.61424,96038.4073,96047.08151,96055.63849,96064.07981,96072.40704,96080.62172,96088.72537,96096.71949,96104.60557,96112.38505,96120.0594,96127.63001,96135.09831,96142.46566,96149.73344,96156.90299,96163.97563,96170.95268,96177.83543,96184.62516,96191.32311,96197.93054,96204.44866,96210.87869,96217.2218,96223.47919,96229.652,96235.74138,96241.74845,96247.67434,96253.52013,96259.28691,96264.97575,96270.5877,96276.1238,96281.58507,96286.97253,96292.28717,96297.52998])
#Meas = (1/1000) * numpy.array([307000,117000,97000,88166.66667,84500,81833.33333,80000,78000,77000,76500,76333.33333,76500,76666.66667,76833.33333,77000,77500,77666.66667,78000,78500,78666.66667,79000,79333.33333,79666.66667,80000,80333.33333,80666.66667,81000,81333.33333,81666.66667,82000,82166.66667,82333.33333,82666.66667,83000,83166.66667,83500,83833.33333,83833.33333,84000,84333.33333,84500,84666.66667,84833.33333,84833.33333,85166.66667,85333.33333,85333.33333,85833.33333,85833.33333,85833.33333,86000,86333.33333,86333.33333,86333.33333,86666.66667,86833.33333,86833.33333,87166.66667,87000,87333.33333,87333.33333,87333.33333,87666.66667,87833.33333,87833.33333,87833.33333,87833.33333,88000,88000,88333.33333,88166.66667,88333.33333,88333.33333,88500,88666.66667,88833.33333,88666.66667,88833.33333,88833.33333,89000,89166.66667,89333.33333,89166.66667,89333.33333,89500,89333.33333,89500,89833.33333,89833.33333,89833.33333,89833.33333,89833.33333,90333.33333,90333.33333,90333.33333,90333.33333,90333.33333,90333.33333,90500,90666.66667,90666.66667,90833.33333,90666.66667,90833.33333,91000,91000,91000,91166.66667,91166.66667,91166.66667,91166.66667,91166.66667,91166.66667,91333.33333,91500,91333.33333,91500,91500,91666.66667,91833.33333,91833.33333,91833.33333,91833.33333,91833.33333,91833.33333,91833.33333,92000,91833.33333,92000,92166.66667,92166.66667,92333.33333,92333.33333,92333.33333,92333.33333,92500,92333.33333,92333.33333,92500,92333.33333,92500,92500,92666.66667,93000,92833.33333,93000,93000,93333.33333,93166.66667,93333.33333,93500,93333.33333,93500,93500,93666.66667,93666.66667,93666.66667,93666.66667,93666.66667,93833.33333,93666.66667,93833.33333,93833.33333,94000,94000,94000,94000,94000,94000,94000,94166.66667,94166.66667,94333.33333,94500,94500,94333.33333,94500,94500,94500,94500,94666.66667,94500,94666.66667,94833.33333,94666.66667,94666.66667,94833.33333,94500,94833.33333,94833.33333,94833.33333,94833.33333,94833.33333,94666.66667,94833.33333,94833.33333,94666.66667,94833.33333,94833.33333,94666.66667,95000,95000,95000,95000,95000,95000,95000,95000,95166.66667,95333.33333,95333.33333,95333.33333,95333.33333,95333.33333,95333.33333,95333.33333,95500,95333.33333,95333.33333,95333.33333,95333.33333,95500,95500,95333.33333,95500,95666.66667,95500,95500,95666.66667,95500,95666.66667,95666.66667,95666.66667,95500,95666.66667,95666.66667,95500,95833.33333,95666.66667,95833.33333,96000,95833.33333,95833.33333,95833.33333,95833.33333,95833.33333,96000,95833.33333,95833.33333,96166.66667,95833.33333,96000,96166.66667,95833.33333,96000,96166.66667,96000,96166.66667,96000,96000,96000,96000,96000,96000,96166.66667,96166.66667,96500,96500,96500,96500,96500,96500,96500,96500,96666.66667,96666.66667,96666.66667,96666.66667,96666.66667,96666.66667,96666.66667,96666.66667,96833.33333,96500,96666.66667,96833.33333,97000,97000,97000,97000,97000,97000,97000,97000,97000,97000,97000,97166.66667,97166.66667,97166.66667,97166.66667])
#Err = (1/1000) * numpy.array([5131.601439,577.3502692,288.6751346,166.6666667,288.6751346,333.3333333,288.6751346,288.6751346,288.6751346,288.6751346,440.9585518,577.3502692,440.9585518,440.9585518,288.6751346,288.6751346,333.3333333,288.6751346,288.6751346,333.3333333,500,440.9585518,333.3333333,500,440.9585518,600.9252126,500,440.9585518,600.9252126,500,333.3333333,440.9585518,333.3333333,500,600.9252126,500,440.9585518,440.9585518,577.3502692,440.9585518,577.3502692,440.9585518,440.9585518,600.9252126,440.9585518,600.9252126,600.9252126,600.9252126,600.9252126,600.9252126,763.7626158,600.9252126,600.9252126,600.9252126,440.9585518,600.9252126,600.9252126,440.9585518,763.7626158,600.9252126,600.9252126,600.9252126,726.4831573,600.9252126,600.9252126,600.9252126,600.9252126,763.7626158,763.7626158,600.9252126,666.6666667,600.9252126,600.9252126,763.7626158,666.6666667,600.9252126,666.6666667,600.9252126,600.9252126,763.7626158,666.6666667,600.9252126,666.6666667,600.9252126,500,600.9252126,500,600.9252126,600.9252126,600.9252126,600.9252126,600.9252126,600.9252126,600.9252126,600.9252126,600.9252126,600.9252126,600.9252126,577.3502692,440.9585518,726.4831573,600.9252126,440.9585518,600.9252126,577.3502692,577.3502692,577.3502692,600.9252126,600.9252126,600.9252126,600.9252126,600.9252126,600.9252126,666.6666667,500,666.6666667,500,500,600.9252126,666.6666667,666.6666667,666.6666667,666.6666667,666.6666667,666.6666667,666.6666667,763.7626158,666.6666667,763.7626158,600.9252126,833.3333333,666.6666667,666.6666667,666.6666667,666.6666667,500,666.6666667,666.6666667,500,666.6666667,500,500,600.9252126,500,440.9585518,500,500,440.9585518,600.9252126,666.6666667,500,440.9585518,500,500,600.9252126,600.9252126,600.9252126,600.9252126,600.9252126,440.9585518,600.9252126,440.9585518,440.9585518,577.3502692,577.3502692,577.3502692,577.3502692,577.3502692,577.3502692,577.3502692,726.4831573,440.9585518,600.9252126,577.3502692,577.3502692,600.9252126,577.3502692,577.3502692,763.7626158,577.3502692,726.4831573,763.7626158,726.4831573,600.9252126,726.4831573,726.4831573,600.9252126,763.7626158,600.9252126,600.9252126,833.3333333,600.9252126,600.9252126,666.6666667,600.9252126,600.9252126,666.6666667,600.9252126,600.9252126,666.6666667,500,500,500,500,500,500,500,500,666.6666667,600.9252126,600.9252126,600.9252126,600.9252126,600.9252126,600.9252126,600.9252126,500,600.9252126,600.9252126,600.9252126,600.9252126,577.3502692,577.3502692,600.9252126,577.3502692,440.9585518,577.3502692,577.3502692,440.9585518,577.3502692,600.9252126,333.3333333,600.9252126,500,333.3333333,600.9252126,500,440.9585518,600.9252126,666.6666667,500,666.6666667,666.6666667,666.6666667,666.6666667,666.6666667,500,666.6666667,666.6666667,600.9252126,666.6666667,763.7626158,600.9252126,666.6666667,500,600.9252126,500,600.9252126,500,500,500,500,500,500,333.3333333,600.9252126,500,500,500,500,500,500,500,500,600.9252126,600.9252126,600.9252126,600.9252126,600.9252126,600.9252126,600.9252126,600.9252126,440.9585518,577.3502692,600.9252126,440.9585518,577.3502692,577.3502692,577.3502692,577.3502692,577.3502692,577.3502692,577.3502692,577.3502692,577.3502692,577.3502692,577.3502692,440.9585518,726.4831573,440.9585518,440.9585518])
#Res = (1/1000) * numpy.array([233006.8556,42700.22084,22397.73049,13265.99522,9304.95978,6347.902982,4228.104388,1945.510951,666.7370047,-108.2690731,-546.2248755,-647.1806401,-744.5192589,-838.2896206,-928.5399534,-681.9845,-765.3368604,-678.6433333,-421.9495918,-495.3006917,-398.7410797,-298.9812685,-196.0645116,-90.0334778,19.06974083,131.2036211,246.3272009,364.400072,485.3823722,609.2347781,569.251831,532.0619301,664.2939915,799.2441084,770.2088774,910.4853914,1053.371233,865.4978024,846.8303081,997.3344301,983.6429784,972.3892208,963.5402097,790.3967764,952.9268578,951.0988245,784.8814743,1120.910694,959.1561182,799.5877941,808.8428389,986.8921029,833.7068305,682.5919879,866.8529249,886.462036,741.392089,931.6162196,623.7745934,817.8410674,680.4565187,544.9288395,744.566266,779.3440403,649.2377391,520.8899356,394.2768624,436.0417397,312.8281048,524.6131408,238.0410058,286.4228291,169.7367064,221.294363,274.4078163,329.0560383,51.88495192,109.5407605,2.003277406,62.58592191,124.6023826,188.0332803,-80.47383577,-14.27115778,53.28937686,-211.1439178,-140.9224796,97.26916499,3.413397433,-89.17382923,-180.5096604,-270.6110098,140.5054376,52.82322208,-33.67389334,-119.0019263,-203.1766781,-286.2137361,-201.4618106,-115.6027375,-195.3181473,-107.2894686,-351.5312636,-261.3912312,-170.2168758,-244.6888441,-318.1542601,-223.9600615,-295.4530023,-365.9796549,-435.5530795,-504.1861598,-571.8916054,-472.0152874,-371.2362407,-602.8999999,-500.3519345,-563.6039181,-459.3343305,-354.221393,-414.9431709,-474.8442421,-533.9356991,-592.2284846,-649.7333933,-706.461074,-595.755365,-817.6266291,-705.4184226,-592.4741635,-645.4704668,-531.0838132,-582.6572171,-633.5335624,-683.7222704,-566.5659685,-782.0738251,-830.2548845,-711.1180691,-924.6721805,-804.2592347,-849.887797,-728.2329836,-439.3031298,-649.7731251,-526.3177477,-568.9449994,-277.6627741,-485.8121921,-360.0676019,-233.7699149,-440.25994,-312.8783851,-351.6325249,-223.1962028,-260.9098316,-298.1137284,-334.8147828,-371.0197911,-240.0687911,-441.9683966,-310.0584656,-344.3454342,-211.5023185,-244.8687153,-277.7841367,-310.2546781,-342.2863523,-373.8850911,-405.056746,-269.1404226,-299.4751488,-162.7332085,-25.58680996,-54.70808645,-250.1024307,-111.7751625,-139.7315297,-167.3100428,-194.5158087,-54.68719875,-247.8291829,-107.2799971,33.62218868,-158.4607299,-183.5334594,-41.60064286,-399.3335272,-90.06996413,-113.8144109,-137.2379311,-160.3448625,-183.1394839,-372.2926832,-227.8086245,-249.6914156,-437.9451087,-292.5737013,-313.581137,-500.9713059,-188.081379,-208.2484753,-228.1429961,-247.7686254,-267.1289975,-286.2276977,-305.0682627,-323.6541813,-175.3222286,-26.74246669,-44.58491143,-62.18620028,-79.54959267,-96.67830397,-113.5755061,-130.2443281,19.97880991,-162.9091371,-178.9111729,-194.6969275,-210.2693242,-58.96457999,-74.11887292,-255.7350093,-103.8157575,48.30281825,-132.7153095,-146.8727983,5.827730149,-174.6163105,-21.54080477,-34.94826958,-48.17452105,-227.8886751,-74.09314787,-86.79032286,-265.9825514,54.99451383,-123.8614155,30.78073687,185.5854108,7.217076351,-4.326433386,-15.71392272,-26.94750041,-38.0292467,117.7054529,-59.74542586,-70.38388017,252.4547867,-91.23136878,65.22240301,221.8142108,-121.4578111,35.4044969,192.3993192,16.19153134,173.4460333,-2.505584709,-11.66504196,-20.70070132,-29.61423602,-38.40729669,-47.08151162,111.0281795,102.5868589,427.5929632,419.3782838,411.2746328,403.2805096,395.3944338,387.614945,379.9406027,372.3699857,531.5683587,524.2010054,516.9332281,509.7636811,502.6910367,495.7139851,488.8312343,482.0415097,642.0102208,302.0694604,462.2180051,622.4546478,782.7781977,776.5208136,770.3480034,764.258624,758.2515477,752.3256623,746.4798702,740.713089,735.0242508,729.4123021,723.8762037,885.081597,879.6941375,874.3794941,869.1366826])

#20 degrees decay
Mod = (1/1000) * numpy.array([4705.811577,4595.173193,4505.107792,4431.789871,4372.105269,4323.518898,4283.967064,4251.769814,4225.559577,4204.223081,4186.854063,4172.714779,4161.204666,4151.834836,4144.207306,4137.9981,4132.943484,4128.828763,4125.479166,4122.75242,4120.532707,4118.725745,4117.254784,4116.057345,4115.082568,4114.289048,4113.643082,4113.117232,4112.689162,4112.340692,4112.057018,4111.826094,4111.638109,4111.485079,4111.360505,4111.259096,4111.176543,4111.109341,4111.054635,4111.010101,4110.973848,4110.944337,4110.920313,4110.900756,4110.884836,4110.871876,4110.861326,4110.852738,4110.845747,4110.840055,4110.835422,4110.831651,4110.828581,4110.826081,4110.824047,4110.82239,4110.821042,4110.819945,4110.819051,4110.818324,4110.817732]) 
Meas = (1/1000) * numpy.array([1757.41,4803.703333,4507.41,4400,4318.52,4277.776667,4250.003333,4233.333333,4218.52,4194.443333,4187.036667,4187.036667,4181.483333,4164.816667,4159.26,4148.15,4151.85,4146.296667,4153.703333,4148.146667,4148.15,4140.743333,4137.036667,4138.89,4138.886667,4133.333333,4138.89,4125.926667,4129.63,4120.37,4120.37,4114.813333,4105.553333,4111.11,4118.52,4103.703333,4100.003333,4103.703333,4105.556667,4098.15,4101.85,4098.146667,4098.15,4096.296667,4100.003333,4100.003333,4107.406667,4105.556667,4101.853333,4107.41,4103.703333,4105.553333,4107.406667,4109.256667,4114.813333,4107.406667,4111.113333,4116.666667,4125.926667,4120.373333,4124.073333]) 
Err = (1/1000) * numpy.array([242.4645973,47.28647775,28.92673216,21.0326516,34.2975762,34.69496713,24.21521308,23.12971129,26.12262685,30.59879101,21.83521035,21.83521035,24.07666667,24.91323767,15.82162234,15.82162234,20.37,23.20371115,21.3570631,20.86870251,24.28768481,18.2379863,16.45759838,17.85786381,23.13051184,16.97298769,13.98242587,18.2379863,8.069698466,12.96142868,20.87151248,19.33484103,14.69840846,9.624428987,17.66517195,16.14245575,5.556666667,13.35255822,13.98043911,11.26461865,9.26,18.79400643,16.45834844,17.66639497,11.56525592,22.45191479,20.61928736,9.62154238,9.801248787,11.26461865,15.82298785,11.56525592,12.14447794,20.86870251,19.33484103,12.96452382,16.66666667,21.03529283,18.79400643,19.33484103,19.59871793])
Res = (1/1000) * numpy.array([-2948.401577,208.5301408,2.302207805,-31.78987087,-53.58526874,-45.742231,-33.96373071,-18.43648055,-7.039577283,-9.779747836,0.182603309,14.32188738,20.27866685,12.98183078,15.05269366,10.15189952,18.9065161,17.46790362,28.22416712,25.39424653,27.61729302,22.01758834,19.78188273,22.83265488,23.80409905,19.04428531,25.2469182,12.80943498,16.94083767,8.029308386,8.31298168,2.987239832,-6.084775352,-0.375079266,7.159494642,-7.555762382,-11.17320966,-7.406007446,-5.497968016,-12.86010107,-9.1238484,-12.79767017,-12.77031289,-14.60408948,-10.88150261,-10.86854273,-3.454659385,-5.296071125,-8.992413169,-3.430055228,-7.132088902,-5.278317404,-3.421913876,-1.569414578,3.989286648,-3.415723782,0.292291148,5.846722037,15.10761551,9.555009501,13.25560158])

#70 degrees modelling residuals

#Mod = (1/1000) *(-32700 +   numpy.array([33414.3963944948,33360.02789,33304.19808,33247.05225,33188.73913,33129.41045,33069.22062,33008.32626,32946.88584,32885.05925,32823.00738,32760.89171,32698.87389,32637.1153,32575.77667,32515.01762,32454.99626,32395.86878,32337.78906,32280.90823,32225.37433,32171.33186,32118.92146,32068.27953,32019.53785,31972.82325,31928.25732,31885.95601,31846.02942,31808.58145,31773.70955,31741.50446,31712.04999,31685.4228,31661.69217,31640.91987,31623.15994,31608.45861,31596.85414,31588.37671,31583.0484,31580.88306,31581.88634,31586.05562,31593.38005,31603.84057,31617.40997,31634.05292,31653.72612,31676.37838,31701.95073,31730.37664,31761.58214,31795.48601,31832.00002,31871.02916,31912.47186,31956.22027,32002.16055,32050.17314,32100.13309,32151.9104,32205.37032,32260.37374,32316.77752,32374.43487,32433.19575,32492.90725,32553.41399,32614.55849,32676.18165,32738.12309,32800.22163,32862.31568,32924.24362,32985.84433,33046.95747,33107.42403,33167.08665,33225.79005,33283.38149,33339.71109,33394.63226,33448.00207,33499.68165,33549.5365,33597.43689,33643.25816,33686.88107,33728.1921,33767.08375,33803.45481,33837.21062,33868.26335,33896.53218,33921.94355,33944.43134,33963.93701,33980.40982,33993.80689,34004.09336,34011.24246,34015.23559,34016.06235,34013.7206,34008.21643,33999.56415,33987.7863,33972.91351,33954.98449,33934.0459,33910.15223,33883.36565,33853.75588,33821.39997,33786.38211,33748.79345,33708.73178,33666.30138,33621.61265,33574.78189,33525.93097,33475.18701,33422.68208,33368.55279,33312.94002,33255.98849,33197.8464,33138.66506,33078.59847,33017.80296,32956.43673,32894.65947,32832.63195,32770.51558,32708.47202,32646.66271,32585.24852,32524.38925,32464.24328,32404.96714,32346.71508,32289.63868,32233.88648,32179.60357,32126.93121,32076.00647,32026.96186,31979.92503,31935.01837,31892.35876,31852.05719,31814.21855,31778.94131,31746.31728,31716.43134,31689.36127,31665.17752,31643.94303,31625.71304,31610.53501,31598.44842,31589.48474,31583.66729,31581.0112,31581.52339,31585.20253,31592.03905,31602.01514,31615.10486,31631.27413,31650.48088,31672.67513,31697.79912,31725.78747,31756.56734,31790.05864,31826.17421,31864.82006,31905.89563,31949.29403,31994.90231,32042.6018,32092.26835,32143.77273,32196.9809,32251.75439,32307.95067,32365.4235,32424.02332,32483.59762,32543.99137,32605.04742,32666.60687,32728.50953,32790.5943,32852.69963,32914.66388,32976.32582,33037.52498,33098.10209,33157.89952,33216.76165,33274.5353,33331.07013,33386.21902,33439.83845,33491.78889,33541.93514,33590.14671,33636.29813,33680.26931,33721.94582,33761.21919,33797.98723,33832.15426,33863.63137,33892.33663,33918.19535,33941.14023,33961.11157,33978.0574,33991.93361,34002.70409,34010.34082,34014.82393,34016.14174,34014.29083,34009.27601,34001.11033,33989.81505,33975.41956,33957.96132,33937.48576,33914.04616,33887.70353,33858.52641,33826.59074,33791.97962,33754.78311,33715.09803,33673.02764,33628.68141,33582.17477,33533.62872,33483.16961,33430.92874,33377.04206,33321.64981,33264.89612,33206.9287,33147.8984,33087.95882,33027.26595,32965.97774,32904.25368,32842.25438,32780.1412,32718.07577,32656.21961,32594.73369,32533.77801,32473.51121,32414.0901,32355.66934,32298.40094,32242.43394,32187.91398,32134.98294,32083.77857,32034.43411,31987.07798,31941.83341,31898.81814,31858.14412,31819.91718,31784.23681,31751.19587,31720.88033,31693.36908,31668.73372,31647.03836,31628.33945,31612.68566,31600.11773,31590.66835,31584.36212,31581.21545,31581.23652,31584.42529,31590.77346,31600.2645,31612.87372,31628.5683,31647.3074,31669.04226,31693.71631,31721.26534,31751.61767,31784.69431,31820.40917]))
#Meas = (1/1000) * numpy.array([158831.034491958,31331.03449,13331.03449,7831.034492,3831.034492,1331.034492,331.034492,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-1168.965508,-1168.965508,-668.965508,-1168.965508,-1168.965508,-668.965508,-1168.965508,-1168.965508,-668.965508,-668.965508,-1168.965508,-668.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-168.965508,-168.965508,-668.965508,-168.965508,-168.965508,-168.965508,331.034492,-168.965508,-168.965508,331.034492,331.034492,331.034492,831.034492,831.034492,831.034492,831.034492,831.034492,831.034492,831.034492,831.034492,831.034492,1331.034492,831.034492,831.034492,1331.034492,1331.034492,831.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,831.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,831.034492,1331.034492,831.034492,831.034492,831.034492,831.034492,831.034492,831.034492,331.034492,331.034492,331.034492,331.034492,-168.965508,-168.965508,-168.965508,-168.965508,-168.965508,-168.965508,-168.965508,-168.965508,-168.965508,-668.965508,-168.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-168.965508,-168.965508,-668.965508,-168.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-1168.965508,-1168.965508,-668.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-1168.965508,-668.965508,-1168.965508,-1168.965508,-668.965508,-668.965508,-1168.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-168.965508,-168.965508,-168.965508,-168.965508,-168.965508,-168.965508,331.034492,331.034492,331.034492,331.034492,331.034492,331.034492,331.034492,331.034492,331.034492,831.034492,831.034492,831.034492,1331.034492,1331.034492,831.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1831.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1831.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,1331.034492,831.034492,831.034492,831.034492,831.034492,331.034492,331.034492,331.034492,-168.965508,331.034492,-168.965508,-168.965508,-168.965508,-168.965508,-168.965508,331.034492,-168.965508,-168.965508,-168.965508,-168.965508,-668.965508,-168.965508,-168.965508,-168.965508,-168.965508,-168.965508,-168.965508,-168.965508,-168.965508,-168.965508,-168.965508,-168.965508,-668.965508,-168.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-1168.965508,-1168.965508,-668.965508,-1168.965508,-1168.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508,-668.965508])
#Err = numpy.zeros((len(Mod)))+0.225
#Res = (1/1000) * numpy.array([158085.603605505,30639.97211,12695.80192,7252.947747,3311.260871,870.5895476,-69.2206169,-1008.326256,-946.8858357,-885.059245,-823.0073765,-760.8917093,-698.8738886,-637.115305,-575.7766744,-515.0176199,-454.9962564,-395.868779,-337.7890566,-280.9082316,-225.3743264,-171.3318583,-618.9214634,-568.2795306,-19.53784677,-472.8232536,-428.2573176,114.0439861,-346.0294243,-308.5814507,226.290455,258.4955447,-212.0499895,314.577202,-161.6921732,-140.9198701,-123.1599448,-108.4586145,-96.85413692,-88.37671058,-83.04839654,-80.88306081,-81.8863383,-86.05561815,-93.38005055,-103.8405749,-117.4099696,-134.0529226,-153.7261235,-176.3783762,-201.9507323,-230.3766441,-261.5821381,-295.4860075,-332.0000234,-371.0291645,-412.4718641,-456.2202749,-502.1605493,-550.1731357,-600.1330898,-651.9103994,-705.3703232,-260.3737411,-316.7775162,-374.4348675,-433.1957519,-492.9072544,-553.4139862,-114.5584891,-176.1816452,-738.123091,-300.2216347,-362.3156757,-424.243625,14.15567411,-546.9574734,-607.4240312,-167.0866455,-225.7900549,-283.381494,160.2889089,105.3677418,51.99792745,0.318351427,-49.53649915,-97.43688574,-143.2581559,-186.8810679,-228.1921005,232.9162509,-303.454805,-337.2106188,131.7366532,103.4678202,-421.9435531,55.56866198,36.06298602,19.59017911,6.193108866,-4.093361179,-11.24246228,-15.23559015,-16.06235336,-13.72060042,-8.216425321,0.435848277,12.21370434,27.08649306,45.01551058,-434.0459002,89.84777162,116.634347,146.2441185,178.6000319,213.6178865,251.2065546,291.2682181,333.6986235,-121.6126469,425.2181124,-25.93096768,24.81298699,77.31792409,131.4472087,187.0599787,244.0115116,-197.8463989,-138.6650576,-78.59847358,-17.80295964,-456.4367255,-394.6594661,-332.6319459,-270.5155808,-208.4720178,-146.6627144,-85.24851862,-24.38925009,35.75671553,-404.9671412,153.284924,-289.6386798,-233.8864839,-179.6035738,-126.9312111,-76.00646661,-26.96186302,20.07496964,64.9816262,607.6412449,647.9428116,185.7814484,721.058687,253.6827243,283.5686622,310.6387276,334.8224753,356.0569715,374.2869571,389.4649916,401.551577,410.5152599,416.332714,418.9888003,418.4766068,-85.20253349,-92.03904634,397.9848591,-115.1048561,-131.2741283,-150.4808798,-172.6751283,-197.7991171,274.2125344,-256.5673388,-290.0586375,173.8257935,135.1799387,-405.8956328,50.70597099,5.097686882,-42.60179755,-92.26835273,-143.7727301,-196.9808985,248.2456071,192.049325,134.5764964,75.9766843,16.40238439,-43.99137156,394.9525807,333.3931288,271.4904706,209.4056968,147.3003724,85.33611553,23.67417741,-37.52497753,-98.10208916,342.1004839,283.238354,225.4646996,668.9298665,613.7809768,60.16154582,508.2111088,458.0648577,409.8532895,363.7018661,319.7306888,278.0541849,238.7808101,202.0127666,167.8457367,636.3686344,107.6633731,81.80465329,58.85976788,38.88842687,21.94260219,508.0663924,-2.704092065,-10.34082293,-14.82392692,-16.14173753,-14.29082541,-9.27600722,-1.110333153,10.18494705,24.58043939,42.03868211,62.51424317,85.95383851,112.2964707,141.4735875,173.4092607,208.0203833,245.2168857,284.9019707,326.9723646,371.3185867,417.8252337,-33.62872001,16.83039308,69.0712619,122.9579387,-321.6498072,-264.8961245,-206.9287047,-647.8983979,-87.95882028,-527.2659541,-465.9777418,-404.2536755,-342.2543812,-280.1412012,281.9242257,-156.219615,-94.73369302,-33.77801484,26.48879305,-414.0901032,144.3306633,201.5990627,257.5660641,312.086023,365.0170608,416.2214336,465.5658911,512.9220228,558.1665928,601.1818598,641.8558843,180.082819,715.7631852,248.8041307,279.1196725,306.6309195,331.2662785,352.9616404,371.6605466,387.3143366,399.8822741,409.3316533,-84.36211627,-81.21544541,418.7634772,-84.42529358,-90.77345954,399.7354993,387.1262818,371.4317011,352.6925998,330.9577429,306.2836918,278.7346564,248.3823281,215.3056936,179.5908292])

pyplot.close('all')

pyplot.figure()
ax1 = pyplot.subplot(211)
pyplot.fill_between(Time[2:61], Meas[2:]-Err[2:], Meas[2:]+Err[2:], facecolor='red', alpha=0.1, edgecolor='none')
pyplot.plot(Time[2:61], Meas[2:], linestyle = '', marker ='.',markersize = 2, color = 'red')
ax1.plot(Time[2:61], Mod[2:], label="Mod", color = 'Black', linewidth =0.5)

pyplot.ylabel("Viscosity - Pa.s")

pyplot.title("")
ax1.set_xticklabels([])

pyplot.subplot(212)
pyplot.plot(Time[2:61], Res[2:], linestyle = '', marker ='.', color = 'red')
#pyplot.errorbar(Time[2:61], Res[2:], yerr=Err[2:],label="Res", marker = '.', color = 'red', linestyle = '' ) 
pyplot.fill_between(Time[2:61], Res[2:]-Err[2:], Res[2:]+Err[2:], facecolor='red', alpha=0.3, edgecolor='none')
pyplot.ylabel("Residuals - Pa.s")
pyplot.xlabel("Time - s")

#pyplot.semilogy()

pyplot.tight_layout()

pyplot.show()