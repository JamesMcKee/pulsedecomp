#import numpy as np
import random
from optparse import OptionParser

#Getting the options you define when calling the script.
usage="usage: random.py -f <max amplitude>" 
parser=OptionParser()
parser.add_option("-f", "--max-amp", type="float", help="maximum amplitude of profile for random number generator", dest='max_amp')
parser.add_option("-n", "--n-components", type="int", help="number of von Mises functions to return components for", dest='n_components')
(opts, args) = parser.parse_args()


for i in range(0,opts.n_components):
	centre=random.uniform(0, 1)
	#concentration=random.uniform(0, 1)
	concentration=random.uniform(1, 10000)
	amplitude=random.uniform(float(opts.max_amp)/100, float(opts.max_amp))

	print(centre, concentration, amplitude)

