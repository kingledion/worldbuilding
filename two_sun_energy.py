import rebound
from math import sqrt, sin, cos, pi, atan
from matplotlib import pyplot as plt
import numpy as np

def f(t):
	if t < 3/2*pi:
		return sin(t-pi/4)+sqrt(2), cos(t-pi/4)
	if t < 3/2 * pi + 2:
		r = t - 3/2*pi
		return sqrt(2)/2-r/sqrt(2), -sqrt(2)/2+r/sqrt(2)
	if t < 3*pi + 2:
		r = t - 3/2*pi - 2
		return sin(pi/4-r)-sqrt(2), cos(pi/4-r)
	if t < 3*pi + 4:
		r = t - 3*pi - 2
		return sqrt(2)/-2+r/sqrt(2), -sqrt(2)/2 + r/sqrt(2)

def dist_1(coord):
	x, y = coord
	return sqrt((x - sqrt(2))**2 + y**2)
def dist_2(coord):
	x, y = coord
	return sqrt((x + sqrt(2))**2 + y**2)

def angle_1(coord):
	x, y = coord
	if x - sqrt(2) < 0:
		return -1* cos(atan(y/(x-sqrt(2))))
	return cos(atan(y/(x-sqrt(2))))

def angle_2(coord):
	x, y = coord
	if x + sqrt(2) < 0:
		return -1* cos(atan(y/(x+sqrt(2))))
	return cos(atan(y/(x+sqrt(2))))

def plot_orbits():
	coords = [f(t/100) for t in range(1342)]
	x = [i[0] for i in coords]
	y = [i[1] for i in coords]

	plt.plot(x, y, sqrt(2), 0, 'ro', -1*sqrt(2), 0, 'ro', sqrt(2)/2, sqrt(2)/2, 'go')
	plt.axis([-3, 3, -3, 3])
	plt.show()

def plot_distances():

	x = [i/3.6767 for i in range(1342)]
	d_1 = [dist_1(f(t/100)) for t in range(1342)]
	d_2 = [dist_2(f(t/100)) for t in range(1342)]
	ang_1 = [angle_1(f(t/100)) for t in range(1342)]
	ang_2 = [angle_2(f(t/100)) for t in range(1342)]

	plt.plot(x, d_1, 'b', x, d_2, 'r', x, ang_1, 'b', x, ang_2, 'r')
	plt.axis([0, 365, -2, 4])
	plt.show()

def plot_energy():
	x = [i/3.6767 for i in range(1342)]
	e_1 = [.905/dist_1(f(t/100))**2 for t in range(1342)]
	e_2 = [.905/dist_2(f(t/100))**2 for t in range(1342)]
	e_tot = [(x + y) for x, y in zip(e_1, e_2)]

	print(sum(e_tot)/len(e_tot))

	plt.plot(x, e_1, 'b', x, e_2, 'r', x, e_tot, 'black')
	plt.axis([0, 365, 0, 1.2])
	plt.show()

def plot_seasons():

	x = [i/1.79 for i in range(1342)]
	e_1 = [.905/dist_1(f(t/100))**2 for t in range(1342)]
	e_2 = [.905/dist_2(f(t/100))**2 for t in range(1342)]
	e_tot = [(x + y) for x, y in zip(e_1, e_2)]

	ang_1 = [angle_1(f(t/100)) for t in range(1342)]
	ang_2 = [angle_2(f(t/100)) for t in range(1342)]

	e_1_eq = [x*cos(y*.411) for x, y in zip(e_1, ang_1)]
	e_2_eq = [x*cos(y*.411) for x, y in zip(e_2, ang_2)]
	e_tot_eq = [(x + y) for x, y in zip(e_1_eq, e_2_eq)]

	e_1_n = [x*cos(.785-y*.411) for x, y in zip(e_1, ang_1)]
	e_2_n = [x*cos(.785-y*.411) for x, y in zip(e_2, ang_2)]
	e_tot_n= [(x + y) for x, y in zip(e_1_n, e_2_n)]

	earth_eq = [cos(sin(i/213.58*1.79)*.411) for i in range(1342)] 
	earth_n = [cos(.785 - sin(i/213.58*1.79)*.411) for i in range(1342)] 
	print(min(e_tot_eq), min(earth_eq))
	print(min(e_tot_n), min(earth_n))

	plt.plot(x, e_tot, 'black', x, e_tot_eq, 'r', x, earth_eq, 'g')
	plt.axis([0, 750, 0, 1.2])
	plt.show()
	plt.plot(x, e_tot, 'black', x, e_tot_n, 'r', x, earth_n, 'g')
	plt.axis([0, 750, 0, 1.2])
	plt.show()


plot_seasons()








