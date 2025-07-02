from optparse import OptionParser
import numpy as np
from scipy import stats
from scipy.stats import shapiro

#Getting the options you define when calling the script.
usage="usage: shapiro_wilks_test.py -f file" 
parser=OptionParser()
parser.add_option("-f", "--file-name", type="string", help="file from paas fit", dest='input_file')
(opts, args) = parser.parse_args()

file=np.loadtxt(opts.input_file,skiprows=1)
data=np.array(file[:,1])
model=np.array(file[:,2])

resid = np.subtract(data,model)

# Shapiro-Wilk normality test
stat, p = shapiro(resid)

alpha = 0.05
if p > alpha:
	#Sample looks Gaussian (fail to reject H0)
	print(1)
else:
	#Sample does not look Gaussian (reject H0)
	print(2)

