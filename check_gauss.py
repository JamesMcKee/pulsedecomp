from optparse import OptionParser
import numpy as np
from scipy import stats

#Getting the options you define when calling the script.
usage="usage: check_gauss.py -f file" 
parser=OptionParser()
parser.add_option("-f", "--file-name", type="string", help="file from paas fit", dest='input_file')
(opts, args) = parser.parse_args()

file=np.loadtxt(opts.input_file,skiprows=1)
bins=np.array(file[:,0])
data=np.array(file[:,1])
model=np.array(file[:,2])

resid = np.subtract(data,model)

k2, p = stats.normaltest(resid)

alpha = 1e-3

if p < alpha:  # null hypothesis: x comes from a normal distribution
	print("2")
else:
	print("1")