#plot a sine wave from 0 to 4pi

import math
import pylab
# from matplotlib import pylab

#initializa the two lists and the counting variable num.Note is a float

y_value = []
x_value = []

num = 0.0

#collect both man and the sine of num in a list

while num <math.pi *4:
	y_value.append(math.sin(num))
	x_value.append(num)
	num += 0.1

#plot the x and y values as red circles

pylab.plot(x_value,y_value,'ro')
pylab.show()


