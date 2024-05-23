import matplotlib.pyplot as plt
import numpy
import glob

x, y_avg, y_std = numpy.loadtxt('data.out', unpack=True)

for file in glob.glob('data/data*in'):
	y = numpy.loadtxt(file, unpack=True)
	plt.plot(x, y, 'o', ms = 4)

plt.errorbar(x, y_avg, marker='*', yerr=y_std)
plt.xlabel('x')

plt.savefig('res.pdf')